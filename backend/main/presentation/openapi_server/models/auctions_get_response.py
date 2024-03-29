# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.auction import Auction
from openapi_server import util

from openapi_server.models.auction import Auction  # noqa: E501

class AuctionsGetResponse(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, has_next=None, auctions=None):  # noqa: E501
        """AuctionsGetResponse - a model defined in OpenAPI

        :param has_next: The has_next of this AuctionsGetResponse.  # noqa: E501
        :type has_next: bool
        :param auctions: The auctions of this AuctionsGetResponse.  # noqa: E501
        :type auctions: List[Auction]
        """
        self.openapi_types = {
            'has_next': bool,
            'auctions': List[Auction]
        }

        self.attribute_map = {
            'has_next': 'has_next',
            'auctions': 'auctions'
        }

        self._has_next = has_next
        self._auctions = auctions

    @classmethod
    def from_dict(cls, dikt) -> 'AuctionsGetResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The auctions_get_response of this AuctionsGetResponse.  # noqa: E501
        :rtype: AuctionsGetResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def has_next(self):
        """Gets the has_next of this AuctionsGetResponse.


        :return: The has_next of this AuctionsGetResponse.
        :rtype: bool
        """
        return self._has_next

    @has_next.setter
    def has_next(self, has_next):
        """Sets the has_next of this AuctionsGetResponse.


        :param has_next: The has_next of this AuctionsGetResponse.
        :type has_next: bool
        """

        self._has_next = has_next

    @property
    def auctions(self):
        """Gets the auctions of this AuctionsGetResponse.


        :return: The auctions of this AuctionsGetResponse.
        :rtype: List[Auction]
        """
        return self._auctions

    @auctions.setter
    def auctions(self, auctions):
        """Sets the auctions of this AuctionsGetResponse.


        :param auctions: The auctions of this AuctionsGetResponse.
        :type auctions: List[Auction]
        """

        self._auctions = auctions
