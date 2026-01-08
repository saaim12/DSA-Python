class Queue:
    def __init__(self):
        self.queue = []
        self.min_queue = []
        self.size = 0

    def push(self, val):
        self.queue.append(val)

        # Maintain increasing order in min_queue
        while self.min_queue and self.min_queue[-1] > val:
            self.min_queue.pop()

        self.min_queue.append(val)
        self.size += 1

    def pop(self):
        if not self.queue:
            return None

        val = self.queue.pop(0)
        self.size -= 1

        # If the popped value is also the current minimum, remove it
        if self.min_queue and self.min_queue[0] == val:
            self.min_queue.pop(0)

        return val

    def front(self):
        return self.queue[0] if self.queue else None

    def get_min(self):
        return self.min_queue[0] if self.min_queue else None

    def isEmpty(self):
        return len(self.queue) == 0

    def size_q(self):
        return self.size


# -----------------------------
# Testing
# -----------------------------

q = Queue()
q.push(5)
q.push(3)
q.push(7)
q.push(2)

print("Queue:", q.queue)
print("Current Min:", q.get_min())  # 2

print("Pop:", q.pop())              # removes 5
print("Queue after pop:", q.queue)
print("Front element:", q.front())  # 3
print("Current Min:", q.get_min())  # 2

q.pop()  # remove 3
q.pop()  # remove 7
print("Queue before removing last element:", q.queue)
print("Current Min:", q.get_min())  # 2

q.pop()  # remove 2
print("Queue empty:", q.isEmpty())  # True
print("Min after empty:", q.get_min())  # None

q.push(10)
q.push(9)
q.push(8)
print("\nQueue after re-adding:", q.queue)
print("Current Min:", q.get_min())  # 8
