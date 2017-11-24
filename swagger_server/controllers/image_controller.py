import connexion
from swagger_server.models.add_image_response import AddImageResponse
from swagger_server.models.get_products_response import GetProductsResponse
from swagger_server.models.image import Image
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime
from orm.images import Images


def add_image(body):
    """
    Added a new Image
    
    :param body: Product object that needs to be added to the db.
    :type body: dict | bytes

    :rtype: AddImageResponse
    """
    return Images.add_image(connexion)
