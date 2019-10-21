#! python3
# multipleTabs.py - uses the webbrowser module to open multiple tabs on browser
# instead of multiple windows

import webbrowser, sys, pyperclip

def main():
    # first, open a new window
    webbrowser.open_new('https://medium.com/@thedancercodes/our-watch-has-ended-the-converge-journey-750e980b4db0')
    print('Openning a dev article on Medium')

    # then, open a new tab on the opened window
    webbrowser.open_new_tab('https://www.learnenough.com/command-line-tutorial/basics')
    print('Opening a new tab on the default browser!')

#main()
if __name__ == '__main__':
    main()