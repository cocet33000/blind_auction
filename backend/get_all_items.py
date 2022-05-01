from Repository.ItemRepository import ItemRepository

if __name__ == "__main__":
    item_repository = ItemRepository()
    items = item_repository.getAll()
    for item in items:
        print(item.convert_to(), item.id)
