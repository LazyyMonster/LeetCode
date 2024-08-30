class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numOccurences = dict()

        for num in nums:
            numOccurences[num] = numOccurences.get(num, 0) + 1
        
        listOccurences = [[] for _ in range(len(nums) + 1)]
        for num, occur in numOccurences.items():
            listOccurences[occur].append(num)
        
        topKelements = []
        for i in range(len(nums), 0, -1):
            for num in listOccurences[i]:
                topKelements.append(num)
                if len(topKelements) == k:
                    return topKelements