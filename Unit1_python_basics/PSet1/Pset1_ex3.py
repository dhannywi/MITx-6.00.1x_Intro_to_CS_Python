# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 11:42:06 2021

@author: Dhanny Indrakusuma
Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh
In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc
"""
# test value for s
s = 'azcbobobegghakl'

# finding longest substring in alphabetical order
temp = ""
longest = ""
for i in range(len(s)):
    if s[i-1] <= s[i]:
        temp = temp+s[i]
        if len(temp) > len(longest):
            longest = temp           
    else:
        temp=s[i]
print('Longest substring in alphabetic order is:' + str(longest))