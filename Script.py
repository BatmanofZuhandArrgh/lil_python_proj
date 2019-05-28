#!/usr/bin/env/ python3

#  Script.py
#  
#
#  Created by Macbook on 5/27/19.
#  
import pyperclip
text = pyperclip.paste()
pyperclip.copy(text)

#Separate line and add star
lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '*' + lines[i]

pyperclip.copy(text)
