class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Queue:
    def __init__(self):
        self.head = None   # front
        self.tail = None   # rear
        self.size = 0

    def push(self, val):
        """Insert (enqueue) element at the end of the queue"""
        new_node = Node(val)
        if self.head is None:
            # First element
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def pop(self):
        """Remove (dequeue) element from the front"""
        if self.head is None:
            print("Queue is empty")
            return None
        popped_val = self.head.val
        self.head = self.head.next
        if self.head is None:
            # If queue becomes empty, reset tail
            self.tail = None
        self.size -= 1
        return popped_val

    def front(self):
        """Get the element at the front"""
        return self.head.val if self.head else None

    def get_size(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def display(self):
        """Display all elements in queue order"""
        temp = self.head
        if not temp:
            print("Queue is empty")
            return
        print("Queue (front → rear):", end=" ")
        while temp:
            print(temp.val, end=" ")
            temp = temp.next
        print()


# -------------------------------
# ✅ TEST CASES
# -------------------------------
q = Queue()
q.push(0)
q.push(1)
q.push(2)

q.display()                 # ➜ Queue (front → rear): 0 1 2
print("Front:", q.front())  # ➜ 0
print("Size:", q.get_size())  # ➜ 3

print("Pop:", q.pop())      # ➜ removes 0
q.display()                 # ➜ 1 2
print("Front:", q.front())  # ➜ 1

q.pop()
q.pop()
q.display()                 # ➜ Queue is empty
print("Pop from empty:", q.pop())  # ➜ Queue is empty
print("Empty?", q.isEmpty())       # ➜ True
