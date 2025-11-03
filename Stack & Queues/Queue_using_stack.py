class Stack:
    def __init__(self):
        self.stack = []
        self.size = 0

    def push(self, val):
        self.stack.append(val)
        self.size += 1

    def pop(self):
        if self.stack:
            self.size -= 1
            return self.stack.pop()
        return None

    def top(self):
        return self.stack[-1] if self.stack else None

    def get_size(self):
        return self.size

    def isEmpty(self):
        return len(self.stack) == 0


class Queue_using_stack:
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()
        self.size = 0

    def push(self, val):
        self.s1.push(val)
        self.size += 1

    def pop(self):
        if self.s1.isEmpty() and self.s2.isEmpty():
            print("Queue is empty")
            return None

        # Move all elements from s1 to s2 if s2 is empty
        if self.s2.isEmpty():
            while not self.s1.isEmpty():
                self.s2.push(self.s1.pop())

        self.size -= 1
        return self.s2.pop()

    def front(self):
        if self.s1.isEmpty() and self.s2.isEmpty():
            print("Queue is empty")
            return None

        if self.s2.isEmpty():
            while not self.s1.isEmpty():
                self.s2.push(self.s1.pop())

        return self.s2.top()

    def get_size(self):
        return self.size

    def isEmpty(self):
        return self.size == 0


# ✅ Test
q = Queue_using_stack()
q.push(10)
q.push(20)
q.push(30)

print("Front element:", q.front())  # ➜ 10
print("Pop:", q.pop())              # ➜ 10
print("Front element:", q.front())  # ➜ 20
q.push(40)
print("Pop:", q.pop())              # ➜ 20
print("Pop:", q.pop())              # ➜ 30
print("Pop:", q.pop())              # ➜ 40
print("Queue empty:", q.isEmpty())  # ➜ True
