import connexion
from swagger_server.models.add_product_response import AddProductResponse
from swagger_server.models.delete_product_response import DeleteProductResponse
from swagger_server.models.get_product_response import GetProductResponse
from swagger_server.models.product import Product
from swagger_server.models.update_product_response import UpdateProductResponse
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from swagger_server.util import deserialize_date, deserialize_datetime
from orm.products import Products

def add_product(body):
    """
    Added a new Product
    
    :param body: Product object that needs to be added to the db.
    :type body: dict | bytes

    :rtype: AddProductResponse
    """
    return Products.add_product(connexion)


def delete_product_by_id(productId):
    """
    Deletes a Product
    
    :param productId: Product id to delete
    :type productId: str

    :rtype: DeleteProductResponse
    """
    print(productId)
    return Products.delete_product_by_id(productId)


def get_product_by_id(productId):
    """
    Find Product by ID
    Returns a single Product
    :param productId: ID of Product to return
    :type productId: str

    :rtype: GetProductResponse
    """
    print(productId)
    return Products.get_product_by_id(productId)

def get_products_by_hostcode(hostCode):
    """
    Get Product by host_code
    Returns Products belongs to a Host
    :param hostCode:
    :type hostCode: str

    :rtype: GetProductsResponse
    """
    return Products.get_product_by_host_code(hostCode)

def update_product(body):
    """
    Update an existing Product
    
    :param body: Product object that needs to be updated to the store
    :type body: dict | bytes

    :rtype: UpdateProductResponse
    """
    return Products.update_product(connexion)
