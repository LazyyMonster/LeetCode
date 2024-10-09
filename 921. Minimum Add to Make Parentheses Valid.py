class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        op = 0
        cl = 0
        for c in s:
            if c == ")":
                if op > 0:   
                    op -= 1
                else: 
                    cl += 1
            else:
                op += 1
      
        return cl + op