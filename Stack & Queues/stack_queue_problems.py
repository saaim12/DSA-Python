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
def next_greater_element_optimized(arr):
    res=[-1]*len(arr)
    stack=[]
    for i in range(len(arr)-1,-1,-1):
        element=arr[i]
        while stack and stack[-1] <=element:
            stack.pop()
        if stack:
            res[i]=stack[-1]
        stack.append(element)

    return res
print(next_greater_element_optimized([2, 1, 5, 3, 4]))
def next_smaller_element(arr):
    res=[-1]*len(arr)
    stack = []
    for i in range(len(arr) - 1, -1, -1):
        element = arr[i]
        while stack and stack[-1] >= element:
            stack.pop()
        if stack:
            res[i] = stack[-1]
        stack.append(element)

    return res
print(next_smaller_element([4, 8, 5, 2, 25]))
def next_greater_element_circular(nums):
    n = len(nums)
    res = [-1] * n
    stack = []

    for i in range(2 * n):
        curr = nums[i % n]
        while stack and nums[stack[-1]] < curr:
            res[stack.pop()] = curr
        if i < n:
            stack.append(i)

    return res
print(next_greater_element_circular([1,2,1]))
def previous_smaller_element(arr):
    res=[-1]*len(arr)
    stack=[]
    for i in range(len(arr)):
        element=arr[i]
        while stack and stack[-1]>=element:
            stack.pop()
        if stack:
            res[i]=stack[-1]
        stack.append(element)

    return res

print(previous_smaller_element([4,5,2,10,9]))


def largestRectangleArea(heights):
    stack = []  # stores indices
    max_area = 0
    n = len(heights)

    for i in range(n + 1):  # +1 adds a virtual 0 height
        curr_height = heights[i] if i < n else 0

        while stack and curr_height < heights[stack[-1]]:
            h = heights[stack.pop()]
            w = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, h * w)

        stack.append(i)

    return max_area
print(largestRectangleArea([2,1,5,6,2,3]))