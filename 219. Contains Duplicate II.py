class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        nums_indexes_map = {}

        for i, num in enumerate(nums):
            if num in nums_indexes_map:
                prev_i = nums_indexes_map[num]
                if i - prev_i <= k:
                    return True
                nums_indexes_map[num] = i
            else:
                nums_indexes_map[num] = i

        return False