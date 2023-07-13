# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def isancestor(root,p):
            if not root:
                return False
            if not root.left:
                return (root.val==p.val) or isancestor(root.right,p)
            if not root.right:
                return (root.val==p.val) or isancestor(root.left,p)
            return (root.val==p.val) or isancestor(root.left,p) or isancestor(root.right,p)
        lca=[]
        def changelca(root,p,q):
            if not root:
                return root
            if (isancestor(root,p) and isancestor(root,q)):
                lca.append(root)     
            if root.val>p.val and   root.val>q.val  :
                root.right=None
            if root.val<p.val and   root.val<q.val  :
                root.left=None
            changelca(root.left,p,q)
            changelca(root.right,p,q)
        changelca(root,p,q)
        return lca[-1]


