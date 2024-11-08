class Solution:
    def toLowerCase(self, s: str) -> str:
        n = len(s)
        res = ""
        for i in range(n):
            pos = ord(s[i])
            if ord('A') <= pos <= ord('Z'):
                res += chr(pos + 32)
            else:
                res += s[i]
        return res