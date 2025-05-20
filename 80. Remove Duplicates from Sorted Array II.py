class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return 1

        prev = nums[0]
        place = 1
        thesame = False

        for n in nums[1:]:
            if n != prev:
                nums[place] = n
                thesame = False
                place += 1

            elif not thesame:
                thesame = True
                nums[place] = n
                place += 1
            prev = n
        
        return place