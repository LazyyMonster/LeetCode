class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = ""
        last = "d"

        while True:
            if (a >= b and a >= c and last != "a"):
                if a == 0: break
                if a >= 2:
                    res += "aa"
                    a -= 2
                else:
                    res += "a"
                    a -= 1
                last = "a"
            
            elif (b >= a and b >= c and last != "b"):
                if b == 0: break
                if b >= 2:
                    res += "bb"
                    b -= 2
                else:
                    res += "b"
                    b -= 1
                last = "b"
                
            elif (c >= a and c >= b and last != "c"):
                if c == 0: break
                if c >= 2:
                    res += "cc"
                    c -= 2
                else:
                    res += "c"
                    c -= 1
                last = "c"
            
            else:
                if (last == "a"):
                    if b >= c and b > 0:
                        res += "b"
                        b -= 1
                        last = "b"
                    elif c > 0:
                        res += "c"
                        c -= 1
                        last = "c"
                    else:
                        break
                
                elif (last == "b"):
                    if a >= c and a > 0:
                        res += "a"
                        a -= 1
                        last = "a"
                    elif c > 0:
                        res += "c"
                        c -= 1
                        last = "c"
                    else:
                        break
                
                elif (last == "c"):
                    if a >= b and a > 0:
                        res += "a"
                        a -= 1
                        last = "a"
                    elif b > 0:
                        res += "b"
                        b -= 1
                        last = "b"
                    else:
                        break
        return res