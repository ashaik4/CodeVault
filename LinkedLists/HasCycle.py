""""""
"""
7.3 Test for cyclicity 
"""
class ListNode:
    def __init__(self, data=0, next_node=None):
        self.data = data
        self.next = next_node


L = ListNode(11, ListNode(3,ListNode(5, ListNode(7, ListNode(2, ListNode(10, ListNode(1, ListNode(100))))))))

def has_cycle(head):
    fast = slow = head
    while fast and fast.next and fast.next.next:
        slow, fast = slow.next, fast.next.next
        if slow is fast: # there is a cycle
            # Tries to find the start of the cycle
            slow = head
            # Both pointers advance at the same time.
            while slow is not fast:
                slow, fast = slow.next, fast.next
            return slow # slow is the start of cycle
    return None

print(has_cycle(L))
