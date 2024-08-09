# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        lin= ListNode(0)
        lin.next = head
        f = lin
        s = lin

        for _ in range(n + 1):
            f = f.next

        while f is not None:
            f = f.next
            s = s.next

        s.next = s.next.next

        return lin.next