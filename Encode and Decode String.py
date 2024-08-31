class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        delimiter = "!"

        for s in strs:
            encoded += str(len(s)) + delimiter + s

        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        delimiter = "!"

        predelimiter = 0
        while predelimiter < len(s):
            delimiterIndex = predelimiter

            while s[delimiterIndex] != delimiter:
                delimiterIndex += 1
            
            wordLen = int(s[predelimiter:delimiterIndex])
            decoded.append(s[delimiterIndex + 1:delimiterIndex + 1 + wordLen])
            predelimiter = delimiterIndex + 1 + wordLen

        return decoded