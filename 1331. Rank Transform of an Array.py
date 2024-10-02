class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        if len(arr) == 0:
            return []

        sortedArr = sorted(arr)
        ranks = {}
        rank = 0
        prevNum = sortedArr[0] - 1
        
        for n in sortedArr:
            if n > prevNum:
                rank += 1
            ranks[n] = rank
            prevNum = n
        
        for i in range(len(arr)):
            n = arr[i]
            arr[i] = ranks[n]

        return arr 