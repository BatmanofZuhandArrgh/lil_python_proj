#! /usr/bin/env python3
PASSWORD = {'email'  : 'Bf3jr3hnjnfejnfjwnejr',
            'blog'   : 'NJvneuqnrunnon3e2NJNC',
            'luggage': 'jdowdnefjewnfjnfjln4n'}
import sys, pyperclip
if len(sys.argv) < 2:
    print("something something something")
    sys.exit()

account = sys.argv[1]

if account in PASSWORD:
    pyperclip.copy(PASSWORD[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)

