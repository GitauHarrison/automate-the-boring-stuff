# Using regex functions

import re

#return a regex object
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

#search for a regex in a string using the search() method
mo = phoneNumRegex.search('My number is 435-555-4242') 

#return matched object using group() method
print('Phone number found: ' + mo.group())


##-----------------
# Using a | (pipe)
##-----------------

heroRegex = re.compile(r'Batman | Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey')
mo1.group() #returns the first occurance of the matching text

#Multiple prefixes
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo2 = batRegex.search('Batmobile lost a wheel')
mo2.group() #returns Batman

##-------------------------
#Optional group using ? (Zero or 1 match)
##-------------------------
myBatRegex = re.compile(r'Bat(wo)?man')
mo3 = myBatRegex.search('The adventures of Batman')
mo3.group() #returns Batman... (wo) group was optional