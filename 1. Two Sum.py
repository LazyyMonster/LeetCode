class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsMap = dict()

        for count, num in enumerate(nums):
            if target - num in numsMap:
                return [numsMap[target - num], count]
            numsMap[num] = count