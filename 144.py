# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        def preadd(root):
            if root==None :
                return
            ans.append(root.val)
            if root.left!=None:
                preadd(root.left)
            if root.right!=None:
                preadd(root.right)
        preadd(root)
        return ans