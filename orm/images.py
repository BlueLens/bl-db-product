
import os
from bson.objectid import ObjectId
from orm.database import DataBase
from swagger_server.models.image import Image
from swagger_server.models.add_image_response import AddImageResponse
from swagger_server.models.add_image_response_data import AddImageResponseData

from bluelens_log import Logging

REDIS_SERVER = os.environ['REDIS_SERVER']
REDIS_PASSWORD = os.environ['REDIS_PASSWORD']

options = {
  'REDIS_SERVER': REDIS_SERVER,
  'REDIS_PASSWORD': REDIS_PASSWORD
}
log = Logging(options, tag='bl-db-product:Images')

class Images(DataBase):
  def __init__(self):
    super().__init__()
    self.images = self.db.images

  @staticmethod
  def add_image(connexion):
    log.debug('add_image')
    orm = Images()
    res = AddImageResponse()
    data = AddImageResponseData()
    response_status = 200
    if connexion.request.is_json:
      body = Image.from_dict(connexion.request.get_json())

      try:
        r = orm.images.insert(body.to_dict())
        res.message = 'Successful'
        data.image_id = str(r)
        log.debug(data.image_id)
        res.data = data
      except Exception as e:
        res.message = str(e)
        response_status = 400

    return res, response_status

