def printItems(items, leftWidth, rightWidth):
    print('Picnic Items'.center(leftWidth + rightWidth, '='))
    for k, v in items.items():
        print(f'{k.ljust(leftWidth, ".")}{str(v).rjust(rightWidth)}')

# Sample data
picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8}
printItems(picnicItems, 12, 5)
printItems(picnicItems, 20, 6)
