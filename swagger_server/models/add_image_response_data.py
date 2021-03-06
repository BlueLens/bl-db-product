# coding: utf-8

from __future__ import absolute_import
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class AddImageResponseData(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, image_id: str=None):
        """
        AddImageResponseData - a model defined in Swagger

        :param image_id: The image_id of this AddImageResponseData.
        :type image_id: str
        """
        self.swagger_types = {
            'image_id': str
        }

        self.attribute_map = {
            'image_id': 'image_id'
        }

        self._image_id = image_id

    @classmethod
    def from_dict(cls, dikt) -> 'AddImageResponseData':
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AddImageResponse_data of this AddImageResponseData.
        :rtype: AddImageResponseData
        """
        return deserialize_model(dikt, cls)

    @property
    def image_id(self) -> str:
        """
        Gets the image_id of this AddImageResponseData.

        :return: The image_id of this AddImageResponseData.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id: str):
        """
        Sets the image_id of this AddImageResponseData.

        :param image_id: The image_id of this AddImageResponseData.
        :type image_id: str
        """

        self._image_id = image_id

