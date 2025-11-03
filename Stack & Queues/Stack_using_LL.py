class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Stack_LL:
    def __init__(self):
        self.head = None  # top of stack
        self.size = 0

    def push(self, val):
        newn=Node(val)
        newn.next=self.head
        self.head=newn
        self.size+=1

    def pop(self):
        if not self.head:
            print("Stack is empty")
            return None
        popped_val = self.head.val
        self.head = self.head.next
        self.size -= 1
        return popped_val

    def top(self):
        """Peek top element"""
        return self.head.val if self.head else None

    def isEmpty(self):
        return self.head is None

    def get_size(self):
        return self.size

    def display(self):
        """Print current stack from top to bottom"""
        temp = self.head
        res = []
        while temp:
            res.append(temp.val)
            temp = temp.next
        print("Stack (top → bottom):", res)


# -------------------------------
# ✅ TEST CASES
# -------------------------------

s = Stack_LL()
s.push(10)
s.push(20)
s.push(30)

s.display()            # ➜ Stack (top → bottom): [30, 20, 10]
print("Top:", s.top()) # ➜ 30
print("Size:", s.get_size())  # ➜ 3

print("Pop:", s.pop()) # ➜ removes 30
s.display()            # ➜ [20, 10]
print("Top:", s.top()) # ➜ 20

print("Pop:", s.pop()) # ➜ 20
print("Pop:", s.pop()) # ➜ 10
print("Pop from empty:", s.pop())  # ➜ Stack is empty
print("Empty?", s.isEmpty())       # ➜ True
