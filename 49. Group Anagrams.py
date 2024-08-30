class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for s in strs:
            ch = [0] * 26

            for c in s:
                ch[ord(c) - ord('a')] += 1
            
            groups[tuple(ch)].append(s)
        
        return groups.values()