class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        modarray = [0] * k

        for n in arr:
            modarray[n % k] += 1

        if modarray[0] % 2 != 0:
            return False

        for i in range(1, int(len(modarray) / 2) + 1):
            if modarray[i] != modarray[(k - i)]:
                return False
        return True 