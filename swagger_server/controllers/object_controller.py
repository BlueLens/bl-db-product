import connexion
from swagger_server.models.add_object_response import AddObjectResponse
from swagger_server.models.get_object_response import GetObjectResponse
from swagger_server.models.object import Object
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime
from orm.objects import Objects


def add_object(body):
    """
    Added a new Object
    
    :param body: Object that needs to be added to the db.
    :type body: dict | bytes

    :rtype: AddObjectResponse
    """
    return Objects.add_object(connexion)


def get_object_by_id(objectId):
    """
    Find Object by ID
    Returns a single Object
    :param objectId: ID of Object to return
    :type objectId: str

    :rtype: GetObjectResponse
    """
    return Objects.get_object_by_id(objectId)
