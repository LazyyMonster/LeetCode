class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        if len(t) == 0:
            return False
        
        end = len(s)
        wanted = 0

        for c in t:
            if c == s[wanted]:
                wanted += 1
                if wanted == end:
                    return True

        return False