allGuests = {
    'Alice': {'apples': 5, 'pretzels':'12'},
    'Bob': {'ham sandwiches': 3, 'apples': 2},
    'Carol': {'cups':3, 'apple pies': 1}
}

def totalBrought(Guests, item):
    numBrought = 0
    for k, v in Guests.items():
        numBrought = numBrought + v.get(item, 0)
    return numBrought

print('Number of things being brought: \n\n')
print('- Apples         ' + str(totalBrought(allGuests, 'apples')))
print('- Cups         ' + str(totalBrought(allGuests, 'cups')))