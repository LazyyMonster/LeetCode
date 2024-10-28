class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        maxLen = 1

        distinctNums = set(nums)
        start = 0
        end = 0
        for n in distinctNums:
            streak = 1
            num = n * n
            while num in distinctNums:
                streak += 1
                if streak > maxLen:
                    maxLen = streak
                    start = n
                    end = num
                num *= num   

        if start == end:
            return -1

        res = 1
        n = start
        while n < end:
            res += 1
            n *= n

        return res