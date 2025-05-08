class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_to_t_map = {}
        for i, c in enumerate(s):
            rep = s_to_t_map.get(c)
            if not rep:
                if t[i] in s_to_t_map.values():
                    return False
                s_to_t_map[c] = t[i]

            elif rep != t[i]:
                return False
                
        return True