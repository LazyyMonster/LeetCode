class Solution(object):
    def containsDuplicate(self, nums):
        numsSet = set()
        for num in nums:
            if num in numsSet:
                return True
            numsSet.add(num)
        return False