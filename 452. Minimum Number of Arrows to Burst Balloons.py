class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        points.sort(key= lambda point: point[0])
        res = [points[0]]

        for start, end in points:
            if start <= res[-1][1]:
                res[-1][1] = min(end, res[-1][1])
            else:
                res.append(start, end)
        return len(res)