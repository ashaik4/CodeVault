"""
2.1 Remove duplicates:
Remove duplicates from an unsorted linkedlist
"""


class ListNode:
    def __init__(self, data=0, next_node=None):
        self.data = data
        self.next = next_node


L = ListNode(2, ListNode(2, ListNode(3, ListNode(5, ListNode(7, ListNode(11, ListNode(11)))))))


def remove_duplicates(L):
    it = L 
    while it: 
        next_distinct = it.next 
        while next_distinct and next_distinct.data == it.data: 
            next_distinct = next_distinct.next 
        it.next = next_distinct
        it = next_distinct
    return L


L_edited = remove_duplicates(L)
while L_edited:
    print(L_edited.data)
    L_edited = L_edited.next
