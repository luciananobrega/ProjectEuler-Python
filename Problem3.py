# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 11:57:49 2017

@author: Luciana
"""
"""
# Largest prime factor
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

number = 600851475143
factors = []


i = 2
while i < number:
    if number % i != 0:
        i += 1
    else:
        number = number/i
print(number)

        
"""
# Code for small numbers (it takes a looong time to run)

for i in range(1,number):
    print('%1.0f of %1.0f done' %(i, number))
    check = []
    if number%i==0: # i is a factor of the number
        # Discover if this factor is a prime number
        for j in range(1,i+1):
            if i%j == 0:
                check.append(j)
        if sum(check)==i+1: #i is a prime number
            factors.append(i)
"""