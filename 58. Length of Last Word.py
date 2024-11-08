class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = len(s)
        end = n

        for i in range(n - 1, -1, -1):
            if s[i] != " ":
                end = i        
                break

        for i in range(i, -1, -1):
            if s[i] == " ":
                return end - i

        return end + 1