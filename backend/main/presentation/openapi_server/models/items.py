# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.item import Item
from openapi_server import util

from openapi_server.models.item import Item  # noqa: E501

class Items(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, has_next=None, items=None):  # noqa: E501
        """Items - a model defined in OpenAPI

        :param has_next: The has_next of this Items.  # noqa: E501
        :type has_next: bool
        :param items: The items of this Items.  # noqa: E501
        :type items: List[Item]
        """
        self.openapi_types = {
            'has_next': bool,
            'items': List[Item]
        }

        self.attribute_map = {
            'has_next': 'has_next',
            'items': 'items'
        }

        self._has_next = has_next
        self._items = items

    @classmethod
    def from_dict(cls, dikt) -> 'Items':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The items of this Items.  # noqa: E501
        :rtype: Items
        """
        return util.deserialize_model(dikt, cls)

    @property
    def has_next(self):
        """Gets the has_next of this Items.


        :return: The has_next of this Items.
        :rtype: bool
        """
        return self._has_next

    @has_next.setter
    def has_next(self, has_next):
        """Sets the has_next of this Items.


        :param has_next: The has_next of this Items.
        :type has_next: bool
        """

        self._has_next = has_next

    @property
    def items(self):
        """Gets the items of this Items.


        :return: The items of this Items.
        :rtype: List[Item]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this Items.


        :param items: The items of this Items.
        :type items: List[Item]
        """

        self._items = items