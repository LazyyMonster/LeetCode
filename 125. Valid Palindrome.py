class Solution:
    def isPalindrome(self, s: str) -> bool:

        L, R = 0, len(s) - 1
        while L < R:
            while L < R and not self.cAlphaNum(s[L]):
                L += 1
            while L < R and not self.cAlphaNum(s[R]):
                R -= 1

            if s[L].lower() != s[R].lower():
                return False

            L, R = L + 1, R - 1

        return True

    def cAlphaNum(self, c: chr) -> bool:
        return (ord('a') <= ord(c) <= ord('z') or 
                ord('A') <= ord(c) <= ord('Z') or
                ord('0') <= ord(c) <= ord('9'))