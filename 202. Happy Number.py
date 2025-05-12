class Solution:
    def isHappy(self, n: int) -> bool:
        
        nums_seen = set()

        def digits_squares_sum(n):
            res = 0
            while n:
                res += (n % 10) ** 2
                n //= 10
            return res

        while n != 1:
            res = digits_squares_sum(n)
            if res in nums_seen:
                return False
            nums_seen.add(res)
            n = res
        
        return True