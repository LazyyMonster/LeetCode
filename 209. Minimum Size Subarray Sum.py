class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        subsum = 0
        L = 0
        res = float("inf")

        for R in range(len(nums)):
            subsum += nums[R]
            while subsum >= target:
                res = min(res, R - L + 1)
                subsum -= nums[L]
                L += 1
                
        return 0 if res > len(nums) else res