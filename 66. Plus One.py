class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        for i in range(1, n + 1):
            if digits[-i] < 9:
                digits[-i] += 1
                return digits
            else:
                digits[-i] = 0
        
        return [1] + digits