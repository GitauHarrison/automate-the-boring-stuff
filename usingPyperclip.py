'''
Note: pyperclip does not come preinstalled with Python.

How to install the pyperclip module:

1.     sudo apt update

2.     sudo apt install python3-pyperclip


'''

import pyperclip

pyperclip.copy('Hello World')
print(pyperclip.paste())