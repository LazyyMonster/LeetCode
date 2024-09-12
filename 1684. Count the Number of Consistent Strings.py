class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowSet = set(allowed)
        res = 0
        
        for w in words:
            counter = 0
            wlen = len(w)
            for c in w:
                if c in allowSet:
                    counter += 1
                else:
                    break
            if counter == wlen:
                res += 1 
        
        return res