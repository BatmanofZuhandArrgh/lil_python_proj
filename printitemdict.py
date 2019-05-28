stuff = {'rope' : 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def printdict(stuff):
    print('stuff: ')
    totalitem = 0
    for k,v in stuff.items():
        print(str(v) + ' ' + str(k))
        totalitem += v
    print("Total number of items: " + str(totalitem))

printdict(stuff)
