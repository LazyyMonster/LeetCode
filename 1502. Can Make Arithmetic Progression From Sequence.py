class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        maxN = max(arr)
        minN = min(arr)
        if minN == maxN:
            return True

        setArr = set(arr)
        if len(setArr) != len(arr):
            return False
        
        step = (maxN - minN) / (len(arr) - 1)
        element = minN
        while element < maxN:
            element += step
            if element not in setArr:
                return False

        return True