class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.i = 0

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.i += 1
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        self.i += 1
        return "added at end"

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.i += 1
        return "added at start"

    def getlength(self):
        return self.i


# Insertion at index
def insertion(llist, data, index):
    if index < 0 or index > llist.getlength():
        return "Index out of bounds"

    if index == 0:
        llist.prepend(data)
        return "Inserted at index 0"

    new_node = Node(data)
    current = llist.head
    count = 0

    while current is not None and count < index - 1:
        current = current.next
        count += 1

    new_node.next = current.next
    current.next = new_node
    llist.i += 1
    return f"Inserted at index {index}"


# Deletion at index
def deletion(llist, index):
    if index >= llist.getlength() or index < 0:
        return "Index out of bounds"

    if index == 0:
        llist.head = llist.head.next
        llist.i -= 1
        return "Deleted from start"

    count = 0
    curr = llist.head
    while curr is not None and count < index - 1:
        curr = curr.next
        count += 1

    if curr.next is None:
        return "Next node is None, cannot delete"

    curr.next = curr.next.next
    llist.i -= 1
    return f"Deleted from index {index}"


# Testing
# llist = LinkedList()
# llist.append("A")
# llist.append("B")
# llist.append("C")
# llist.prepend("D")
#
# print("Before insertion:")
# llist.print_list()
# print("Length:", llist.getlength())
#
# print("\nAfter insertion at index 2:")
# print(insertion(llist, 3, 2))
# llist.print_list()
# print("Length:", llist.getlength())
#
# print("\nAfter deletion at index 0:")
# print(deletion(llist, 0))
# llist.print_list()
# print("Length:", llist.getlength())
