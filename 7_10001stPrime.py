# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10,001st prime number?

import time
import math
start_time = time.time()

def isprime(num):
    if num> 1:  
        for n in range(2,num):  
            if (num % n) == 0:  
                return False
        return True
    else:
        return False

num = 2

PrimeCounter = 0
#PrimeCounterGoal = 6
PrimeCounterGoal = 10001

while True:
    result = isprime(num)

    if result:
        PrimeCounter += 1
        print(str(num) + ' is Prime # ' + str(PrimeCounter))

    num += 1

    if PrimeCounter == PrimeCounterGoal:
        break

# Answer = 104743
