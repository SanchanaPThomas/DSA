# cook your dish here
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, value):
        new_node = Node(value)
        
        # If there are no nodes in the linked list
        # Set the new node as head and return
        if self.head is None:
            self.head =new_node
            return
        
        # Iterate to the end of list
        current = self.head
        while current.next:
            current = current.next
        
        # Set the next of last value to the new Node
        current.next = new_node
        

    def get_last_value(self):
        
        if self.head is None:
            return -1
        
        current = self.head
        while current.next:
            current = current.next
        return current.value

if __name__ == "__main__":
    n = int(input())
    linked_list = LinkedList()
    vals = list(map(int, input().split()))
    for x in vals:
        linked_list.insert_at_end(x)
        print(linked_list.get_last_value(), end=" ")
