import os
from pymongo import MongoClient


DB_HOST = os.environ['DB_HOST']
DB_PORT = os.environ['DB_PORT']
DB_NAME = os.environ['DB_NAME']


class DataBase(object):
  def __init__(self):
    self.client = MongoClient('mongodb://root:x4fSKpXCX4bE@' + DB_HOST + ':' + DB_PORT)
    self.db = self.client[DB_NAME]


