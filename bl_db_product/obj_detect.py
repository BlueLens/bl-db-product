from __future__ import print_function
import uuid

import os

import numpy as np
import argparse
import multiprocessing
import tensorflow as tf
from PIL import Image
import json
import urllib
import time
from pprint import pprint
from util import label_map_util, s3
from object_detection.utils import visualization_utils as vis_util
import stylelens_index
from stylelens_index.rest import ApiException
from stylelens_feature import feature_extract
import stylelens_search
from stylelens_search.rest import ApiException

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO



TMP_CROP_IMG_FILE = './tmp.jpg'


NUM_CLASSES = 89

HOST_URL = 'host_url'
TAG = 'tag'
SUB_CATEGORY = 'sub_category'
PRODUCT_NAME = 'product_name'
IMAGE_URL = 'image_url'
PRODUCT_PRICE = 'product_price'
CURRENCY_UNIT = 'currency_unit'
PRODUCT_URL = 'product_url'
PRODUCT_NO = 'product_no'
MAIN = 'main'
NATION = 'nation'


AWS_ACCESS_KEY = os.environ['AWS_ACCESS_KEY'].replace('"', '')
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY'].replace('"', '')

OD_MODEL = os.environ['OD_MODEL']
OD_LABELS = os.environ['OD_LABELS']

AWS_BUCKET = 'bluelens-style-model'
AWS_MODEL_DIR = 'object_detection'

