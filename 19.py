# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next==None:
            return None

        ans=op=head
        count=0
        while head:
            head=head.next
            count=count+1
        if count==n:
            return ans.next
        for i in range(0,count-n-1):
            ans=ans.next
        if ans.next and ans.next.next:
            ans.next=ans.next.next
        else:
            ans.next=None

        return op
