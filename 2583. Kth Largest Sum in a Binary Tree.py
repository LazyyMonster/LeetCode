# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def levelSum(self, level: int, root: Optional[TreeNode]):
            if len(self.sums) - 1 < level:
                self.sums.append(root.val)
            else:
                self.sums[level] += root.val

            if root.right:
                self.levelSum(level + 1, root.right)
            if root.left:
                self.levelSum(level + 1, root.left)

    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        self.sums = []
        self.levelSum(0, root)
        self.sums.sort(reverse=True)
        return self.sums[k - 1] if len(self.sums) >= k else -1