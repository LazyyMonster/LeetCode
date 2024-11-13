class Solution:

    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        res = 0
        n = len(nums)
        
        for i in range(n):
            num = nums[i]
            floor = lower - num
            ceiling = upper - num
            floorIndex = bisect_left(nums, floor, i + 1, n)
            ceilingIndex = bisect_right(nums, ceiling, i + 1, n)
            
            res += ceilingIndex - floorIndex

        return res