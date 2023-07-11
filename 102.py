# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ld={}
        def addtodict(level,root):
            if not level in ld :
                ld[level]=[]
            
            if root==None:
                return
            ld[level].append(root.val)
            if root.left!=None:
                addtodict(level+1,root.left)
            if root.right!=None:
                addtodict(level+1,root.right)
        addtodict(0,root)
        rl=[]
        for keys in ld.keys():
            if ld[keys]==[]:
                rl.append(keys)
        for keys in rl:
            del ld[keys]
        return ld.values()
            