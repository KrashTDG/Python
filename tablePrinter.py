tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(table):
    
    col_width = [max(len(item) for item in col) for col in table] # finds out the width of the columns
    for col_index in range(len(table[0])):
        for row_index, row in enumerate(table):
            print(row[col_index].rjust(col_width[row_index]), end=' ')
        print()

        

        
printTable(tableData)