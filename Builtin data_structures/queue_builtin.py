from collections import deque

queue = deque()

# Enqueue elements
queue.append(10)
queue.append(20)
queue.append(30)

print("Queue:", queue)

# Dequeue element
print("Dequeued:", queue.popleft())

# Peek front element
print("Front:", queue[0])

# Check if empty
print("Is empty?", len(queue) == 0)
