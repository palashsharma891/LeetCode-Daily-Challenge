class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # sort start
        points.sort()
        currStart = points[-1][0]
        ans = 1
        for start, end in points[::-1]:
            if end < currStart:
                currStart = start
                ans += 1

        return ans
        
        ''' 
        # sort end
        points.sort(key=lambda x:x[1])
        currEnd = points[0][1]
        ans = 1
        for start, end in points:
            if start > currEnd:
                currEnd = end
                ans += 1

        return ans
        '''
