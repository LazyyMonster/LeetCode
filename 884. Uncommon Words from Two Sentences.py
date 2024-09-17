class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        arr = s1.split(" ") + s2.split(" ")

        words = {}
        for w in arr: 
            words[w] = words.get(w, 0) + 1
        
        res = []
        for w, c in words.items():
            if c == 1:
                res.append(w)
        
        return res