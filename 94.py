# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        def inadd(root):
            if root==None :
                return
            if root.left!=None: 
                inadd(root.left)
            ans.append(root.val)
            if root.right!=None:
                inadd(root.right)
        inadd(root)
        return ans