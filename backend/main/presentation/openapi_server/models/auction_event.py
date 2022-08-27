# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class AuctionEvent(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, name=None, status=None):  # noqa: E501
        """AuctionEvent - a model defined in OpenAPI

        :param id: The id of this AuctionEvent.  # noqa: E501
        :type id: str
        :param name: The name of this AuctionEvent.  # noqa: E501
        :type name: str
        :param status: The status of this AuctionEvent.  # noqa: E501
        :type status: str
        """
        self.openapi_types = {
            'id': str,
            'name': str,
            'status': str
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'status': 'status'
        }

        self._id = id
        self._name = name
        self._status = status

    @classmethod
    def from_dict(cls, dikt) -> 'AuctionEvent':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The auction_event of this AuctionEvent.  # noqa: E501
        :rtype: AuctionEvent
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this AuctionEvent.


        :return: The id of this AuctionEvent.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AuctionEvent.


        :param id: The id of this AuctionEvent.
        :type id: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this AuctionEvent.


        :return: The name of this AuctionEvent.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AuctionEvent.


        :param name: The name of this AuctionEvent.
        :type name: str
        """

        self._name = name

    @property
    def status(self):
        """Gets the status of this AuctionEvent.


        :return: The status of this AuctionEvent.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this AuctionEvent.


        :param status: The status of this AuctionEvent.
        :type status: str
        """

        self._status = status
