# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        count=0
        if head==None:
            return False
        while head.next!=None:
            count=count+1
            head=head.next
            if count>10001:
                return True
        return False