class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p = 0
        for n in nums:
            if n != 0:
                nums[p] = n
                p += 1
        for i in range(1, len(nums) - p + 1):
            nums[-i] = 0