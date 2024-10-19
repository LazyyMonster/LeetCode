class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if n == 1:
            return "0"

        def invert(s: list) -> list:
            res = []

            for c in s:
                res.append(1 if c == 0 else 0)
            return res

        prev = [0]
        actual = []

        for _ in range(n - 1):
            actual = prev + [1] + (invert(prev))[::-1]
            prev = actual
        
        return str(actual[k - 1])