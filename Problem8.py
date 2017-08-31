# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 22:37:18 2017

@author: Luciana
"""

"""
Largest product in a series

The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832.

Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?
"""

#Reading the file
l=open('Problem81.txt')
a=l.read()
a=a.split('\n')

num = []

# splitting the string
for i in range(0,20):
    num = num + list(a[i])

#Getting the greatest number
biggestNumber = 0
digits = 13

for i in range(0,len(num)-digits):
    candidateBiggest = 1
    for j in range(0,digits):
        candidateBiggest = int(num[i+j])  * candidateBiggest
    if candidateBiggest > biggestNumber:
        biggestNumber = candidateBiggest