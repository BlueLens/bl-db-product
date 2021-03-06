# coding: utf-8

from __future__ import absolute_import
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class DeleteProductResponse(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, message: str=None):
        """
        DeleteProductResponse - a model defined in Swagger

        :param message: The message of this DeleteProductResponse.
        :type message: str
        """
        self.swagger_types = {
            'message': str
        }

        self.attribute_map = {
            'message': 'message'
        }

        self._message = message

    @classmethod
    def from_dict(cls, dikt) -> 'DeleteProductResponse':
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The DeleteProductResponse of this DeleteProductResponse.
        :rtype: DeleteProductResponse
        """
        return deserialize_model(dikt, cls)

    @property
    def message(self) -> str:
        """
        Gets the message of this DeleteProductResponse.

        :return: The message of this DeleteProductResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message: str):
        """
        Sets the message of this DeleteProductResponse.

        :param message: The message of this DeleteProductResponse.
        :type message: str
        """

        self._message = message

