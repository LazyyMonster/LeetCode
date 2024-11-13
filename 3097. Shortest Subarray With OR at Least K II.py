class Solution:
    
    def decimal(self, bits: List[int]) -> int:
        n = len(bits)
        res = 0
        for i in range(n):
            if bits[n - i - 1] > 0:
                res += 2 ** (i)

        return res


    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        if k == 0:
            return 1

        n = len(nums)
        
        if n == 1:
            if nums[0] > k:
                return 1
            return -1

        bits = [0] * 32

        L = 0
        res = n + 1

        for R in range(n):
            add = nums[R]
            i = 0
            while add:
                b = add % 2 
                bits[31 - i] += b
                add //= 2
                i += 1

            while self.decimal(bits) >= k:
                res = min(res, R - L + 1)
                out = nums[L]
                i = 0
                while out:
                    b = out % 2 
                    bits[31 - i] -= b
                    out //= 2
                    i += 1
                L += 1

        return -1 if res == n + 1 else res