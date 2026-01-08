stack = []

# Push elements
stack.append(10)
stack.append(20)
stack.append(30)

print("Stack:", stack)

# Pop element
print("Popped:", stack.pop())

# Peek top element
print("Top:", stack[-1])

# Check if empty
print("Is empty?", len(stack) == 0)
