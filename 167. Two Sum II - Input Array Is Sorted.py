class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L = 0
        R = len(numbers) - 1

        while L < R:
            currentSum = numbers[L] + numbers[R]
            if currentSum < target:
                L += 1
            elif currentSum > target:
                R -= 1
            else:
                return [L + 1, R + 1]