class Solution:
    def minimumSteps(self, s: str) -> int:
        z = 0
        swaps = 0

        for i, c in enumerate(s):
            if c == "0":
                swaps += i - z
                z += 1

        return swaps