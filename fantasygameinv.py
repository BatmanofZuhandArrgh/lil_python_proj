inv = {'gold coin' : 42, 'rope': 1}

def displayInventory(inv):
    print('stuff: ')
    totalitem = 0
    for k,v in inv.items():
        print(str(v) + ' ' + str(k))
        totalitem += v
    print("Total number of items: " + str(totalitem))

def addToInventory(inventory, addedItems):
    for i in addedItems:
        #if i in inventory.keys():
        inventory.setdefault(i, 0)
        inventory[i] = inventory[i] + 1

    return inventory

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
