"""
7.11 Test if the linked list is palindromic
"""
"""
idea: reverse the second half of the list and check if nodes are equal. 
"""
from ListNode import ListNode

L = ListNode(3,ListNode(2,ListNode(2,ListNode(11,ListNode(2,ListNode(2,ListNode(3)))))))

def reverse_list(L):
    dummy_head = sublist_head = ListNode(0, L)
    sublist_iter = sublist_head.next
    while(sublist_iter.next ):
        temp = sublist_iter.next
        sublist_iter.next = temp.next
        temp.next = sublist_head.next
        sublist_head.next = temp
    return dummy_head.next


def is_list_palindromic(L):
    slow = fast = L
    while fast and fast.next:
        fast, slow = fast.next.next, slow.next
    first_half, second_half = L , reverse_list(slow)
    while first_half and second_half:
        if first_half.data != second_half.data:
            return False
        first_half, second_half = first_half.next, second_half.next
    return True
print(is_list_palindromic(L))

