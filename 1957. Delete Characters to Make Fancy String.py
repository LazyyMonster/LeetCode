class Solution:
    def makeFancyString(self, s: str) -> str:
        sLen = len(s)
        if sLen < 3:
            return s

        res = s[:2]

        for i in range(2, sLen):
            c = s[i]
            if c != res[-1]:
                res += c
            elif c != res[-2]:
                res += c
        return res        