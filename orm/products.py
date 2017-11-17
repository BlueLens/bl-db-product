
from bson.objectid import ObjectId
from orm.database import DataBase
from swagger_server.models.product import Product
from swagger_server.models.add_product_response import AddProductResponse
from swagger_server.models.get_product_response import GetProductResponse
from swagger_server.models.delete_product_response import DeleteProductResponse
from swagger_server.models.add_product_response_data import AddProductResponseData

from swagger_server.models.update_product_response import UpdateProductResponse


class Products(DataBase):
  def __init__(self):
    super().__init__()
    self.products = self.db.products

  @staticmethod
  def add_product(connexion):
    orm = Products()
    res = AddProductResponse()
    data = AddProductResponseData()
    response_status = 200
    if connexion.request.is_json:
      body = Product.from_dict(connexion.request.get_json())

      try:
        r = orm.products.insert(body.to_dict())
        res.message = 'Successful'
        data.product_id = str(r)
        res.data = data
      except Exception as e:
        res.message = str(e)
        response_status = 400

    return res, response_status

  @staticmethod
  def update_product(connexion):
    orm = Products()
    res = UpdateProductResponse()
    response_status = 200
    if connexion.request.is_json:
      product = Product.from_dict(connexion.request.get_json())

      try:
        r = orm.products.update_one({"_id": ObjectId(product.id)},
                                    {"$set": product.to_dict()})
        if r.modified_count > 0:
          res.message = 'Successfully updated'
        elif r.modified_count == 0:
          res.message = 'Nothing to update'
      except Exception as e:
        res.message = str(e)
        response_status = 400

    return res, response_status

  @staticmethod
  def get_product_by_id(product_id):
    print('get_product')
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

    return res, response_status

  @staticmethod
  def delete_product_by_id(product_id):
    orm = Products()
    res = DeleteProductResponse()
    response_status = 200
    try:
      r = orm.products.delete_one({"_id": ObjectId(product_id)})
      if r.deleted_count > 0:
        res.message = 'Successfully deleted'
      else:
        response_status = 404
        res.message = 'Product not found'
    except Exception as e:
      res.message = str(e)
      response_status = 400

    return res, response_status
