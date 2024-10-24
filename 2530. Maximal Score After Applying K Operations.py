class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        h = []
        score = 0 
        
        for n in nums:
            heappush(h, -n)
        
        for i in range(k):
            m = -heapq.heappop(h)
            score += m
            heapq.heappush(h, -math.ceil(m / 3))
        
        return score