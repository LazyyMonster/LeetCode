class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        res = [0] * len(nums)
        xorTotal = 0
        maxVal = (2 ** maximumBit) - 1
        
        for i, n in enumerate(nums):
            xorTotal ^= n
            res[-i - 1] = xorTotal ^ maxVal

        return res