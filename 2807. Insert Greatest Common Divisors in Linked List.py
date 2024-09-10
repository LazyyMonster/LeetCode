# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        actual = head

        if not actual.next:
            return head

        while actual.next:
            gcd = self.gcd(actual.val, actual.next.val)
            middle = ListNode(gcd, actual.next)
            actual.next = middle
            actual = middle.next

        return head

    
    def gcd(self, a: int, b: int):
        while b:
            a, b = b, a % b
        return a