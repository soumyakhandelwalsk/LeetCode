#Problem: https://leetcode.com/problems/validate-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.num = None
    def isValid(self, root):
        if root == None:
            return True
        else:
            if self.isValid(root.left):
                if (self.num == None):
                    self.num = root.val
                elif root.val > self.num:
                     self.num = root.val
                else:
                    return False
                return self.isValid(root.right)
            else:
                return False
            
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValid(root)
        
        
