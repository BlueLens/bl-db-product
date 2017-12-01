import connexion
from swagger_server.models.add_host_response import AddHostResponse
from swagger_server.models.host import Host
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime

from orm.hosts import Hosts

def add_host(body):
    """
    Add a new HOst
    
    :param body: Host object that needs to be added to the db.
    :type body: dict | bytes

    :rtype: AddHostResponse
    """
    return Hosts.add_host(connexion)
