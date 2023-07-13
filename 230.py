# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        li=[]
        def treetolist (root):
            if root ==None:
                return
            if root.left:
                treetolist(root.left)
            li.append(root.val)
            if root.right:
                treetolist(root.right)
        treetolist(root)
        return li[k-1]