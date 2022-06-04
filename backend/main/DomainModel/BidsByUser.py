class BidsByUser(list):
    _bids = []

    def __init__(self, bids):
        self._bids = bids

    def exists_bid_by_item_id(self, item_id: int) -> bool:
        for bid_by_user in self._bids:
            if bid_by_user.bid_item_id == item_id:
                return True

        return False
