#Power Digit Sum
#2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#What is the sum of the digits of the number 2^1000?

import time
start_time = time.time()

sum = 0
n = 2**1000
for digit in str(n):
    sum += int(digit)

print(sum)
print("\n--- %s seconds ---" % (time.time() - start_time))    

#Answer: 1366 

