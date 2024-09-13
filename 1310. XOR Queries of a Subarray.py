class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        answer = []
        prearr = [0]
        pre = 0

        for n in arr:
            pre = pre ^ n
            prearr.append(pre)

        for q in queries:
            res = prearr[q[0]] ^ prearr[q[1] + 1]
            answer.append(res)

        return answer