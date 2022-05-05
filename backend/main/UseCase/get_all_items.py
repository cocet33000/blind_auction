import json

from Repository import ItemRepository


def get_items() -> dict:
    items = ItemRepository.getAll()
    return {"items": [item.to_model().to_dict() for item in items]}


if __name__ == "__main__":
    print(json.dumps(get_items()))
