
import os
import time
from bson.objectid import ObjectId
from orm.database import DataBase
from swagger_server.models.object import Object
from swagger_server.models.add_object_response import AddObjectResponse
from swagger_server.models.add_object_response_data import AddObjectResponseData
from swagger_server.models.get_object_response import GetObjectResponse

from bluelens_log import Logging

REDIS_SERVER = os.environ['REDIS_SERVER']
REDIS_PASSWORD = os.environ['REDIS_PASSWORD']

options = {
  'REDIS_SERVER': REDIS_SERVER,
  'REDIS_PASSWORD': REDIS_PASSWORD
}
log = Logging(options, tag='bl-db-product:Products')

class Objects(DataBase):
  def __init__(self):
    super().__init__()
    self.objects = self.db.objects

  @staticmethod
  def add_object(connexion):
    start_time = time.time()
    orm = Objects()
    res = AddObjectResponse()
    data = AddObjectResponseData()
    response_status = 200
    if connexion.request.is_json:
      body = Object.from_dict(connexion.request.get_json())

      try:
        r = orm.objects.insert(body.to_dict())
        res.message = 'Successful'
        data.object_id = str(r)
        res.data = data
      except Exception as e:
        res.message = str(e)
        response_status = 400

    elapsed_time = time.time() - start_time
    log.info('add_object time: ' + str(elapsed_time))
    return res, response_status

  @staticmethod
  def get_object_by_id(object_id):
    start_time = time.time()
    orm = Objects()
    res = GetObjectResponse()
    response_status = 200

    try:
      r = orm.objects.find_one({"_id": ObjectId(object_id)})
      res.message = 'Successful'
      object = Object.from_dict(r)
      object.id = str(r['_id'])
      res.data = object.to_dict()
    except Exception as e:
      res.message = str(e)
      response_status = 400

    elapsed_time = time.time() - start_time
    log.info('get_object_by_id time: ' + str(elapsed_time))

    return res, response_status

