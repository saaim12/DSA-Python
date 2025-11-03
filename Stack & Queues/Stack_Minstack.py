class Stack:
    def __init__(self):
        self.stack=[]
        self.minStack=[]
        self.size=0

    def push(self,val):
        self.stack.append(val)
        if not self.minStack or self.minStack[-1] >= val:
            self.minStack.append(val)
        self.size+=1

    def pop(self):
        if not self.stack:
            return -1
        val=self.stack[-1]
        self.size-=1
        if self.minStack and  self.minStack[-1]==val:
            self.minStack.pop()
        return self.stack.pop()

    def get_size(self):
        return self.size

    def top(self):
        return self.stack[-1]
    def get_min(self):
        return self.minStack[-1] if self.minStack else -1





s = Stack()
s.push(5)
s.push(3)
s.push(7)

# current minStack = [5, 3]

print(s.pop())
s.pop()
s.pop()
print(s.get_min())
