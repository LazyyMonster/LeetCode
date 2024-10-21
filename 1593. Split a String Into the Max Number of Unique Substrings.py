class Solution:
    res = 0

    def split(self, s: str, p: int, cnt: int, sub: set) -> None:
        if p == len(s):
            self.res = max(cnt, self.res)
            return
        
        for i in range(p, len(s)):
            substring = s[p:i + 1]
            if substring not in sub:
                sub.add(substring)
                self.split(s, i + 1, cnt + 1, sub)
                sub.remove(substring)


    def maxUniqueSplit(self, s: str) -> int:
        substrings = set()
        self.split(s, 0, 0, substrings)
        return self.res