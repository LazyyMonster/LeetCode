class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        if len(words) != len(pattern):
            return False

        char_to_word = {}
        word_to_char = {}

        for i, c in enumerate(pattern):
            w = char_to_word.get(c)
            if w and w != words[i]:
                return False
            char_to_word[c] = words[i]

        for i, w in enumerate(words):
            c = word_to_char.get(w)
            if c and c != pattern[i]:
                return False
            word_to_char[w] = pattern[i]
        
        return True