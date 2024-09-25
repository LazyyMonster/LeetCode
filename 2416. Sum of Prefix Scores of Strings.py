class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        prefixes = {}

        for w in words:
            prefix = ""
            for c in w:
                prefix += c
                prefixes[prefix] = prefixes.get(prefix, 0) + 1
        
        res = []
        for w in words:
            prefix = ""
            score = 0
            for c in w:
                prefix += c
                score += prefixes[prefix]
            res.append(score)
        
        return res