class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        allSum = mean * (len(rolls) + n)

        nSum = allSum - sum(rolls)

        if nSum > n * 6 or nSum < n:
            return []
        
        if nSum == n:
            return [1] * n

        remainder = nSum % n
        quotient = nSum // n

        if remainder == 0:
            return [quotient] * n
        
        output = []
        for _ in range(remainder):
            output.append(quotient + 1)
        for _ in range(n - remainder):
            output.append(quotient)
        return output    