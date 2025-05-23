class Solution:
    def firstUniqChar(self, s: str) -> int:
        chars_map = {}
        
        for i, c in enumerate(s):
            if c in chars_map:
                chars_map[c] = -1
            else:
                chars_map[c] = i
                             
        for c in s:
            ci = chars_map[c]
            if ci != -1:
                return ci
            
        return -1