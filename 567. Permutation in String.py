class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1d = {}
        window = {}

        for c in s1:
            s1d[c] = s1d.get(c, 0) + 1

        for i in range(len(s1)):
            window[s2[i]] = window.get(s2[i], 0) + 1

        if s1d == window:
            return True
        
        L = 0
        for R in range(len(s1), len(s2)):                
            window[s2[L]] -= 1
            window[s2[R]] = window.get(s2[R], 0) + 1

            if window[s2[L]] == 0:
                del window[s2[L]]        
            if window == s1d:
                return True
            L += 1

        return False