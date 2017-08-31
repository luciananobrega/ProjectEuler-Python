# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 16:18:44 2017

@author: Luciana
"""

"""
Largest palindrome product
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

import time

start = time.time()


#We want a number between 10000 and 998001

b=999 #biggest
s=100 #smallest

n=[]

flag=0
i=b*b

while i>=s*s and flag == 0:
    
    a=str(i)
    a=int(a[::-1])
    #checks if it is paliandromic
    if i-a!=0:
        i-=1
    else:
        #checks its products
        for j in range(s,b):
            if i/j < s or i/j > b or not j*int(i/j)==i:
                continue
            else:
                n.append(i)
                flag = 1
                break
        i-=1
        
print(n[0])

end = time.time()
print(end - start)
