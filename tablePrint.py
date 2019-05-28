tableData = [['apples', 'oranges', 'cherries', 'bananas'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
def printTable(tableData):
    for i in range(4):
        for j in range(3):
            print(tableData[j][i].rjust(10), end = " ")
        print('\n')
printTable(tableData)
