class Solution:
    def minSwaps(self, s: str) -> int:
        if s == "":
            return 0
        
        op = 0
        cl = 0
        res = 0
        for c in s:

            if c == "]":
                cl += 1
            else: 
                op += 1
            if cl > op:
                res += 1
                cl -= 1
                op += 1
        return res