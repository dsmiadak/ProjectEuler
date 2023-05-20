##Problem 3 (https://projecteuler.net/problem=3)
## The prime factors of 13195 are 5, 7, 13 and 29.
##What is the largest prime factor of the number 600851475143 ?

import time
import math
start_time = time.time()

number = int(input('Enter number: '))
#number = 600851475143
TopRange = int(math.sqrt(number) + 1)
#print(str(TopRange))

##if number % 2 == 0:
##    print('2')
##
##else: #number must be odd
for x in range(2, TopRange):
    if number % x == 0:
        print(str(x) + ' is a prime factor')
        number = number / x
    x += 2

#NOTE: These are the prime factors, not the prime factorization tree.
#number = 600851475143
#answer = 6857
