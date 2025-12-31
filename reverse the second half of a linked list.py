class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def reverse_second_half(head):
    if not head or not head.next:
        return head

    # Step 1: Find middle
    slow = fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    middle = slow

    # Step 2: Reverse second half
    prev = None
    curr = middle.next

    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    # Step 3: Connect reversed half
    middle.next = prev

    return head
