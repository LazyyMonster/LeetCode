# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNode(self, node: Optional[TreeNode], level: int) -> None:
        self.levelSums[level] = self.levelSums.get(level, 0) + node.val
        if node.right:
            self.sumNode(node.right, level + 1)
        if node.left:
            self.sumNode(node.left, level + 1)


    def changeNode(self, node: Optional[TreeNode], level: int) -> None:
        if level >= len(self.levelSums):
            return
        r = node.right
        l = node.left
        res = self.levelSums[level]
        if r:
            res -= r.val
        if l:
            res -= l.val
            node.left.val = res
            self.changeNode(node.left, level + 1)
        if r:
            node.right.val = res
            self.changeNode(node.right, level + 1)
        

    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.levelSums = {0 : 0, 1: 0}
        if root.left:
            if root.left.left:
                self.sumNode(root.left.left, 2)    
            if root.left.right:
                self.sumNode(root.left.right, 2)
        if root.right:
            if root.right.left:
                self.sumNode(root.right.left, 2)    
            if root.right.right:
                self.sumNode(root.right.right, 2)

        root.val = 0
        if root.left:
            root.left.val = 0
            self.changeNode(root.left, 2)    
            
        if root.right:
            root.right.val = 0
            self.changeNode(root.right, 2)    


        return root