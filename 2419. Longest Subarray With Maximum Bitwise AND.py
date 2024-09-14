class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        maximum = nums[0]
        res = 0
        actual = 0

        for n in nums:
            if n > maximum:
                res = 1
                actual = 1
                maximum = n
            elif n == maximum:
                actual += 1
                res = max(res, actual)
            else:
                actual = 0
                
        return res