# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(p,q):
            if p==None and q==None:
                return True
            if (p==None and q!=None) or (p!=None and q==None):
                return False
            return (p.val==q.val) and (isSameTree(p.left,q.left)) and (isSameTree(p.right,q.right))
        if subRoot ==None:
            return True
        if root==None:
            return False
        return isSameTree(subRoot,root) or self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot) 