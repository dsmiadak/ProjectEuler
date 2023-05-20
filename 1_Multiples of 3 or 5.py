##Problem 1 (https://projecteuler.net/problem=1)
##If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
##Find the sum of all the multiples of 3 or 5 below 1000.



import time
start_time = time.time()

def multipler(r1,r2):

    Value = r1
    Matches = 0
    ValueSum = 0
    Flag = 0
##    List = list(mults)
    for i in range(r1,r2):
        if Value % 3 == 0:
            Matches += 1
            print(str(Value) + ' is a multiple of 3')
            ValueSum = ValueSum + Value
            Flag = 1

        if Value % 5 == 0 and Flag == 0:
            Matches += 1
            print(str(Value) + ' is a multiple of 5')
            ValueSum = ValueSum + Value

        #else:
            #print('Not a multiple: ' + str(Value))
        Value += 1
        Flag = 0
        
    return ValueSum

r1 = int(input('Enter min of range (inclusive): '))
r2 = int(input('Enter max of range (exclusive): '))
##mults = [3,5] 

print(multipler(r1,r2))

##file1 = open("CollatzConjecture.txt", "w")
##file1.writelines("Step,N")
##file1.write('\n')
##file1.writelines("0," + str(n))
##file1.write('\n')
##file1.close()
##print('Collatz Sequence: ', end='')
##TotalSteps, MaxValue = collatz(n)
##print('\nSteps -> 1: ' + str(TotalSteps) + '; Maximum = ' + str(MaxValue))
# Need total steps, Max value

#Answer = 233168

print("\n--- %s seconds ---" % (time.time() - start_time))    

