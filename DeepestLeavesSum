# Problem: https://leetcode.com/problems/deepest-leaves-sum/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.level = 0
        self.sum1 = 0
    
    def findDeepestLeavesSum(self, root, depth):
        if root == None:
            return 
        if root.right == None and root.left == None:
            if depth == self.level:
                self.sum1 += root.val
            if depth > self.level:
                self.level = depth
                self.sum1 = root.val
        else:
            self.findDeepestLeavesSum(root.left, depth+1)
            self.findDeepestLeavesSum(root.right, depth+1)
    
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        self.findDeepestLeavesSum(root, 0)
        return self.sum1
