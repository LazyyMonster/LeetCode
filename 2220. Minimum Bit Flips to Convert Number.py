class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        s = self.convert(start, 2)
        g = self.convert(goal, 2)

        slen = len(s)
        glen = len(g)
        sub = abs(slen - glen)

        res = 0
        if slen > glen:
            for i in range(sub):
                if s[i] == '1':
                    res += 1
        else:
            for i in range(sub):
                if g[i] == '1':
                    res += 1
            
        com = min(slen, glen)
        for i in range(com):
            if s[slen - i - 1] != g[glen - i - 1]:
                res += 1
        return res


    def convert(self, num: int, base: int) -> str:
        res = ""

        while num:
            res = str(num % base) + res
            num //= base

        return res