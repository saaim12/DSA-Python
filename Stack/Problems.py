
from Stack import Stack



def check_brackets(brackets):
    mystack = Stack()
    # Dictionary to map closing to opening brackets
    matching = {')': '(', '}': '{', ']': '['}

    for char in brackets:
        if char in '({[':
            mystack.push(char)
        elif char in ')}]':
            if mystack.isEmpty():
                return False
            top = mystack.pop()
            if matching[char] != top:
                return False

    return mystack.isEmpty()

def int_to_binary(num):
    if num == 0:
        return "0"

    mystack = Stack()
    while num > 0:
        mystack.push(str(num % 2))
        num = num // 2

    binary_str = ""
    while not mystack.isEmpty():
        binary_str += mystack.pop()
    return binary_str

print(int_to_binary(28))
print(check_brackets("{{}}"))