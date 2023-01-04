class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        d = Counter(tasks)
        ans = 0
        for v in d.values():
            if v == 1:
                return -1
            ans += ceil(v / 3)

        return ans
      
'''or
class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        d = Counter(tasks)
            
        print(d)
        ans = 0
        for v in d.values():
            if v == 1:
                return -1
            
            if v % 3 == 0:
                ans += v // 3
            elif (v - 4) % 3 == 0:
                ans += ((v - 4) // 3) + 2
            elif (v - 2) % 3 == 0:
                ans += ((v - 2) // 3) + 1
            elif v % 2 == 0: #this check should be done at last since we should first try to divide by 3
                ans += v // 2

        return ans
