# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        mh=head
        while mh and mh.next:
            print(mh.val,mh.next.val)
            if mh.val==mh.next.val:
                rm=mh.next
                mh.next=rm.next
                rm.next=None
            else:
                mh=mh.next
        return head