# The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832.
# Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?

import time
import math
start_time = time.time()

num = '73167176531330624919225119674426574742355349194934'\
      '96983520312774506326239578318016984801869478851843'\
      '85861560789112949495459501737958331952853208805511'\
      '12540698747158523863050715693290963295227443043557'\
      '66896648950445244523161731856403098711121722383113'\
      '62229893423380308135336276614282806444486645238749'\
      '30358907296290491560440772390713810515859307960866'\
      '70172427121883998797908792274921901699720888093776'\
      '65727333001053367881220235421809751254540594752243'\
      '52584907711670556013604839586446706324415722155397'\
      '53697817977846174064955149290862569321978468622482'\
      '83972241375657056057490261407972968652414535100474'\
      '82166370484403199890008895243450658541227588666881'\
      '16427171479924442928230863465674813919123162824586'\
      '17866458359124566529476545682848912883142607690042'\
      '24219022671055626321111109370544217506941658960408'\
      '07198403850962455444362981230987879927244284909188'\
      '84580156166097919133875499200524063689912560717606'\
      '05886116467109405077541002256983155200055935729725'\
      '71636269561882670428252483600823257530420752963450'

digits = [int(x) for x in str(num)]
MaxProduct = 0

##for i in range (0,996):
##    Product = int(digits[i]) * int(digits[i+1]) * int(digits[i+2]) * int(digits[i+3])
##
##    if Product > MaxProduct:
##        Max1 = digits[i]
##        Max2 = digits[i+1]
##        Max3 = digits[i+2]
##        Max4 = digits[i+3]
##        MaxProduct = Product
##        
##print(str(Max1) + ' x ' + str(Max2) + ' x ' + str(Max3) + ' x ' + str(Max4) + ' = ' + str(MaxProduct))

for i in range (0,987):
    Product = int(digits[i]) * int(digits[i+1]) * int(digits[i+2]) * int(digits[i+3]) \
              * int(digits[i+4]) * int(digits[i+5]) * int(digits[i+6]) * int(digits[i+7]) \
              * int(digits[i+8]) * int(digits[i+9]) * int(digits[i+10]) * int(digits[i+11]) \
              * int(digits[i+12])

    if Product > MaxProduct:
        MaxProduct = Product
        
print(str(MaxProduct))
print("\n--- %s seconds ---" % (time.time() - start_time))
# Better solution
##temp, result = 1, 0
##num_list = list(map(int, num))
##for i in range(1000-12):
##    for j in num_list[i:13+i]:
##        temp *= j
##    result = temp if temp > result else result
##    temp = 1
##print(result)

#Answer = 23514624000

