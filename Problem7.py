# -*- codipng: utf-8 -*-
"""
Created on Tue Jul  4 18:44:51 2017

@author: Luciana
"""

"""
10001st prime

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

import time

start = time.time()


order = 1000

primes = [2]
num = 3

while order>len(primes):
    per=len(primes)/order
    #print('%1.4f of the simulation already done' %per)
    flag = True
    i = 2
    
    while i<num and flag:
        if num%i != 0: # não é divisível, talvez seja primo
            i += 1
        else: # é divisível, e não é primo. Pular para o próximo num
            num += 2
            flag = False
    
    if flag:
        primes.append(num)
        num+=2
        
print(primes[-1])


end = time.time()
print(end - start)