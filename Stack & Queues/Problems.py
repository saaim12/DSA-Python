#Q1: valid parenthesis problem
def check_brackets(brackets):
    stack = []
    for ch in brackets:
        if ch in '{([':
            stack.append(ch)
        elif ch in '})]':
            if not stack:
                return False
            top=stack.pop()
            if (ch=='}' and top!='{' ) or (ch==')' and top!='(' ) or (ch==']' and top!='[' ):
                return False



    return len(stack)==0
print(check_brackets("{{}"))

#Q2 : next greater element
def next_greater_element(arr):
    res=[-1]*len(arr)
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[j]>arr[i]:
                res[i]=arr[j]
                break

    return res

print(next_greater_element([2, 1, 3, 0, 5]))
