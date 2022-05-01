from Model.Item import Item

if __name__ == "__main__":
    item = Item("2")
    item.update(actions=[
        Item.name.set("piyo")
    ])
