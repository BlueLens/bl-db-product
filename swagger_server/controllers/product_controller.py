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

def get_products_by_image_id_and_object_id(imageId, objectId):
    """
    Get Products by imageId and objectId
    Returns Products belongs to a imageId and objectId
    :param imageId:
    :type imageId: str
    :param objectId:
    :type objectId: str

    :rtype: GetProductsResponse
    """
    return Products.get_products_by_image_id_and_object_id(imageId, objectId)

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

def get_products_by_hostcode_and_product_no(hostCode, productNo):
    """
    Get Product by hostCode and productNo
    Returns Product belongs to a Host and productNo
    :param hostCode:
    :type hostCode: str
    :param productNo:
    :type productNo: str

    :rtype: GetProductResponse
    """
    return Products.get_product_by_host_code_and_product_no(hostCode, productNo)

def get_products_by_hostcode(hostCode, offset=None, limit=None):
    """
    Get Product by host_code
    Returns Products belongs to a Host
    :param hostCode:
    :type hostCode: str
    :param offset:
    :type offset: int
    :param limit:
    :type limit: int

    :rtype: GetProductsResponse
    """
    return Products.get_products_by_host_code(hostCode, offset, limit)

def get_products_by_ids(productIds):
    """
    Find Products by IDs
    Returns Products
    :param productIds: IDs of Products to return
    :type productIds: List[str]

    :rtype: GetProductsResponse
    """
    return Products.get_products_by_ids(productIds)

def get_products_by_version_id(versionId, is_indexed=None, offset=0, limit=100):
    """
    Get Product by versionId
    Returns Products belongs to a Version
    :param versionId:
    :type versionId: str
    :param is_indexed:
    :type is_indexed: bool
    :param offset:
    :type offset: int
    :param limit:
    :type limit: int

    :rtype: GetProductsResponse
    """
    return Products.get_products_by_version_id(versionId, is_indexed, offset, limit)

def update_product_by_hostcode_and_productno(hostCode, productNo, body):
    """
    Update an existing Product

    :param hostCode:
    :type hostCode: str
    :param productNo:
    :type productNo: str
    :param body: Product object that needs to be updated to the store
    :type body: dict | bytes

    :rtype: UpdateProductResponse
    """
    return Products.update_product_by_hostcode_and_productno(connexion, hostCode, productNo)

def update_product_by_id(productId, body):
    """
    Update an existing Product

    :param productId: ID of Product to return
    :type productId: str
    :param body: Product object that needs to be updated to the store
    :type body: dict | bytes

    :rtype: UpdateProductResponse
    """
    return Products.update_product_by_id(productId, body)
