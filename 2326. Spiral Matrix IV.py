# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        matrix = [[-1 for _ in range(n)] for _ in range(m)]

        lcol = 0
        rcol = n - 1
        urow = 0
        drow = m - 1
        actual = head
        while actual:
            for c in range(lcol, rcol + 1):
                if not actual:
                    return matrix
                matrix[urow][c] = actual.val
                actual = actual.next
            urow += 1
            for r in range(urow, drow + 1):
                if not actual:
                    return matrix
                matrix[r][rcol] = actual.val
                actual = actual.next
            rcol -= 1
            for c in range(rcol, lcol - 1, -1):
                if not actual:
                    return matrix
                matrix[drow][c] = actual.val
                actual = actual.next
            drow -= 1
            for r in range(drow, urow - 1, -1):
                if not actual:
                    return matrix
                matrix[r][lcol] = actual.val
                actual = actual.next
            lcol += 1

        return matrix