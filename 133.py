"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node==None:
            return None
        copied={}
        def copy_node(n1,n2):
            n2.val= n1.val
            copied[n1.val]=n2
            for kid in n1.neighbors :
                if kid.val in copied.keys():
                    n2.neighbors.append(copied[kid.val])
                else:
                    n2_neighbors = Node(kid.val,[])
                    copy_node(kid,n2_neighbors)
                    n2.neighbors.append(n2_neighbors)
        answer_node=Node()
        copy_node(node,answer_node)
        """        
        printed=[]
        def printnode(n):
            
            print(n.val,n)
            printed.append(n.val)
            count=1
            for i in n.neighbors:
                print("-"*count,i.val)
                count=count+1
            for i in n.neighbors:
                if i.val not in printed:
                    printnode(i)
        printnode(node)
        printed=[]
        print("----")
        printnode(answer_node)
        """
        return answer_node