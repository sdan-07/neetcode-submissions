# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes=[]
        p=head
        while p:
            nodes.append(p.val)
            p=p.next

        # 1,2,3,4  n=2
        nodes.pop(-n)

        dummy=ListNode()
        cur=dummy

        i=0
        while i<len(nodes):
            cur.next = ListNode(nodes[i])
            cur=cur.next
            i+=1
        return dummy.next