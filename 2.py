# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        d1,d2=l1,l2
        ans=[]
        r=0
        while (d1 != None) | (d2 != None):
            if d1== None :
                l3=r+d2.val
                r=l3//10
                l3=l3%10
                d2= d2.next
            elif d2== None :
                l3=r+d1.val
                r=l3//10
                l3=l3%10
                d1= d1.next
            elif  (d1 != None) & (d2 != None):
                l3=r+d1.val+d2.val
                r=l3//10
                l3=l3%10
                d1= d1.next
                d2=d2.next
            ans.append(l3)
        if r!=0: ans.append(r)
        cur = dummy = ListNode(ans[0])
        for e in ans[1::]:
            cur.next = ListNode(e)
            cur = cur.next
        return dummy
            
            





