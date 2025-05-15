class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        distinct_nums = set(nums)
        max_len = 0

        for n in distinct_nums:
            if n - 1 in distinct_nums:
                continue

            seq_len = 1
            while n + seq_len in distinct_nums:
                seq_len += 1
            
            if seq_len > max_len:
                max_len = seq_len
                
        return max_len