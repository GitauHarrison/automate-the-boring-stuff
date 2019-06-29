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

##----------------
#Greedy (returns longest possible value)
# & 
# Nongreedy (returns shortest possible value)...add a ? after the curly braces
##----------------
nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo4 = nongreedyHaRegex.search('HaHaHaHaHaHaHaHa')
mo4.group()


##----------------
#findall() 
##----------------

#It returns all matched text as a list as long as there are no groups in the regex

myPhoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') #no groups
myPhoneNumRegex.findall('Cell:  415-555-9999 Work: 212-555-0000')

#findall() returns a tuple if it has groups
myPhoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)') #no groups
myPhoneNumRegex.findall('Cell:  415-555-9999 Work: 212-555-0000')

#More character classes
xmasRegex = re.compile(r'\d+\s\w+')
xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')


##-----------------------------------
#making your own character classes...use []
##------------------------------------
vowelRegex = re.compile(r'[aeiouAEIOU]')
vowelRegex.findall('Robocop eats baby food. BABY FOOD')


##------------------------------------
#Caret (^) character
# it makes a negative character class (all the characters that are not in the charater class)
##------------------------------------
consonantRegex = re.compile(r'[^aeiouAEIOU]')
consonantRegex.findall('Robocop eats baby food. BABY FOOD.')


##--------------------------------------
#Caret (^) and dollar sign ($)
# begin(^), end($)
##--------------------------------------
beginsWithHello = re.compile(r'^Hello ')
beginsWithHello.search('Hello world') == None # returns True

endsWithDigit = re.compile(r'\d$')
endsWithDigit.search('jddhk5453')== None # returns True

wholeStringIsNum = re.compile(r'\d+$')
wholeStringIsNum.search('12345xyz67890') == None #returns True


##-------------------------------------
# wildcard (.)
# matches anything excluding  a new line
##-------------------------------------
atRegex = re.compile(r'.at') 
mo8 = atRegex.search('The cat in the hat sat on the flat mat')
#it will match anything with the character combination (at)


##-------------------------------
# Wildcard (.) with new lines
#add re.DOTALL argument
##-------------------------------
newLineRegex = re.compile(r'.*', re.DOTALL)
newLineRegex.search('Serve the public interest.\nProtect the innocent. \nUphold the law.').group()


##------------------------
# Case Insensitive regex
#re.IGNORECASE (re.I)
##------------------------
robocop = re.compile(r'robocop', re.I)
robocop.search('ROBOCOP is part human, part machine, all cop.').group()

##--------------
#substituting strings with sub()
##
namesRegex = re.compile(r'Agent \w+')
namesRegex.sub('CENSORED', 'Agent Alice gave secret documents to Agent Bob')

#show only the first letter of their names
agentNamesREgex = re.compile(r'Agent (w)\w*')
agentNamesREgex.sub(r'1***', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.')



##---------------------
#Complex regex
#USE re.VERBOSE (multiline regex)
##---------------------
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))? #area code
    (\s|-|\.)? #separator
    \d{3} #first three digits
    (\s|-|.) #separator
    \d{4} #last four digits
    (\s*(ext|x|ext.)\s*\d{2,5})? #extension
    )''', re.VERBOSE)