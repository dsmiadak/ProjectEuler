#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


import time
import math
start_time = time.time()

Start = 2520

while True:
    print(str(Start))
    if Start % 20 == 0:
        if Start % 19 == 0:
            if Start % 18 == 0:
                if Start % 17 == 0:
                    if Start % 16 == 0:
                        if Start % 15 == 0:
                            if Start % 14 == 0:
                                if Start % 13 == 0:
                                    if Start % 12 == 0:
                                        if Start % 11 == 0:
                                            print('Answer = ' + str(Start))
                                            break
    Start += 2520
# Answer = 232,792,560

##while not x:
##    for i in range(2,11):
##        print(str(Start) + '|' + str(i))
##        if Start % i == 0:
##            print(str(Start) + ' is divisible by: ' + str(i))
##            if i == 10:
##                x = True
##        else:
##            break 


