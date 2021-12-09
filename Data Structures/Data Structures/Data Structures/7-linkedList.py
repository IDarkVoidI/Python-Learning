# methods of linked lists
# 1. append
# 2. prepend
# 3. insert_after_node

class Node:
    def __init__(self, data):
        self.data = data  # A, B, C etc.
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None  # points to the first node inside the link list

    # print
    def print_list(self):
        cur_node = self.head
        while cur_node:
            print("Data", cur_node.data)
            cur_node = cur_node.next

    # append method
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("Previous node does not exist")
            return
        new_node = Node(data)

        new_node.next = prev_node.next
        prev_node.next = new_node


l_list = LinkedList()
l_list.append('Batman')
l_list.append('Spiderman')
l_list.append('Centos')
l_list.append('Ubuntu')

l_list.print_list()
print('_______')

# each next is an object ID reference
l_list.insert_after_node(l_list.head.next.next, 'D')

l_list.print_list()

# new_node = {data: 'Z', next: None', _id: '0x7f87d013ca90'}
