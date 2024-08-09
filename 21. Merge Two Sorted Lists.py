# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = current = ListNode(0)
        i, j = list1, list2
        while i and j:
            if i.val < j.val:
                current.next, i = i, i.next
            else:
                current.next, j = j, j.next
            current = current.next
        current.next = i or j
        return head.next