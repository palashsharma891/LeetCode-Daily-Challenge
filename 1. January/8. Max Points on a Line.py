class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        
        if len(points) <= 2:
            return len(points)

        def slope(p1, p2):
            if p1[0] == p2[0]: #vertical line
                return inf
            return (p1[1] - p2[1]) / (p1[0] - p2[0])

        res = 0
        for i in range(len(points)):
            count = defaultdict(int)
            for j in range(i+1, len(points)):
                count[slope(points[i], points[j])] += 1
            if count:
                res = max(res, max(count.values()))

        return res + 1

        '''

        ans = 0
        (x0, y0), (x1, y1) = points[0], points[1]
        for i in range(2, len(points)):
            x, y = points[i]
            print(x0,y0,x1,y1,x,y)
            print((x0 - x1) * (y1 - y))
            if abs((x0 - x1) * (y1 - y)) == abs((x1 - x) * (y0 - y1)):
                ans += 1
        return ans'''
