from main.infrastructure import ItemRepositoryImpl


def test_正常系():
    AUCTION_ID = 100
    ItemRepositoryImpl.getByAuctionId(auction_id=AUCTION_ID)
