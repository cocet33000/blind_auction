from main.infrastructure.auction_repository_impl import AuctionRepositoryImpl


def test_正常系():
    auctions = AuctionRepositoryImpl.getAll()
