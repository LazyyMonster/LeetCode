class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key= lambda interval: interval[0])
        res = [intervals[0]]

        for s, e in intervals:
            prev_end = res[-1][1]
            
            if prev_end >= s:
                res[-1][1] = max(e, prev_end)
            else:
                res.append([s, e])

        return res