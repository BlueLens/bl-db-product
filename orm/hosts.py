import os
from bson.objectid import ObjectId
import time
from orm.database import DataBase

from swagger_server.models.host import Host
from swagger_server.models.add_host_response import AddHostResponse
from swagger_server.models.get_hosts_response import GetHostsResponse
from swagger_server.models.add_host_response_data import AddHostResponseData
from bluelens_log import Logging

REDIS_SERVER = os.environ['REDIS_SERVER']
REDIS_PASSWORD = os.environ['REDIS_PASSWORD']

options = {
  'REDIS_SERVER': REDIS_SERVER,
  'REDIS_PASSWORD': REDIS_PASSWORD
}
log = Logging(options, tag='bl-db-product:Hosts')

class Hosts(DataBase):
  def __init__(self):
    super().__init__()
    self.hosts = self.db.hosts

  @staticmethod
  def add_host(connexion):
    orm = Hosts()
    res = AddHostResponse()
    data = AddHostResponseData()
    response_status = 200

    if connexion.request.is_json:
      host_json = connexion.request.get_json()

      try:
        r = orm.hosts.update_one({"host_code": host_json['host_code']},
                                 {"$set": host_json},
                                 upsert=True)
        if r.matched_count > 0:
          if r.modified_count == 0:
            res.message = 'Already existing'
          elif r.modified_count > 0:
            res.message = 'Already existing & Updated with new data'
        else:
          res.message = 'Successfully added'
          data.host_id = str(r.upserted_id)
          res.data = data

      except Exception as e:
        res.message = str(e)
        response_status = 400

    return res, response_status

  @staticmethod
  def get_hosts(offset=0, limit=1000):
    start_time = time.time()
    orm = Hosts()
    res = GetHostsResponse()
    response_status = 200

    try:
      response = orm.hosts.find({}).skip(offset).limit(limit)
      res.message = 'Successful'

      hosts = []
      for h in response:
        log.debug(h)
        hosts.append(Host.from_dict(h))
      res.data = hosts
    except Exception as e:
      res.message = str(e)
      response_status = 400

    # log.debug(res)
    elapsed_time = time.time() - start_time
    log.info('get_hosts time: ' + str(elapsed_time))
    return res, response_status

