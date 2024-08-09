# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if lists is None or len(lists) == 0:  # Updated variable name to 'lists'
            return None
        return self.divideAndMerge(lists, 0, len(lists) - 1)

    def divideAndMerge(self, input_lists, start_idx, end_idx):
        if start_idx == end_idx:
            return input_lists[start_idx]
        mid_idx = start_idx + (end_idx - start_idx) // 2
        left_part = self.divideAndMerge(input_lists, start_idx, mid_idx)
        right_part = self.divideAndMerge(input_lists, mid_idx + 1, end_idx)
        return self.mergeTwoLists(left_part, right_part)

    @staticmethod
    def mergeTwoLists(left_list, right_list):
        merged_head = ListNode(-1)
        temp_node = merged_head
        while left_list is not None and right_list is not None:
            if left_list.val < right_list.val:
                temp_node.next = left_list
                left_list = left_list.next
            else:
                temp_node.next = right_list
                right_list = right_list.next
            temp_node = temp_node.next

        while left_list is not None:
            temp_node.next = left_list
            left_list = left_list.next
            temp_node = temp_node.next

        while right_list is not None:
            temp_node.next = right_list
            right_list = right_list.next
            temp_node = temp_node.next

        return merged_head.next
