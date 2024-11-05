class Solution:
    def minChanges(self, s: str) -> int:
        sLen = len(s)
        changes = 0
        for i in range(0, sLen, 2):
            if s[i] != s[i + 1]:
                changes += 1
        
        return changes