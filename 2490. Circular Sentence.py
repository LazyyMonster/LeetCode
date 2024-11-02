class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        strings = sentence.split(" ")
        first = strings[0]

        if len(strings) == 1:
            return first[0] == first[-1]

        if first[0] != strings[-1][-1]:
            return False

        for i in range (len(strings) - 1):
            if strings[i][-1] != strings[i + 1][0]:
                return False

        return True