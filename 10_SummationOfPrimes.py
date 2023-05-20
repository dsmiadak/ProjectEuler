##Problem 10 (https://projecteuler.net/problem=10)
##The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
##Find the sum of all the primes below two million.

import time
import math
start_time = time.time()

num = 2
PrimeSum = 0

def isprime(num):
    for n in range(2,int(num**0.5)+1):
        if num%n==0:
            return False
    return True

for h in range(2,2000000):
    result = isprime(h)

    if result:
        #print(h, " is a prime number")
        PrimeSum = PrimeSum + h
        h += 1
    else:
        h += 1
print(PrimeSum, " is the prime sum")

print("\n--- %s seconds ---" % (time.time() - start_time))
#Answer = 142,913,828,922
          
    
