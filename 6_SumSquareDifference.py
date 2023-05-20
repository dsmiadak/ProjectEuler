# The sum of the squares of the first ten natural numbers is 385
# The square of the sum of the first ten natural numbers is 3025
# The difference is 2640
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.


import time
import math
start_time = time.time()

#number = int(input('Enter number max: '))

i = 0
j = 0

for x in range(1,101):
   i = i + (x * x)

print(i)

for y in range(1,101):
    j = 1 + (j + (y-1))
    print(str(j) + ', ' + str(y))
    
j = j*j
print(j)

print('Difference = ' + str(j-i))
# Answer = 25164150
