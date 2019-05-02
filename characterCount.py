#program that counts the number of characters in a message 

import pprint

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message:
    count.setdefault(character, 0) #sets the default value as 0
    count[character] = count[character] + 1 #updating
pprint.pformat(count)


#PRETTY PRINT
# 1. import the pprint module
# 2. Substitute the print() function with pprint() function
# 3. Kind of like sorting, use the pformat() function for order
