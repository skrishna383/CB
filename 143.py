# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        fast,slow,mh=head,head,head
        while fast and fast.next :
            slow,fast=slow.next,fast.next.next
        prev , cur=None, slow
        while cur:
            cur.next,prev,cur=prev,cur,cur.next
        while prev.next:
            dummy=mh.next
            mh.next=prev
            mh,dummy=dummy,prev.next
            prev.next,prev=mh,dummy

        return head
            