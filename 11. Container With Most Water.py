class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0

        Li = 0
        Ri = len(height) - 1

        while Li < Ri:
            actualArea = min(height[Li], height[Ri]) * (Ri - Li)
            if actualArea > maxArea:
                maxArea = actualArea
            
            if height[Li] < height[Ri]:
                Li += 1
            else:
                Ri -= 1
        
        return maxArea