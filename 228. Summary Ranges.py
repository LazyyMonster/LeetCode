class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
            
        left = right = nums[0]
        res = []

        for num in nums[1:]:
            if num - 1 == right:
                right = num
            else:
                res.append(f"{left}->{right}" if left != right else f"{right}")
                left = right = num
                              
        res.append(f"{left}->{right}" if left != right else f"{right}")
        return res