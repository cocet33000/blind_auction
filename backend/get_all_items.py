from Model.Item import Item

if __name__ == "__main__":
    scaned = Item.scan()
    for _item in scaned:
        print(_item.id, _item.name)
