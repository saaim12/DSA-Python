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

#insertion using recursion
def insertion_recursion(newval,llist,index):
    if index <0 or index > llist.getlength():
        return "index out of bounds"
    def insert(node,index):
        if index==0:
            newn=Node(newval)
            newn.next=node
            return newn
        node.next=insert(node.next,index-1)
        return node
    llist.head=insert(llist.head,index)
    llist.i+=1
    return f"Inserted at index {index} (recursively)"

def reverseBetween( head, left, right):
    if not head or left == right:
        return head
    dummy = Node(0)
    dummy.next = head
        # 1. Locate Pointers
        # 'node_before_start' is the node immediately preceding 'left'
    node_before_start = dummy
    for _ in range(left - 1):
        node_before_start = node_before_start.next
        # 'sublist_tail' is the first node of the sublist (original position 'left')
    sublist_tail = node_before_start.next
        # 2. Reverse the Sublist (Standard Iterative Reversal)
        # We need to reverse 'right - left + 1' nodes.
    prev = None
    curr = sublist_tail
        # 'i' counts the nodes being reversed
    for _ in range(right - left + 1):
        temp_next = curr.next  # 1. Save the next node
        curr.next = prev  # 2. Reverse the current node's pointer
        prev = curr  # 3. Advance 'prev' to 'curr'
        curr = temp_next  # 4. Advance 'curr' to 'temp_next' (the next node)
        # After the loop:
        # - 'prev' is the new head of the reversed sublist (e.g., node 4)
        # - 'curr' is the node immediately following the reversed sublist (e.g., node 5)
        # 3 & 4. Re-stitch the list
        # Connect the end of the reversed sublist (the original tail, e.g., node 2)
        # to the rest of the original list (e.g., node 5).
    sublist_tail.next = curr
        # Connect the main list before the sublist (e.g., node 1)
        # to the new head of the reversed sublist (e.g., node 4).
    node_before_start.next = prev
    return dummy.next
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


#Testing
llist = LinkedList()
# llist.append("A")
# llist.append("B")
# llist.append("C")
# llist.prepend("D")
llist.append(1)
llist.append(2)
llist.append(3)
llist.append(4)
llist.append(5)
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
# print(insertion_recursion(23,llist,4))
llist.print_list()
reverseBetween(llist.head,2,4)
llist.print_list()