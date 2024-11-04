class Solution:
    def buildComp(self, indexes: List[int], word: str) -> str:
        comp = ""
        for i in range(1, len(indexes)):
            L = indexes[i - 1]
            R = indexes[i]
            length = R - L
            while length:
                if length <= 9:
                    comp += str(length) + word[L]
                    length = 0
                else:
                    comp += "9" + word[L]
                    length -= 9
        return comp


    def compressedString(self, word: str) -> str:

        prefixes = [0]
        for i in range(1, len(word)):
            if word[i] != word[i - 1]:
                prefixes.append(i)

        prefixes.append(len(word))

        return self.buildComp(prefixes, word)