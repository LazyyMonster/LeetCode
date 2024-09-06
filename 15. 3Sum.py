class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []

        nums.sort()

        for i, x in enumerate(nums):
            if x > 0:
                break
            if i > 0 and x == nums[i - 1]:
                continue
            
            L, R = i + 1, len(nums) - 1
            while L < R:
                threeSum = x + nums[L] + nums[R]

                if threeSum < 0:
                    L += 1
                elif threeSum > 0:
                    R -= 1
                else:
                    output.append([x, nums[L], nums[R]])
                    L += 1
                    while nums[L] == nums[L - 1] and L < R:
                        L += 1
        return output