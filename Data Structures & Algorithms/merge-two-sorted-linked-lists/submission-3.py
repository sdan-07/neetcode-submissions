# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2: return  
        p1 = list1
        p2 = list2
        dummy = ListNode()
        cur=dummy

        while p1 and p2:
            if p1.val <= p2.val:
                cur.next = ListNode(p1.val)
                p1=p1.next
            elif p1.val > p2.val:
                cur.next = ListNode(p2.val)
                p2=p2.next
            
            cur=cur.next
        
        if p1 or p2: cur.next = p1 if p1 else p2


        return dummy.next