# Using regex functions

import re

#return a regex object
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

#search for a regex in a string using the search() method
mo = phoneNumRegex.search('My number is 435-555-4242') 

#return matched object using group() method
print('Phone number found: ' + mo.group())