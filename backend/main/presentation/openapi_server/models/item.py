# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class Item(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, name=None, image_src=None, description=None, start_price=None, bid_num=None):  # noqa: E501
        """Item - a model defined in OpenAPI

        :param id: The id of this Item.  # noqa: E501
        :type id: int
        :param name: The name of this Item.  # noqa: E501
        :type name: str
        :param image_src: The image_src of this Item.  # noqa: E501
        :type image_src: str
        :param description: The description of this Item.  # noqa: E501
        :type description: str
        :param start_price: The start_price of this Item.  # noqa: E501
        :type start_price: int
        :param bid_num: The bid_num of this Item.  # noqa: E501
        :type bid_num: int
        """
        self.openapi_types = {
            'id': int,
            'name': str,
            'image_src': str,
            'description': str,
            'start_price': int,
            'bid_num': int
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'image_src': 'image_src',
            'description': 'description',
            'start_price': 'start_price',
            'bid_num': 'bid_num'
        }

        self._id = id
        self._name = name
        self._image_src = image_src
        self._description = description
        self._start_price = start_price
        self._bid_num = bid_num

    @classmethod
    def from_dict(cls, dikt) -> 'Item':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The item of this Item.  # noqa: E501
        :rtype: Item
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this Item.


        :return: The id of this Item.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Item.


        :param id: The id of this Item.
        :type id: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Item.


        :return: The name of this Item.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Item.


        :param name: The name of this Item.
        :type name: str
        """

        self._name = name

    @property
    def image_src(self):
        """Gets the image_src of this Item.


        :return: The image_src of this Item.
        :rtype: str
        """
        return self._image_src

    @image_src.setter
    def image_src(self, image_src):
        """Sets the image_src of this Item.


        :param image_src: The image_src of this Item.
        :type image_src: str
        """

        self._image_src = image_src

    @property
    def description(self):
        """Gets the description of this Item.


        :return: The description of this Item.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Item.


        :param description: The description of this Item.
        :type description: str
        """

        self._description = description

    @property
    def start_price(self):
        """Gets the start_price of this Item.


        :return: The start_price of this Item.
        :rtype: int
        """
        return self._start_price

    @start_price.setter
    def start_price(self, start_price):
        """Sets the start_price of this Item.


        :param start_price: The start_price of this Item.
        :type start_price: int
        """

        self._start_price = start_price

    @property
    def bid_num(self):
        """Gets the bid_num of this Item.


        :return: The bid_num of this Item.
        :rtype: int
        """
        return self._bid_num

    @bid_num.setter
    def bid_num(self, bid_num):
        """Sets the bid_num of this Item.


        :param bid_num: The bid_num of this Item.
        :type bid_num: int
        """

        self._bid_num = bid_num
