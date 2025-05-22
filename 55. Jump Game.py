class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_jump = 0
        for i in range(len(nums) - 1):
            jump = nums[i]
            if jump == 0 and max_jump <= i:
                return False
            max_jump = max(max_jump, jump + i)
        return max_jump >= len(nums) - 1