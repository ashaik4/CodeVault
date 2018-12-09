"""
"""
"""
7.2 Reverse a single sublist
---------------------------- 
11 -> 3 -> 5 -> 7 -> 2
----------------------
11 -> 7 -> 5 -> 3 -> 2
"""
class ListNode:
    def __init__(self, data=0, next_node=None):
        self.data = data
        self.next = next_node


L = ListNode(11, ListNode(3,ListNode(5, ListNode(7, ListNode(2, ListNode(10, ListNode(1, ListNode(100))))))))

def recursive_traversal(L):
    if L:
        print(L.data)
        recursive_traversal(L.next)

def reverse_sublist(L , start, finish):
    dummy_head = sublist_head = ListNode(0, L)
    for _ in range(1, start):
        sublist_head = sublist_head.next
        print(_)
    print("sublist_head", sublist_head.data)
    # reverses sublist
    sublist_iter = sublist_head.next
    for _ in range(finish - start):
        """
        11 -> 3 -> 5 -> 7
        """
        temp = sublist_iter.next
        sublist_iter.next = temp.next
        temp.next = sublist_head.next
        sublist_head.next = temp
    return dummy_head.next

reversed_L = reverse_sublist(L , 1,8)
while(reversed_L):
    print(reversed_L.data)
    reversed_L = reversed_L.next




