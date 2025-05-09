class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(magazine) < len(ransomNote):
            return False

        ransomCharacters = {}
        magazineCharacters = {}

        for c in ransomNote:
            ransomCharacters[c] = ransomCharacters.get(c, 0) + 1

        for c in magazine:
            magazineCharacters[c] = magazineCharacters.get(c, 0) + 1
            
        for c, occur in ransomCharacters.items():
            if magazineCharacters.get(c, 0) < occur:
                return False
            
        return True
