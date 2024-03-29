# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.bid_history_bid import BidHistoryBid
from openapi_server.models.bid_history_item import BidHistoryItem
from openapi_server import util

from openapi_server.models.bid_history_bid import BidHistoryBid  # noqa: E501
from openapi_server.models.bid_history_item import BidHistoryItem  # noqa: E501

class BidHistory(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, item=None, bid=None):  # noqa: E501
        """BidHistory - a model defined in OpenAPI

        :param item: The item of this BidHistory.  # noqa: E501
        :type item: BidHistoryItem
        :param bid: The bid of this BidHistory.  # noqa: E501
        :type bid: BidHistoryBid
        """
        self.openapi_types = {
            'item': BidHistoryItem,
            'bid': BidHistoryBid
        }

        self.attribute_map = {
            'item': 'item',
            'bid': 'bid'
        }

        self._item = item
        self._bid = bid

    @classmethod
    def from_dict(cls, dikt) -> 'BidHistory':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The bid_history of this BidHistory.  # noqa: E501
        :rtype: BidHistory
        """
        return util.deserialize_model(dikt, cls)

    @property
    def item(self):
        """Gets the item of this BidHistory.


        :return: The item of this BidHistory.
        :rtype: BidHistoryItem
        """
        return self._item

    @item.setter
    def item(self, item):
        """Sets the item of this BidHistory.


        :param item: The item of this BidHistory.
        :type item: BidHistoryItem
        """

        self._item = item

    @property
    def bid(self):
        """Gets the bid of this BidHistory.


        :return: The bid of this BidHistory.
        :rtype: BidHistoryBid
        """
        return self._bid

    @bid.setter
    def bid(self, bid):
        """Sets the bid of this BidHistory.


        :param bid: The bid of this BidHistory.
        :type bid: BidHistoryBid
        """

        self._bid = bid
