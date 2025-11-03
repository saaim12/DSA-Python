# first implementing queue
class Queue:
    def __init__(self):
        self.q=[]
        self.size=0

    def push(self,val):
        self.q.append(val)
        self.size+=1

    def pop(self):
        if self.q:
            self.size-=1
            return self.q.pop(0)
        else :
            return None

    def get_size(self):
        return self.size

    def front(self):
        return self.q[0] if self.q else None

    def isEmpty(self):
        return len(self.q)==0

class Stack_using_Queue:
    def __init__(self):
        self.q1=Queue()
        self.q2=Queue()
        self.size=0

    def push(self,val):
        self.q1.push(val)
        self.size+=1

    def pop(self):
        if self.q1.isEmpty():
            print("Stack is empty")
            return None
        while self.q1.size>1:
            self.q2.push(self.q1.pop())

        # now only last element remaining
        val=self.q1.pop()
        # now q1 is empty
        self.size-=1
        self.q1,self.q2=self.q2,self.q1
        return val
    def top(self):
        if self.q1.isEmpty():
            print("stack is empty")
            return None
        while self.q1.size>1:
            self.q2.push(self.q1.pop())

        top_element=self.q1.pop()
        self.q2.push(top_element)
        self.q1, self.q2 = self.q2, self.q1
        return top_element

    def get_size(self):
        return self.size

    def isEmpty(self):
        return self.size == 0


s = Stack_using_Queue()
s.push(10)
s.push(20)
s.push(30)

print("Top element:", s.top())     # ➜ 30
print("Pop:", s.pop())             # ➜ 30
print("Pop:", s.pop())             # ➜ 20
print("Top element:", s.top())     # ➜ 10
print("Is empty:", s.isEmpty())    # ➜ False
print("Pop:", s.pop())             # ➜ 10
print("Is empty:", s.isEmpty())    # ➜ True
s.pop()






