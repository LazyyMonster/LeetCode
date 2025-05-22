class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        L = R = 0
        while R < len(nums) - 1:
            max_reachable = R
            for i in range(L, R + 1):
                max_reachable = max(max_reachable, i + nums[i])
            L, R = R + 1, max_reachable 
            jumps += 1
        return jumps