# coding: utf-8

from __future__ import absolute_import
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class Object(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id: str=None, name: str=None, product_id: str=None, version: str=None, class_code: str=None, class_name: str=None, storage: str=None, bucket: str=None, color: int=None, texture: str=None, fabric: str=None, shape: str=None, part: str=None, style: str=None):
        """
        Object - a model defined in Swagger

        :param id: The id of this Object.
        :type id: str
        :param name: The name of this Object.
        :type name: str
        :param product_id: The product_id of this Object.
        :type product_id: str
        :param version: The version of this Object.
        :type version: str
        :param class_code: The class_code of this Object.
        :type class_code: str
        :param class_name: The class_name of this Object.
        :type class_name: str
        :param storage: The storage of this Object.
        :type storage: str
        :param bucket: The bucket of this Object.
        :type bucket: str
        :param color: The color of this Object.
        :type color: int
        :param texture: The texture of this Object.
        :type texture: str
        :param fabric: The fabric of this Object.
        :type fabric: str
        :param shape: The shape of this Object.
        :type shape: str
        :param part: The part of this Object.
        :type part: str
        :param style: The style of this Object.
        :type style: str
        """
        self.swagger_types = {
            'id': str,
            'name': str,
            'product_id': str,
            'version': str,
            'class_code': str,
            'class_name': str,
            'storage': str,
            'bucket': str,
            'color': int,
            'texture': str,
            'fabric': str,
            'shape': str,
            'part': str,
            'style': str
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'product_id': 'product_id',
            'version': 'version',
            'class_code': 'class_code',
            'class_name': 'class_name',
            'storage': 'storage',
            'bucket': 'bucket',
            'color': 'color',
            'texture': 'texture',
            'fabric': 'fabric',
            'shape': 'shape',
            'part': 'part',
            'style': 'style'
        }

        self._id = id
        self._name = name
        self._product_id = product_id
        self._version = version
        self._class_code = class_code
        self._class_name = class_name
        self._storage = storage
        self._bucket = bucket
        self._color = color
        self._texture = texture
        self._fabric = fabric
        self._shape = shape
        self._part = part
        self._style = style

    @classmethod
    def from_dict(cls, dikt) -> 'Object':
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Object of this Object.
        :rtype: Object
        """
        return deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """
        Gets the id of this Object.

        :return: The id of this Object.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """
        Sets the id of this Object.

        :param id: The id of this Object.
        :type id: str
        """

        self._id = id

    @property
    def name(self) -> str:
        """
        Gets the name of this Object.

        :return: The name of this Object.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """
        Sets the name of this Object.

        :param name: The name of this Object.
        :type name: str
        """

        self._name = name

    @property
    def product_id(self) -> str:
        """
        Gets the product_id of this Object.

        :return: The product_id of this Object.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id: str):
        """
        Sets the product_id of this Object.

        :param product_id: The product_id of this Object.
        :type product_id: str
        """

        self._product_id = product_id

    @property
    def version(self) -> str:
        """
        Gets the version of this Object.

        :return: The version of this Object.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version: str):
        """
        Sets the version of this Object.

        :param version: The version of this Object.
        :type version: str
        """

        self._version = version

    @property
    def class_code(self) -> str:
        """
        Gets the class_code of this Object.

        :return: The class_code of this Object.
        :rtype: str
        """
        return self._class_code

    @class_code.setter
    def class_code(self, class_code: str):
        """
        Sets the class_code of this Object.

        :param class_code: The class_code of this Object.
        :type class_code: str
        """

        self._class_code = class_code

    @property
    def class_name(self) -> str:
        """
        Gets the class_name of this Object.

        :return: The class_name of this Object.
        :rtype: str
        """
        return self._class_name

    @class_name.setter
    def class_name(self, class_name: str):
        """
        Sets the class_name of this Object.

        :param class_name: The class_name of this Object.
        :type class_name: str
        """

        self._class_name = class_name

    @property
    def storage(self) -> str:
        """
        Gets the storage of this Object.

        :return: The storage of this Object.
        :rtype: str
        """
        return self._storage

    @storage.setter
    def storage(self, storage: str):
        """
        Sets the storage of this Object.

        :param storage: The storage of this Object.
        :type storage: str
        """

        self._storage = storage

    @property
    def bucket(self) -> str:
        """
        Gets the bucket of this Object.

        :return: The bucket of this Object.
        :rtype: str
        """
        return self._bucket

    @bucket.setter
    def bucket(self, bucket: str):
        """
        Sets the bucket of this Object.

        :param bucket: The bucket of this Object.
        :type bucket: str
        """

        self._bucket = bucket

    @property
    def color(self) -> int:
        """
        Gets the color of this Object.

        :return: The color of this Object.
        :rtype: int
        """
        return self._color

    @color.setter
    def color(self, color: int):
        """
        Sets the color of this Object.

        :param color: The color of this Object.
        :type color: int
        """

        self._color = color

    @property
    def texture(self) -> str:
        """
        Gets the texture of this Object.

        :return: The texture of this Object.
        :rtype: str
        """
        return self._texture

    @texture.setter
    def texture(self, texture: str):
        """
        Sets the texture of this Object.

        :param texture: The texture of this Object.
        :type texture: str
        """

        self._texture = texture

    @property
    def fabric(self) -> str:
        """
        Gets the fabric of this Object.

        :return: The fabric of this Object.
        :rtype: str
        """
        return self._fabric

    @fabric.setter
    def fabric(self, fabric: str):
        """
        Sets the fabric of this Object.

        :param fabric: The fabric of this Object.
        :type fabric: str
        """

        self._fabric = fabric

    @property
    def shape(self) -> str:
        """
        Gets the shape of this Object.

        :return: The shape of this Object.
        :rtype: str
        """
        return self._shape

    @shape.setter
    def shape(self, shape: str):
        """
        Sets the shape of this Object.

        :param shape: The shape of this Object.
        :type shape: str
        """

        self._shape = shape

    @property
    def part(self) -> str:
        """
        Gets the part of this Object.

        :return: The part of this Object.
        :rtype: str
        """
        return self._part

    @part.setter
    def part(self, part: str):
        """
        Sets the part of this Object.

        :param part: The part of this Object.
        :type part: str
        """

        self._part = part

    @property
    def style(self) -> str:
        """
        Gets the style of this Object.

        :return: The style of this Object.
        :rtype: str
        """
        return self._style

    @style.setter
    def style(self, style: str):
        """
        Sets the style of this Object.

        :param style: The style of this Object.
        :type style: str
        """

        self._style = style

