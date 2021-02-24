# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 11:02:12 2021

@author: Dhanny Indrakusuma

Assume s is a string of lower case characters.

Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:

Number of vowels: 5

"""
#test value for s
s = 'jbvvuyweifcbwebgf'

#code works!
count = 0
for e in s:
    if e in 'aiueo':
        count += 1

print('Number of vowels: ' + str(count))


'''
Another version of solution:
    
count = 0
for e in s:
    if e == 'a' or e == 'i' or e == 'o' or e == 'u' or e == 'e':
        count +=1
        
print('Number of vowels:', count)
'''
