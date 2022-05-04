import json

from Repository.ItemRepository import ItemRepository


def get_items():
    items = ItemRepository.getAll()
    return {"items": [item.to_model().to_dict() for item in items]}


if __name__ == "__main__":
    print(json.dumps(get_items()))
