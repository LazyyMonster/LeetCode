class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        hl, nl = len(haystack), len(needle)
        for i in range(hl - nl + 1):
            for j in range(nl):
                if needle[j] != haystack[i + j]:
                    break
                if j == nl - 1:
                    return i
        return -1