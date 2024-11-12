class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort(key = itemgetter(0))

        queries = [(q, i) for i, q in enumerate(queries)]

        queries.sort(key = itemgetter(0))

        n = len(items)
        maxBeauty = 0
        p = 0
        res = [0] * len(queries)

        for q, i in queries:
            
            while p < n and q >= items[p][0]:
                maxBeauty = max(maxBeauty, items[p][1])
                p += 1
            res[i] = maxBeauty
  
        return res