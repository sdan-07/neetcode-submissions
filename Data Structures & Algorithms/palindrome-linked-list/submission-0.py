# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        fast=slow=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        if fast: slow = slow.next

        slow = self.reverse(slow)

        p1 = head
        p2=slow

        while p2:
            if p1.val != p2.val:
                return False
            p1=p1.next
            p2=p2.next
        return True

    
    def reverse(self,head):
        cur=head
        pr = None

        while cur:
            nxt = cur.next
            cur.next = pr
            pr = cur
            cur = nxt
        return pr