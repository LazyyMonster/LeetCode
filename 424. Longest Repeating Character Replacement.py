class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charDict = {}
        L = 0
        maxf = 0

        for R in range(len(s)):
            charDict[s[R]] = charDict.get(s[R], 0) + 1
            maxf = max(maxf, charDict[s[R]])
            window = R - L + 1
            if window - maxf > k:
                charDict[s[L]] -= 1
                L += 1

        return R - L + 1