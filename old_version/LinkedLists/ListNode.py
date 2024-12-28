class ListNode:
    def __init__(self, data=0, next_node = None):
        self.data = data
        self.next = next_node
    def get_data(self):
        return self.data

    def get_next_node(self):
        return self.next

    def set_data(self, data):
        self.data = data

    def set_next_node(self, next_node):
        self.next = next_node

