#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#a^2 + b^2 = c^2
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

import time
import math
start_time = time.time()

for b in range(1000):
    for a in range(1, b):
        c = math.sqrt(a**2+b**2)
        if c % 1 == 0:
            #print(str(a) + ', ' + str(b) + ', ' + str(c))
            #c = int(c)
            if a + b + c == 1000:
                Product = a*b*c
                print(str(a) + ', ' + str(b) + ', ' + str(c) + '= 1000!')
                print('Product = ' + str(Product))
                break
print("\n--- %s seconds ---" % (time.time() - start_time))
#Answer = 31875000
