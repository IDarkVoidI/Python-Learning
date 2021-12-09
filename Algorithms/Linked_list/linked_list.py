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
    
    def delete_node(self, key):
        current_node = self.head
        if current_node and current_node.data == key:
            self.head = current_node.next
            current_node = None
            return
        prev = None
        while current_node and current_node.data != key:
            prev = current_node
            current_node = current_node.next
        if current_node is None:
            return
        prev.next = current_node.next
        current_node = None
    
    def delete_node_at_pos(self, key):
        if self.head:
            current_node = self.head
            if key == 0:
                self.head = current_node.next
                current_node = None
                return
        previous = None
        count = 0
        while current_node and count != key:
            previous = current_node
            current_node = current_node.next
            count += 1
        if current_node == None:
            return
        previous.next = current_node.next
        current_node = None
    
    def len_iterate(self):
        count = 0
        current_node = self.head
        while current_node:
            count += 1
            current_node = current_node.next
        return count
    
    def len_recursive(self, node):
        if node is None:
            return 0
        return 1 + self.len_recursive(node.next)
    
    def swap(self, key1, key2):
        # 2 keys are the same
        if key1 == key2:
            return
        # Assign the prev to none and current to head
        previous1 = None
        current_node1 = self.head
        while current_node1 and current_node1.data != key1:
            previous1 = current_node1
            current_node1 = current_node1.next
        
        previous2 = None
        current_node2 = self.head
        while current_node2 and current_node2.data != key2:
            previous2 = current_node2
            current_node2 = current_node2.next
        
        if not current_node1 or not current_node2:
            return
        
        if previous1:
            previous1.next = current_node2
        else:
            self.head = current_node2
        
        if previous2:
            previous2.next = current_node1
        else:
            self.head = current_node1
        
        current_node1.next, current_node2.next = current_node2.next, current_node1.next
    
    def reverse(self):
        previous = None
        current_node = self.head
        # Arrows are flipped to reverse the pointers
        # 1) Keep track of next of every current node
        # 2) Assign current_node.next to previous
        # 3) Updating the previous with current node
        # 4) Update current node with next
        while current_node:
            nxt = current_node.next
            current_node.next = previous
            previous = current_node
            current_node = nxt
        self.head = previous
    
    def merge_sorted(self, list2):
        s = None
        p = self.head
        q = list2.head
        if not p or not q:
            return q or p
        
        if p and q:            
            if p.data <= q.data:
                s = p
                p = s.next
                print(f's is {s.data} and p is {p.data}')
            else:
                s = q
                q = s.next
                print(f's is {s.data} and q is {q.data}')
            new_head = s
        while p and q:
            if p.data <= q.data:
                s.next = p
                s = p
                p = s.next
            else:
                s.next = q
                s = q
                q = s.next
        if not p:
            s.next = q
            print(f'q is {q.data}')
        if not q:
            s.next = p
            print(f'p is {p.data}')
        self.head = new_head
        return self.head

        # Remove duplicated -> No inputs
        # Sample input: A, A, B, B, C, C -> A B C
        # 1) Create 3 var: current = self.head, previous = None, dup_val = dict{}
        # 2) While current:
        # 3) If current.data in dup_val:
        # previous = current.next   
        # current = None
        #       else:
        #       dup_val[current.data] = 1
        #       A : 1
        #       A : 1
        #       previous = current
        #current = previous.next
    
    def del_dup(self):
        current = self.head
        previous = None
        dup_val = {}
        while current:
            if current.data in dup_val:
                previous.next = current.next
                current = None
            else:
                dup_val[current.data] = 1
                previous = current
            current = previous.next
    # 1) Calculate the length of the ll
    # 2) Countdown from the total length until ns is reached
    
    def print_nth_from_last(self, n):
        length = self.len_iterate()
        current_node = self.head  
        while current_node:
            if length == n:
                return current_node.data
            length -= 1
            current_node = current_node.next
        if current_node == None:
            return

# Move tail to head
# Node in the tail and node in the head should change their places
# A, B, C, D =》D, B, C, A
    def swap_tail_head(self):
        # current = self.head
        # previous = None
        # while current:    
        #     previous = current
        #     current = current.next
        #     nxt = current.next
        #     current = nxt
        # previous, current = current, previous
        # return
        temp = self.head
        seclast = None
        if not temp or not temp.next:
            return
        while temp and temp.next:
            seclast = temp
            temp = temp.next
        seclast.next = None
        temp.next = self.head
        self.head = temp

# Problem statement: Find occurences of an input

# Given a singly linked list and a key, count the number of occurrences of the given key in the linked list. For example, if the given linked list is 1->2->1->2->1->3->1 and the given key is 1, then the output should be 4

# Algorithm:

# 1. Initialize count as zero.
# 2. Loop through each element of linked list:
#      a) If element data is equal to the passed input then
#         increment the count.
# 3. Return count.
    def count(self, key):
        count = 0
        current = self.head
        while current is not None:
            if key == current.data:
                count += 1
            current = current.next        
        return count
# The steps are: 

# Traverse the two linked lists in order to add preceding zeros in case a list is having lesser digits than the other one.
# Start from the head node of both lists and call a recursive function for the next nodes.
# Continue it till the end of the lists.
# Creates a node for current digits sum and returns the carry.
    def add_lists(self, l1, l2):
        current = None
        previous = None
        carry = 0
        while l1 or l2:
            fdata = 0 if l1 is None else l1.data
            sdata = 0 if l2 is None else l2.data
            sum = carry + fdata + sdata


            carry = 1 if sum >= 10 else 0
            sum = sum if sum < 10 else sum%10
            temp = Node(sum)


            if self.head is None:
                self.head = temp
            else:
                previous.next = temp


            previous = temp


            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

            if carry > 0:
                temp.next = Node(carry)