class ObjectDetector:
  def __init__(self):
    # self.download_model()
    # Loading label map
    self.__api_instance = stylelens_index.ImageApi()
    self.__search = stylelens_search.SearchApi()
    label_map = label_map_util.load_labelmap(OD_LABELS)
    print(label_map)
    categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=NUM_CLASSES,
                                                                use_display_name=True)
    self.__category_index = label_map_util.create_category_index(categories)
    self.__detection_graph = tf.Graph()
    with self.__detection_graph.as_default():
      od_graph_def = tf.GraphDef()
      with tf.gfile.GFile(OD_MODEL, 'rb') as fid:
        serialized_graph = fid.read()
        od_graph_def.ParseFromString(serialized_graph)
        tf.import_graph_def(od_graph_def, name='')

      self.__sess = tf.Session(graph=self.__detection_graph)

    self.image_feature = feature_extract.ExtractFeature()
    print('_init_ done')

  def download_model(self):
    storage = s3.S3(AWS_ACCESS_KEY, AWS_SECRET_ACCESS_KEY)
    storage.download_file_from_bucket(AWS_BUCKET,
                                      os.path.join(LOCAL_MODEL_DIR, MODEL_FILE),
                                      os.path.join(AWS_MODEL_DIR, MODEL_FILE))
    storage.download_file_from_bucket(AWS_BUCKET,
                                      os.path.join(LOCAL_MODEL_DIR, LABEL_FILE),
                                      os.path.join(AWS_MODEL_DIR, LABEL_FILE))

  def query(self, image):
      origin_size = image.size
      size = 300, 300
      image.thumbnail(size, Image.ANTIALIAS)
      new_size = image.size

      ratio = 1
      if new_size[0] == 300:
        ratio = new_size[0] / origin_size[0]
      elif new_size[1] == 300:
        ratio = new_size[1] / origin_size[1]
      image_np = self.load_image_into_numpy_array(image)

      show_box = True
      out_image, boxes, scores, classes, num_detections = self.detect_objects(image_np, self.__sess, self.__detection_graph, show_box)

      image_info = stylelens_index.Image()
      out_boxes = self.take_object(
                  image_info,
                  ratio,
                  out_image,
                  np.squeeze(boxes),
                  np.squeeze(scores),
                  np.squeeze(classes).astype(np.int32))

      item = {}
      if len(out_boxes) < 2:
        if len(out_boxes) == 0:
          item['box'] = [0, 0, 0, 0]
          image.save(TMP_CROP_IMG_FILE)
        elif len(out_boxes) == 1:
          self.save_box_to_file(out_boxes[0]['box'], image, ratio)
          item['box'] = out_boxes[0]['box']
          item['class_code'] = out_boxes[0]['class_code']
          item['class_name'] = out_boxes[0]['class_name']
          out_boxes.clear()

        try:
          api_response = self.__search.search_image(file=TMP_CROP_IMG_FILE)
          if api_response.code == 0 and api_response.data != None:
            res_images = api_response.data.images
            item['images'] = res_images
            out_boxes.append(item)

        except ApiException as e:
          print("Exception when calling SearchApi->search_image: %s\n" % e)

      if show_box:
        img = Image.fromarray(out_image, 'RGB')
        img.show()

      return out_boxes

  def save_box_to_file(self, box, image, ratio):
    left = box[0] * ratio
    right = box[1] * ratio
    top = box[2] * ratio
    bottom = box[3] * ratio
    area = (left, top, left + abs(left-right), top + abs(bottom-top))
    new_image = image.crop(area)
    new_image.save(TMP_CROP_IMG_FILE)
    return new_image

  def take_object(self, image_info, ratio, image_np, boxes, scores, classes):
    max_boxes_to_save = 3
    min_score_thresh = 0.1
    taken_boxes = []
    if not max_boxes_to_save:
      max_boxes_to_save = boxes.shape[0]
    for i in range(min(max_boxes_to_save, boxes.shape[0])):
      if scores is None or scores[i] > min_score_thresh:
        print(scores[i])
        if classes[i] in self.__category_index.keys():
          class_name = self.__category_index[classes[i]]['name']
          class_code = self.__category_index[classes[i]]['code']
        else:
          class_name = 'na'
          class_code = 'na'
        print(boxes.shape)
        print(boxes[i])
        print(boxes[i].shape)
        ymin, xmin, ymax, xmax = tuple(boxes[i].tolist())

        use_normalized_coordinates = True
        left, right, top, bottom = self.crop_bounding_box(
          image_info,
          image_np,
          ymin,
          xmin,
          ymax,
          xmax,
          use_normalized_coordinates=use_normalized_coordinates)
        item = {}

        item['box'] = [left / ratio, right / ratio, top / ratio, bottom / ratio]
        item['class_name'] = class_name
        item['class_code'] = class_code
        taken_boxes.append(item)
    return taken_boxes

  def load_image_into_numpy_array(self, image):
    (im_width, im_height) = image.size
    return np.array(image.getdata()).reshape(
        (im_height, im_width, 3)).astype(np.uint8)

  def crop_bounding_box(self,
                        image_info,
                        image,
                         ymin,
                         xmin,
                         ymax,
                         xmax,
                         use_normalized_coordinates=True):
    """Adds a bounding box to an image (numpy array).

    Args:
      image: a numpy array with shape [height, width, 3].
      ymin: ymin of bounding box in normalized coordinates (same below).
      xmin: xmin of bounding box.
      ymax: ymax of bounding box.
      xmax: xmax of bounding box.
      name: classname
      color: color to draw bounding box. Default is red.
      thickness: line thickness. Default value is 4.
      display_str_list: list of strings to display in box
                        each to be shown on its own line).
      use_normalized_coordinates: If True (default), treat coordinates
        ymin, xmin, ymax, xmax as relative to the image.  Otherwise treat
        coordinates as absolute.
    """
    image_pil = Image.fromarray(np.uint8(image)).convert('RGB')
    im_width, im_height = image_pil.size
    if use_normalized_coordinates:
      (left, right, top, bottom) = (xmin * im_width, xmax * im_width,
                                    ymin * im_height, ymax * im_height)
    else:
      (left, right, top, bottom) = (xmin, xmax, ymin, ymax)

    # print(image_pil)
    # area = (left, top, left + abs(left-right), top + abs(bottom-top))
    # cropped_img = image_pil.crop(area)
    # cropped_img.save(TMP_CROP_IMG_FILE)
    # img_feature_vec = self.image_feature.extract_feature(TMP_CROP_IMG_FILE)
    # cropped_img.show()
    # id = self.save_to_db(image_info)


    # try:
    #   api_response = self.__search.search_image(file=TMP_CROP_IMG_FILE)
    #   if api_response.code == 0 and api_response.data != None:
    #     res_images = api_response.data.images
    #
    # except ApiException as e:
    #   print("Exception when calling SearchApi->search_image: %s\n" % e)

    # save_image_to_file(image_pil, ymin, xmin, ymax, xmax,
    #                            use_normalized_coordinates)
    # np.copyto(image, np.array(image_pil))
    # return id, res_images, left, right, top, bottom
    # return id, left, right, top, bottom
    return left, right, top, bottom

  def search_image(self, feature_vector):
    #ToDo: Have to implement searcning image from bl-api-search
    print('search_image')

  def save_to_db(self, image):
    try:
      api_response = self.__api_instance.add_image(image)
      pprint(api_response)
    except ApiException as e:
      print("Exception when calling ImageApi->add_image: %s\n" % e)
    return api_response.data._id

  def detect_objects(self, image_np, sess, detection_graph, show_box=True):
      # Expand dimensions since the model expects images to have shape: [1, None, None, 3]
      image_np_expanded = np.expand_dims(image_np, axis=0)
      image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')

      # Each box represents a part of the image where a particular object was detected.
      boxes = detection_graph.get_tensor_by_name('detection_boxes:0')

      # Each score represent how level of confidence for each of the objects.
      # Score is shown on the result image, together with the class label.
      scores = detection_graph.get_tensor_by_name('detection_scores:0')
      classes = detection_graph.get_tensor_by_name('detection_classes:0')
      num_detections = detection_graph.get_tensor_by_name('num_detections:0')

      # Actual detection.
      (boxes, scores, classes, num_detections) = sess.run(
          [boxes, scores, classes, num_detections],
          feed_dict={image_tensor: image_np_expanded})

      if show_box:
        # Visualization of the results of a detection.
        vis_util.visualize_boxes_and_labels_on_image_array(
            image_np,
            np.squeeze(boxes),
            np.squeeze(classes).astype(np.int32),
            np.squeeze(scores),
            self.__category_index,
            use_normalized_coordinates=True,
            max_boxes_to_draw=3,
            min_score_thresh=.05,
            line_thickness=8)
      # print(image_np)
      return image_np, boxes, scores, classes, num_detections

