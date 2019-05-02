stuff = {
    'arrow': 12, 'gold coin': 42, 'rope': 1, 'torch': 6,'dagger': 1
}

def displayInventory(inventory):
    print('Inventory: ')
    item_total = 0
    for k, v in stuff.items():
        print(k , v)
        item_total = item_total + stuff.get(k, 0)
    print("Total Number of items:" + str(item_total))
displayInventory(stuff)