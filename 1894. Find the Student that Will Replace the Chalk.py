class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:

        k = k % sum(chalk)
        for i in range(0, len(chalk)):
            k -= chalk[i]
            if (k < 0):
                return i