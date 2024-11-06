class Solution:
    def countOne(self, n: int) -> int:
        p = 2
        res = 0
        while n > 0:
            if n % p == 1:
                res += 1
            n //= p

        return res


    def canSortArray(self, nums: List[int]) -> bool:
        oneCnt = {}

        prev = 0
        isSorted = True
        for n in nums:
            oneCnt[n] = self.countOne(n)
            if n < prev:
                isSorted = False
            prev = n

        if isSorted:
            return True

        n = len(nums)
        for i in range(n - 1):
            for j in range(n - i - 1):
                L = nums[j]
                R = nums[j + 1]
                if L > R:
                    if oneCnt[L] != oneCnt[R]:
                        return False
                    else:
                        nums[j + 1], nums[j] = nums[j], nums[j + 1]

        return True