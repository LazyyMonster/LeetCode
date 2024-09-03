class Solution:
    def getLucky(self, s: str, k: int) -> int:

        result = ""
        for c in s:
            result += str(ord(c) - ord('a') + 1)

        def sumDigits(n: int) -> int:
            sum = 0
            while n:
                sum += n % 10
                n //= 10
            return sum

        result = int(result)
        for _ in range(k):
            result = sumDigits(result)

        return result