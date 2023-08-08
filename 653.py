# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        l=[]
        def addtolist(root):
            l.append(root.val)
            if root.left:
                addtolist(root.left)
            if root.right:
                addtolist(root.right)
        addtolist(root)
        print(l)

        for i in l:
            if k/2==i:
                if l.count(i)>1:
                    return True
                else:
                    continue
            if k-i in l:
                return True
        return False
