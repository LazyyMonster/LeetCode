class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        res = 0
        bits = [0] * 24

        for n in candidates:
            binary = bin(n)[2:]
            bLen = len(binary)
            for i, bit in enumerate(binary):
                if bit == "1":
                    bits[bLen - i - 1] += 1

        res = max(bits)

        return res