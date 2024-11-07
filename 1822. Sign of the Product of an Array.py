class Solution:
    def arraySign(self, nums: List[int]) -> int:
        below = 0

        for n in nums:
            if n == 0:
                return 0
            elif n < 0:
                below += 1

        if below % 2:
            return -1

        return 1    