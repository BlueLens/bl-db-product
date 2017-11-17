# coding: utf-8

from __future__ import absolute_import
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class UpdateProductResponse(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, message: str=None):
        """
        UpdateProductResponse - a model defined in Swagger

        :param message: The message of this UpdateProductResponse.
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
    def from_dict(cls, dikt) -> 'UpdateProductResponse':
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The UpdateProductResponse of this UpdateProductResponse.
        :rtype: UpdateProductResponse
        """
        return deserialize_model(dikt, cls)

    @property
    def message(self) -> str:
        """
        Gets the message of this UpdateProductResponse.

        :return: The message of this UpdateProductResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message: str):
        """
        Sets the message of this UpdateProductResponse.

        :param message: The message of this UpdateProductResponse.
        :type message: str
        """

        self._message = message

