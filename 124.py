# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res=[root.val]
        def dfs(root):
            if not root:
                return 0
            leftmax=dfs(root.left)
            leftmax=max(0,leftmax)
            rightmax=dfs(root.right)
            rightmax=max(0,rightmax)
            res[0]=max(res[0],root.val+leftmax+rightmax)
            return root.val+max(leftmax,rightmax)
        dfs(root)
        return res[0]