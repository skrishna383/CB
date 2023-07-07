# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head and head.next:
            ans=head.next
            first,second=head,head.next
            while second:
                if second.next:
                    if second.next.next:       
                        dum1=second.next
                        dum2=dum1.next
                    else :
                        dum1,dum2=second.next,second.next
                else :
                    dum1,dum2=None,None
                second.next=first
                first.next=dum2
                first,second=dum1,dum2
            return ans
        else:
            return head
