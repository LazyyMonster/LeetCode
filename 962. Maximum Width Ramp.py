class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        res = 0
        stack = []

        for i in range(len(nums)):
            if not stack or nums[i] < nums[stack[-1]]:
                stack.append(i)

        for R in range(len(nums) - 1, -1, -1):
            while stack and nums[R] >= nums[stack[-1]]:
                res = max(res, R - stack.pop())
  
        return res