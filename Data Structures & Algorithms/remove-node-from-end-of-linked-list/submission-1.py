# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        c1 = dummy
        c2 = head

        for i in range(n):
            c2=c2.next

        while c2:
            c1=c1.next
            c2=c2.next
        
        c1.next = c1.next.next

        return dummy.next