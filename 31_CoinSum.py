class Solution:
    def solve(self, coins, amount):
        # Generate an array of amount + 1 items
        dp = [0] * (amount + 1)
          #print(dp)
        dp[0] = 1
        # For loop can execute a set of statements, once for each item in a list
        for d in coins:
            for i in range(1, len(dp)):
##                print('i =' + str(i))
##                print('d =' + str(d))
                if i - d >= 0:
                    print(dp[i-d])
                    dp[i] += dp[i - d]
        return dp[-1] % (10 ** 9 + 7)
ob = Solution()
coins = [1, 2, 5, 10, 20, 50, 100, 200]
#coins = [2, 5]
amount = 200
#amount = 10
print(ob.solve(coins, amount))
