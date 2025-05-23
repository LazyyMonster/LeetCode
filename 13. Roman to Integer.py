class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}

        prev = 0
        res = 0
        for i in range(len(s) - 1, -1, -1):
            c = s[i]
            v = roman[c]
            
            if prev > v:
                res -= v
            else:
                res += v

            prev = v
        
        return res