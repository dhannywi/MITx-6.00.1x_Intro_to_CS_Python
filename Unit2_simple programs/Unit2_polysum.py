# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 20:24:54 2021

@author: Dhanny Indrakusuma

Unit 2 Additional exercise
Complete Programming Experience: polysum

A regular polygon has n number of sides. Each side has length s.

The area of a regular polygon is:  (0.25∗n∗s**2)/(tan(π/n)) 
The perimeter of a polygon is: length of the boundary of the polygon
Write a function called polysum that takes 2 arguments, n and s.
This function should sum the area and square of the perimeter of the regular polygon. The function returns the sum, rounded to 4 decimal places.
"""

import math

def polysum (n, s):
    if n < 3:
        print('Not a valid number of sides for a regular polygon, please re-enter')
        
    else:
        area = (0.25*n*(s**2))/math.tan(math.pi/n)
        perimeter = n*s
        return round((area + perimeter**2), 4)

n = int(input('Enter number of sides: '))
s = float(input('Enter length of each side: '))

print('The polysum is', polysum(n, s))