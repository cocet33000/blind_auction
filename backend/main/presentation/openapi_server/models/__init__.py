# coding: utf-8

# flake8: noqa
from __future__ import absolute_import

import sys
import os

# 2つ上の階層もパスに追加
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))

from openapi_server.models.bid_history_bid import BidHistoryBid
