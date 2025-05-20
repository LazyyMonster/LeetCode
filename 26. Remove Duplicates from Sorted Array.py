class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev = nums[0]
        place = 1

        for n in nums:
            if n != prev:
                nums[place] = n
                prev = n
                place += 1
        return place