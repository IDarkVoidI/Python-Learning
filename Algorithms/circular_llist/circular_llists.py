class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLList:
    def __init__(self):
        self.head = None

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        temp = self.head
        
        if self.head:
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
        
        else:
            new_node.next = new_node
        
        self.head = new_node
    
    def print_list(self):
        current = self.head
        
        if self.head == None:
            return
        
        while True:
            print('Data', current.data)
            current = current.next
            if current == self.head:
                break