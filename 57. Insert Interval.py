class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i, interval in enumerate(intervals):
            si, ei = interval

            if newInterval[1] < si:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > ei:
                res.append([si, ei])
            else:
                newInterval = [min(newInterval[0], si), max(newInterval[1], ei)]

        res.append(newInterval)

        return res