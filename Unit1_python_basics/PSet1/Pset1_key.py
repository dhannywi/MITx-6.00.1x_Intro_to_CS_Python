# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 15:30:46 2021

@author: Dhanny Indrakusuma
Problem set 1 - one-liner solutions
"""
#test string
s = 'azcbobobegghakl'

#exercise 1 answer
print(sum(c in 'aeiou' for c in s))

#exercise 2 answer
print(s.replace('b', 'bb').count('bob'))

#exercise 3 answer
print(max((''.join(j+' '*(i<j)for i,j in zip(s[1:]+s,s))).split(),key=len))

#ex3 option 2 (TA answer)
current = longest = s[0]
for e in s[1:] + ' ':
    if e < current[-1]:
        if len(current) > len(longest):
            longest = current
        current = ''
    current += e
print('Longest substring in alphabetical order is:', longest)

#ex3 option 3
y=s[0]
ans=""
for x in range(len(s)-1):
    if s[x+1]>=s[x]:
        y+=s[x+1]
    else:
        y=s[x+1]
    if len(y)>len(ans):
        ans=y
print("Longest substring in alphabetical order is: " + ans)

#ex3 - similar to mine
temp=""
long=""
for i in range(len(s)):
    if s[i-1]<=s[i]:
        temp += s[i]
        if len(temp)>len(long):
            long = temp           
    else:
        temp = s[i]
print('Longest substring in alphabetic order is:' + str(long))