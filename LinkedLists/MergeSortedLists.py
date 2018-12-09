"""
7.1 EPI: Merge two sorted lists.
bruteforce solution: append each list to another and sort. (n log n )
optimal solution: traverse each list and keep appending the list nodes to tail node.
"""

class ListNode:
    def __init__(self, data=0, next_node=None):
        self.data = data
        self.next = next_node

L1 = ListNode(2, ListNode(5, ListNode(7)))
L2 = ListNode(3, ListNode(11))


def merge_sorted_lists(L1, L2):
    dummy_head = tail = ListNode()
    while(L1 and L2):
        if L1.data < L2.data:
            tail.next = L1
            L1 = L1.next
        else:
            tail.next = L2
            L2 = L2.next
        tail = tail.next
    tail.next = L1 or L2
    return dummy_head.next
merged_list = merge_sorted_lists(L1, L2)

while(merged_list):
    print(merged_list.data)
    merged_list = merged_list.next
