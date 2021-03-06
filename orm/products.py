
import os
import time
from bson.objectid import ObjectId
from orm.database import DataBase
from swagger_server.models.product import Product
from swagger_server.models.image import Image
from swagger_server.models.add_product_response import AddProductResponse
from swagger_server.models.get_product_response import GetProductResponse
from swagger_server.models.get_products_response import GetProductsResponse
from swagger_server.models.delete_product_response import DeleteProductResponse
from swagger_server.models.add_product_response_data import AddProductResponseData

from swagger_server.models.update_product_response import UpdateProductResponse

from bluelens_log import Logging

REDIS_SERVER = os.environ['REDIS_SERVER']
REDIS_PASSWORD = os.environ['REDIS_PASSWORD']

options = {
  'REDIS_SERVER': REDIS_SERVER,
  'REDIS_PASSWORD': REDIS_PASSWORD
}
log = Logging(options, tag='bl-db-product:Products')

class Products(DataBase):
  def __init__(self):
    super().__init__()
    self.products = self.db.products
    self.images = self.db.images

  @staticmethod
  def add_product(connexion):
    start_time = time.time()
    orm = Products()
    res = AddProductResponse()
    data = AddProductResponseData()
    response_status = 200
    if connexion.request.is_json:
      product = connexion.request.get_json()

      try:
        r = orm.products.insert(product)
        res.message = 'Successful'
        data.product_id = str(r)
        res.data = data
      except Exception as e:
        res.message = str(e)
        response_status = 400

    elapsed_time = time.time() - start_time
    log.debug('add_product time: ' + str(elapsed_time))
    return res, response_status

  @staticmethod
  def update_product_by_id(product_id, product):
    start_time = time.time()
    orm = Products()
    res = UpdateProductResponse()
    response_status = 200

    try:
      r = orm.products.update_one({"_id": ObjectId(product_id)},
                                  {"$set": product})
      res.modified_count = r.modified_count
      if r.modified_count > 0:
        res.message = 'successfully updated'
      elif r.modified_count == 0:
        res.message = 'nothing to update'
    except Exception as e:
      res.message = str(e)
      response_status = 400

    # elapsed_time = time.time() - start_time
    # log.info('update_product time: ' + str(elapsed_time))
    return res, response_status

  @staticmethod
  def update_product_by_hostcode_and_productno(connexion, host_code, product_no):
    start_time = time.time()
    orm = Products()
    res = UpdateProductResponse()
    response_status = 200
    if connexion.request.is_json:
      product_json = connexion.request.get_json()
      # log.debug(product_json)

      try:
        r = orm.products.update_one({"host_code": host_code, "product_no": product_no},
                                    {"$set": product_json},
                                    upsert=True)
        res.created_count = 0
        res.modified_count = r.modified_count
        if r.modified_count > 0:
          res.message = 'successfully updated'
        elif r.upserted_id != None:
          res.product_id = str(r.upserted_id)
          res.created_count = 1
          res.message = 'successfully created'
        elif r.modified_count == 0:
          res.message = 'nothing to update'
      except Exception as e:
        res.message = str(e)
        response_status = 400

    elapsed_time = time.time() - start_time
    log.debug('update_product_by_hostcode_and_productno time: ' + str(elapsed_time))
    return res, response_status


  @staticmethod
  def get_product_by_id(product_id):
    start_time = time.time()
    orm = Products()
    res = GetProductResponse()
    response_status = 200

    try:
      r = orm.products.find_one({"_id": ObjectId(product_id)})
      res.message = 'Successful'
      product = Product.from_dict(r)
      product.id = str(r['_id'])
      res.data = product.to_dict()
    except Exception as e:
      res.message = str(e)
      response_status = 400

    elapsed_time = time.time() - start_time
    log.debug('get_product_by_id time: ' + str(elapsed_time))
    return res, response_status


  @staticmethod
  def get_products_by_ids(product_ids):
    start_time = time.time()
    orm = Products()
    res = GetProductsResponse()
    response_status = 200

    try:
      ids = []
      for id in product_ids:
        ids.append(ObjectId(id))

      res_products = orm.products.find({"_id": {"$in": ids}})
      products = []
      for p in res_products:
        p['sub_images'] = None
        products.append(Product.from_dict(p))
      res.message = 'Successful'
      res.data = products
    except Exception as e:
      res.message = str(e)
      response_status = 400

    elapsed_time = time.time() - start_time
    log.debug('get_products_by_ids time: ' + str(elapsed_time))
    return res, response_status

  @staticmethod
  def get_products_by_version_id(version_id, is_indexed, offset=0, limit=5):
    start_time = time.time()
    orm = Products()
    res = GetProductsResponse()
    response_status = 200

    try:
      response = orm.products.find({"version_id": version_id,
                                    "is_indexed": is_indexed})\
                                    .skip(offset).limit(limit)

      res.message = 'Successful'

      products = []
      for r in response:
        # log.debug(r)
        product = Product.from_dict(r)
        product.id = str(r['_id'])
        products.append(product)

      if len(products) == 0:
        res.message = 'No matched products'
        response_status = 404
        res.data = None
      else:
        res.data = products

    except Exception as e:
      res.message = str(e)
      response_status = 400

    # log.debug(res)
    elapsed_time = time.time() - start_time
    log.debug('get_products_by_version_id time: ' + str(elapsed_time))
    return res, response_status

  @staticmethod
  def get_products_by_host_code(host_code, offset=0, limit=1000):
    start_time = time.time()
    orm = Products()
    res = GetProductsResponse()
    response_status = 200

    try:
      response = orm.products.find({"host_code": host_code}).skip(offset).limit(limit)
      res.message = 'Successful'

      products = []
      for r in response:
        # log.debug(r)
        product = Product.from_dict(r)
        product.id = str(r['_id'])
        products.append(product)
      res.data = products
    except Exception as e:
      res.message = str(e)
      response_status = 400

    # log.debug(res)
    elapsed_time = time.time() - start_time
    log.info('get_products_by_host_code time: ' + str(elapsed_time))
    return res, response_status

  @staticmethod
  def get_products_by_image_id_and_object_id(image_id, object_id):
    start_time = time.time()
    log.debug(image_id)
    log.debug(object_id)
    orm = Products()
    res = GetProductsResponse()
    response_status = 200

    try:
      r = orm.images.find_one({"_id": ObjectId(image_id)})
      res.message = 'Successful'
      image = Image.from_dict(r)
      boxes = image.boxes
      products = boxes[int(object_id)]['products']
      res.data = products
    except Exception as e:
      res.message = str(e)
      response_status = 400

    elapsed_time = time.time() - start_time
    log.debug('get_products_by_image_id_and_object_id time: ' + str(elapsed_time))
    return res, response_status

  @staticmethod
  def get_product_by_host_code_and_product_no(host_code, product_no):
    start_time = time.time()
    orm = Products()
    res = GetProductResponse()
    response_status = 200

    try:
      r = orm.products.find_one({"host_code": host_code, "product_no": product_no})
      res.message = 'Successful'
      product = Product.from_dict(r)
      product.id = str(r['_id'])
      res.data = product.to_dict()
    except Exception as e:
      res.message = str(e)
      response_status = 400

    elapsed_time = time.time() - start_time
    log.debug('get_product_by_host_code_and_product_no time: ' + str(elapsed_time))
    return res, response_status

  @staticmethod
  def get_product_by_host_code_and_version_id(host_code, version_id, is_indexed=False,
                                              offset=0, limit=100):
    start_time = time.time()
    orm = Products()
    res = GetProductsResponse()
    response_status = 200

    try:
      response = orm.products.find({"host_code": host_code,
                                    "version_id": version_id,
                                    "is_indexed": is_indexed})\
                                    .skip(offset).limit(limit)
      res.message = 'Successful'

      products = []
      for r in response:
        # log.debug(r)
        product = Product.from_dict(r)
        product.id = str(r['_id'])
        products.append(product)

      if len(products) == 0:
        res.message = 'No matched products'
        response_status = 404
        res.data = None
      else:
        res.data = products

    except Exception as e:
      res.message = str(e)
      response_status = 400

    # log.debug(res)
    elapsed_time = time.time() - start_time
    log.debug('get_product_by_host_code time: ' + str(elapsed_time))
    return res, response_status

  @staticmethod
  def delete_product_by_id(product_id):
    start_time = time.time()
    orm = Products()
    res = DeleteProductResponse()
    response_status = 200
    try:
      r = orm.products.delete_one({"_id": ObjectId(product_id)})
      if r.deleted_count > 0:
        res.message = 'Successfully deleted'
      else:
        response_status = 404
        res.message = 'None of Products are deleted'
    except Exception as e:
      res.message = str(e)
      response_status = 400

    elapsed_time = time.time() - start_time
    log.debug('delete_product_by_id time: ' + str(elapsed_time))
    return res, response_status

  @staticmethod
  def delete_products_by_hostcode_and_version_id(host_code, version_id, except_version=True):
    start_time = time.time()
    orm = Products()
    res = DeleteProductResponse()
    response_status = 200
    try:

      if except_version == True:
        r = orm.products.delete_many({"host_code": host_code,
                                      "version_id": {"$ne": version_id}})
      else:
        r = orm.products.delete_many({"host_code": host_code,
                                      "version_id": version_id})
      if r.deleted_count > 0:
        res.message = 'Successfully deleted: ' + str(r.deleted_count)
      else:
        response_status = 404
        res.message = 'None of Products are deleted'
    except Exception as e:
      res.message = str(e)
      response_status = 400

    elapsed_time = time.time() - start_time
    log.debug('delete_product_by_hostcode_and_version_id time: ' + str(elapsed_time))
    return res, response_status
