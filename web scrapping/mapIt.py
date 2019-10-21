#! python3
# mapIt.py - Launches a map in the browser using an address from the 
# command line or clipboard

import webbrowser, sys, pyperclip
if len(sys.argv) > 1:
    # get address from the command line.
    address = ' '.join(sys.argv[1:])
else:
    #get address from the clipboard
    address = pyperclip.paste()

webbrowser.open('http://www.google.com/map/place/' + address)
webbrowser.open('http://wwww.learnenough.com/command-line-tutorial/basics' + address)
webbrowser.open('https://medium.com/@thedancercodes/our-watch-has-ended-the-converge-journey-750e980b4db0' + address)
