class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        letterDict = dict()
        
        for letter in s:
            if letter in letterDict:
                letterDict[letter] += 1
            else:
                letterDict[letter] = 1
        for letter in t:
            if letter in letterDict:
                letterDict[letter] -= 1
            else:
                return False

        if any(letterDict.values()):
            return False

        return True
