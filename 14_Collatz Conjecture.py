#Collatz Conjecture

import time
start_time = time.time()

def collatz(n):
    TotalSteps = 0
    MaxValue = n
    while n > 1:
        if (n % 2):
            # n is odd
            n = 3*n + 1
            TotalSteps += 1
            if n > MaxValue:
                MaxValue = n
        else:
            # n is even
            n = n//2
            TotalSteps += 1
            if n > MaxValue:
                MaxValue = n
    return TotalSteps,MaxValue

n = 0
TotalStepMax = 0
MaxNumber = 0

while n < 1000000:
    TotalSteps, MaxValue = collatz(n)
    #print(str(n) + ' is ' + str(TotalSteps) + ' steps!')
    if TotalSteps > TotalStepMax:
        TotalStepMax = TotalSteps
        MaxNumber = n
        print('New Max! Found at ' + str(n) + ' with ' + str(TotalStepMax) + ' steps!')
    n += 1
print("\n--- %s seconds ---" % (time.time() - start_time))    

#Answer: 837799 at 524 steps
