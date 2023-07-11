# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if preorder ==[]:
            return None
        root= TreeNode(preorder[0])
        s=inorder.index(preorder[0])       
        if s!=0:
            root.left=self.buildTree(preorder[1:s+1],inorder[:s])
        else:
            root.left=None
        if s!=len(preorder)-1:
            root.right=self.buildTree(preorder[s+1:],inorder[s+1:])
        else:
            root.right=None
        return root