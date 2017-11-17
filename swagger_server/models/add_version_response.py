# coding: utf-8

from __future__ import absolute_import
from swagger_server.models.add_version_response_data import AddVersionResponseData
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class AddVersionResponse(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, message: str=None, data: AddVersionResponseData=None):
        """
        AddVersionResponse - a model defined in Swagger

        :param message: The message of this AddVersionResponse.
        :type message: str
        :param data: The data of this AddVersionResponse.
        :type data: AddVersionResponseData
        """
        self.swagger_types = {
            'message': str,
            'data': AddVersionResponseData
        }

        self.attribute_map = {
            'message': 'message',
            'data': 'data'
        }

        self._message = message
        self._data = data

    @classmethod
    def from_dict(cls, dikt) -> 'AddVersionResponse':
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AddVersionResponse of this AddVersionResponse.
        :rtype: AddVersionResponse
        """
        return deserialize_model(dikt, cls)

    @property
    def message(self) -> str:
        """
        Gets the message of this AddVersionResponse.

        :return: The message of this AddVersionResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message: str):
        """
        Sets the message of this AddVersionResponse.

        :param message: The message of this AddVersionResponse.
        :type message: str
        """

        self._message = message

    @property
    def data(self) -> AddVersionResponseData:
        """
        Gets the data of this AddVersionResponse.

        :return: The data of this AddVersionResponse.
        :rtype: AddVersionResponseData
        """
        return self._data

    @data.setter
    def data(self, data: AddVersionResponseData):
        """
        Sets the data of this AddVersionResponse.

        :param data: The data of this AddVersionResponse.
        :type data: AddVersionResponseData
        """

        self._data = data
