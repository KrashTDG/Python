def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in sorted(inventory.items()):
        print(str(v) + ' ' + k)
        item_total += v
    print("Total number of items: " + str(item_total))

def addToInv(inv, addedItems):
    for items in addedItems:
        inv.setdefault(items,0)
        inv[items] += 1
        

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
addToInv(inv,dragonLoot)
displayInventory(inv)