import connexion
from swagger_server.models.add_version_response import AddVersionResponse
from swagger_server.models.get_version_response import GetVersionResponse
from swagger_server.models.latest_version_response import LatestVersionResponse
from swagger_server.models.version import Version
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime

from orm.versions import Versions


def add_version(body=None):
    """
    Add a new Version
    
    :param body: Version object that needs to be added to the db.
    :type body: dict | bytes

    :rtype: AddVersionResponse
    """
    return Versions.add_version(connexion)


def get_latest_version():
    """
    Gat latest Version
    Returns a latest Version

    :rtype: LatestVersionResponse
    """
    return Versions.get_latest_version()


def get_version_by_id(versionId):
    """
    Gat Version by ID
    Returns a Version
    :param versionId: ID of Version to return
    :type versionId: str

    :rtype: GetVersionResponse
    """
    return Versions.get_version_by_id(versionId)
