from Repository.ItemRepository import ItemRepository

if __name__ == "__main__":
    item_repository = ItemRepository()
    item_repository.deleteByItemId("68")
