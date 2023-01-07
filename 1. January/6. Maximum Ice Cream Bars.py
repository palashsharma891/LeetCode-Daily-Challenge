class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        temp = 0
        ans = 0
        for i in costs:
            print(i)
            if i <= coins:
          
                ans += 1
                coins -= i
                
                print(ans, coins, i)
                
        return ans
