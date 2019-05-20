#!python3
# bullentPointAdder.py - Adds wikipedia bullet points to the start
# to the start of each line

import pyperclip

text = pyperclip.paste()

# TODO: Separate line and add stars

lines = text.split('\n')
for i  in range (len(lines)): #loop through the indeces for 'lines' list
    lines[i] = '* ' + lines[i] # add star to each string in 'lines' list

text = '\n'.join(lines)

print(pyperclip.copy(text))
