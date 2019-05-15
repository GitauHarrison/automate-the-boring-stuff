#(shebang)


#!python3 
# pw.py - An insecure password locker program.

passwords = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6', 
            'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
            'luggage': '12345'
}

import sys, pyperclip

if len(sys.argv)<2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1] # first command line arg is the account name

#check if account name exists in the dictionary
if account in passwords: 
    pyperclip.copy(passwords[account])
    print('Passwords for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)