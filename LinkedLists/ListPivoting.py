"""
7.12: Implement list pivoting.
For any integer k, the pivot of a list of integers with respect to k is that list with its nodes
reordered so that all nodes containing keys less than k appear before nodes containing k, and all nodes
containing keys greater than k appear after the nodes containing k.
eg:
input: 3 -> 2 -> 2 -> 11 -> 7 -> 5 -> 11
output:3 -> 2 -> 2 -> 5 -> 7 -> 11 -> 11
"""
from ListNode import ListNode
L = ListNode(3, ListNode(2, ListNode(2, ListNode(11,ListNode(7, ListNode(5, ListNode(11)))))))

def list_pivoting(L, x):
    less_head = less_iter = ListNode()
    equal_head = equal_iter = ListNode()
    great_head = great_iter = ListNode()
    while L:
        if L.data < x:
            less_iter.next = L
            less_iter = less_iter.next
        elif L.data == x:
            equal_iter.next = L
            equal_iter = equal_iter.next
        else:
            great_iter.next = L
            great_iter = great_iter.next
        L = L.next
    #combine three lists
    great_iter.next = None
    equal_iter.next = great_head.next
    less_iter.next = equal_head.next
    return less_head.next

L_pivoted = list_pivoting(L, 5)

while(L_pivoted):
    print(L_pivoted.data)
    L_pivoted = L_pivoted.next