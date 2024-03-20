# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 16:55:01 2024

@author: Geektron
"""

str = "X-DSPAM-Confidence: 0.8475"
str.strip()
print(str)

colonPos = str.find(':')

numberExract = str[colonPos+1:]
numberExract = float(numberExract)

print(numberExract)