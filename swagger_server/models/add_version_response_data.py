# coding: utf-8

from __future__ import absolute_import
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class AddVersionResponseData(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, version_id: str=None, version_name: str=None, modified_count: int=None, created_count: int=None):
        """
        AddVersionResponseData - a model defined in Swagger

        :param version_id: The version_id of this AddVersionResponseData.
        :type version_id: str
        :param version_name: The version_name of this AddVersionResponseData.
        :type version_name: str
        :param modified_count: The modified_count of this AddVersionResponseData.
        :type modified_count: int
        :param created_count: The created_count of this AddVersionResponseData.
        :type created_count: int
        """
        self.swagger_types = {
            'version_id': str,
            'version_name': str,
            'modified_count': int,
            'created_count': int
        }

        self.attribute_map = {
            'version_id': 'version_id',
            'version_name': 'version_name',
            'modified_count': 'modified_count',
            'created_count': 'created_count'
        }

        self._version_id = version_id
        self._version_name = version_name
        self._modified_count = modified_count
        self._created_count = created_count

    @classmethod
    def from_dict(cls, dikt) -> 'AddVersionResponseData':
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AddVersionResponse_data of this AddVersionResponseData.
        :rtype: AddVersionResponseData
        """
        return deserialize_model(dikt, cls)

    @property
    def version_id(self) -> str:
        """
        Gets the version_id of this AddVersionResponseData.

        :return: The version_id of this AddVersionResponseData.
        :rtype: str
        """
        return self._version_id

    @version_id.setter
    def version_id(self, version_id: str):
        """
        Sets the version_id of this AddVersionResponseData.

        :param version_id: The version_id of this AddVersionResponseData.
        :type version_id: str
        """

        self._version_id = version_id

    @property
    def version_name(self) -> str:
        """
        Gets the version_name of this AddVersionResponseData.

        :return: The version_name of this AddVersionResponseData.
        :rtype: str
        """
        return self._version_name

    @version_name.setter
    def version_name(self, version_name: str):
        """
        Sets the version_name of this AddVersionResponseData.

        :param version_name: The version_name of this AddVersionResponseData.
        :type version_name: str
        """

        self._version_name = version_name

    @property
    def modified_count(self) -> int:
        """
        Gets the modified_count of this AddVersionResponseData.

        :return: The modified_count of this AddVersionResponseData.
        :rtype: int
        """
        return self._modified_count

    @modified_count.setter
    def modified_count(self, modified_count: int):
        """
        Sets the modified_count of this AddVersionResponseData.

        :param modified_count: The modified_count of this AddVersionResponseData.
        :type modified_count: int
        """

        self._modified_count = modified_count

    @property
    def created_count(self) -> int:
        """
        Gets the created_count of this AddVersionResponseData.

        :return: The created_count of this AddVersionResponseData.
        :rtype: int
        """
        return self._created_count

    @created_count.setter
    def created_count(self, created_count: int):
        """
        Sets the created_count of this AddVersionResponseData.

        :param created_count: The created_count of this AddVersionResponseData.
        :type created_count: int
        """

        self._created_count = created_count

