# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 17:18:06 2017

@author: Luciana
"""

"""
Smallest multiple

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

import time

start = time.time()

num = 2520

i=19

while i>=11:
    if num%i==0:
        i-=1
    else:
        i=19
        num+=2520
print(num)

end = time.time()
print(end - start)