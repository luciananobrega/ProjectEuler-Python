# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 23:24:58 2017

@author: Luciana
"""

"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

import time

start = time.time()


def prime(num):
    i = 2
    while i < num:
        if num%i == 0: # não é primo, passa para próximo num
            return False
        else:
            i+=1
    #print(i)
    return True

below = int(1000)
primeSum = 2

i = 3

while i<=below:
    #print(i/below)
    if prime(i):
        primeSum = primeSum + i
        print (i)
    i += 2
        
print(primeSum)

"""
below = 80000
primes = [2]
num = 3
sumPrimes = 2

while below>num:
    print(num/below)
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
        #sumPrimes = sumPrimes+num
        num+=2
        
print(sum(primes))
"""

end = time.time()
print(end - start)