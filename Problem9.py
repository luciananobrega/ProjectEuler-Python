# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 23:11:49 2017

@author: Luciana
"""
"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

for a in range(1,400):
    for b in range(1,400):
        c2 = a**2 + b**2
        c = int(c2 ** 0.5)
        if c2 == (c ** 2):
            if a+b+c==1000:
                print(a,b,c,a+b+c)
                print(a*b*c)