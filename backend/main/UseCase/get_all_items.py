import json

from Infrastructure import ItemRepositoryImpl


def get_items() -> dict:
    items = ItemRepositoryImpl.getAll()
    return {"items": [item.to_dict() for item in items]}


if __name__ == "__main__":
    print(json.dumps(get_items()))
