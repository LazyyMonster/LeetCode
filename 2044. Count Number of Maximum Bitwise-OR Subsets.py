class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        target = 0

        for n in nums:
            target = target | n
        
        res = 0
        for m in range(1 << len(nums)):
            subset = 0
            for i in range(len(nums)):
                if m & (1 << i):
                    subset = subset | nums[i]

            if subset == target:
                    res += 1
        
        return res