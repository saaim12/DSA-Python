import collections

q=collections.deque()
q.append(1)
q.append(23)
q.append(23)
q.append(23)
print(q)
print(q.pop())
print(q.popleft())