class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        asc = False
        des = False
        n = len(nums)

        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                if des:
                    return False
                asc = True
            elif nums[i] < nums[i - 1]:
                if asc:
                    return False
                des = True

        return True