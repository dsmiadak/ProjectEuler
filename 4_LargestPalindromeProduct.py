#A palindromic number reads the same both ways.
#The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.

import time
import math
start_time = time.time()

First = 100
Second = 100
Max = 0
Max1 = 0
Max2 = 0

for y in range(100,1000):
    Second = 100  
    for x in range(100,1000):
        Sum = First * Second
        #print(str(First) + '*' + str(Second))
        SumString = str(Sum)
        SumReversed = ''.join(reversed(SumString))
        if SumString == SumReversed:
            print(SumString + ' is a palindromic number' + str(First) + '*' + str(Second))
            if Sum > Max:
                Max = Sum
                Max1 = First
                Max2 = Second
        x += 1
        Second += 1
    y += 1
    First += 1

print('Largest Palindrome: ' + str(Max) + '. From: ' + str(Max1) + '*' + str(Max2))
print("\n--- %s seconds ---" % (time.time() - start_time))    

#Answer = 906609
