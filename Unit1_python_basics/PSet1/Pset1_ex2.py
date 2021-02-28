# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 11:28:31 2021

@author: Dhanny Indrakusuma

Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2

"""
#test value for s
s = 'hjboobbobobobobbobob'

#code works!
count = 0
for e in range(len(s)):
    if s[e:e+3] == 'bob':
        count += 1

print('Number of times bob occurs is: ' + str(count))
