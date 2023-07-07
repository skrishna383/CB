# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]: 
        ans_head=None 
        while head!=None :
            n=ListNode(head.val)
            n.next=ans_head
            ans_head=n
            head=head.next
        return ans_head
