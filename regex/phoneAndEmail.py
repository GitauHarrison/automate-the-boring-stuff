#! python3
#phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard


#Say you have the boring task of finding every phone number and email address in a long web page or document.

import pyperclip, re

phoneRegex = re.compile(r'''(
    (\d{3}|\(d{3}\))? #area code
    (\s|-|\.)? #separator
    (\d{3}) # first three digits
    (\s|-|\.) # separator
    (\d{4}) # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))? #extension  
)''', re.VERBOSE)

#TODO: Create email regex
emailRegex = re.compile(r'''(
    [a-zA-Z0-9_%+-]+ #username
    @ # @ symbol
    [a-zA-Z0-9.-]+ #domain name
    (\.[a-zA-Z]{2,4}) #dot-something
)''', re.VERBOSE)

#TODO: Find matches in clipboard
text = str(pyperclip.paste()) #contents on clipboard (ctrl+A)
matches = [] #save to empty list
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]]) #join hyphen to area code, first 3 digits, lst 4 digits and extension
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for email in emailRegex.findall(text):
    matches.append(groups[0]) #entire email regex


#TODO: Copy results to clipboard
if len (matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard: ')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')