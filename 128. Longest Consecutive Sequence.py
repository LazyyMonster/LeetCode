class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        distinctNumbers = set(nums)
        maxLen = 0

        for n in nums:
            if n - 1 in distinctNumbers:
                continue

            i = 1
            while n + i in distinctNumbers:
                i += 1
            
            if i > maxLen:
                maxLen = i

        return maxLen