class Stack():
    def __init__(self):
        # onmaking object it will have an empty stack
        self.items=[]

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def isEmpty(self):
        return self.items==[]

    def getstack(self):
        return self.items