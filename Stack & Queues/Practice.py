# Q1 : next greater element
import collections


def next_greater_element(arr):
    n=len(arr)
    res=[-1]*n
    stack=[]
    for i in range(n-1,-1,-1):
        element=arr[i]
        while stack and element>=stack[-1]:
            stack.pop()
        if stack:
            res[i]=stack[-1]
        stack.append(arr[i])

    return res

print(next_greater_element([2,10,12,1,11]))

#Q2 : circular Queue O(n^2)
def next_greater_element_circular(arr):
    n=len(arr)
    res=[-1]*n
    for i in range(n):
        for j in range(i+1,i+n):
            idx=j%n
            if arr[idx]>arr[i]:
                res[i]=arr[idx]
                break

    return res
print(next_greater_element_circular([2,10,12,1,11]))
#Q2 : circular Queue O(n)
def next_greater_element_circular_optimized(arr):
    n=len(arr)
    res=[-1]*n
    stack=[]
    for i in range(2*n-1,-1,-1):
        element=arr[i%n]
        while stack and stack[-1]<=element:
            stack.pop()
        if stack:
            if i<n:
               res[i]=stack[-1]
        stack.append(element)

    return res
print(next_greater_element_circular_optimized([2,10,12,1,11]))

#Q4: previous smaller elements
def prev_smaller_element(arr):
    n=len(arr)
    res=[-1]*n
    stack=[]
    for i in range(n):
        element=arr[i]
        while stack and stack[-1]>=element:
            stack.pop()
        if stack:
            res[i]=stack[-1]
        stack.append(arr[i])

    return res

print(prev_smaller_element([1,2,3,4]))

# Q5: trapping rain water
def trapping_rain_water(arr):
    n = len(arr)
    # Step 1: Precompute left max (prefixes)
    left_max = [0] * n
    left_max[0] = arr[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], arr[i])

    # Step 2: Precompute right max (suffixes)
    right_max = [0] * n
    right_max[n - 1] = arr[n - 1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], arr[i])

    print("Left Max:", left_max)
    print("Right Max:", right_max)
    total=0
    for i in range(n):
        if arr[i]<left_max[i] and arr[i]<right_max[i]:
            total+=min(left_max[i],right_max[i])-arr[i]
    return total

print(trapping_rain_water([4,2,0,3,2,5]))

# Q5 trapping rain water optimized
def trapping_rain_water_optimized(arr):
    n = len(arr)
    left=0
    right=n-1
    rightmax=0
    leftmax=0
    total=0
    while left<right:
        if arr[left]<arr[right]:
            if arr[left]>leftmax:
                leftmax=arr[left]
            else:
                total+=leftmax-arr[left]
            left+=1
        else:
            if arr[right]>rightmax:
                rightmax=arr[right]
            else:
                total+=rightmax-arr[right]
            right-=1
    return total
print(trapping_rain_water_optimized([4,2,0,3,2,5]))
# Q6 sliding window maximum
def slidingwindow(arr,k):
    res=[]
    n=len(arr)
    max_=0
    for i in range(n-k+1):
        for j in range(i,i+k):
            max_=max(max_,arr[j])

        res.append(max_)
    return res

print(slidingwindow([1,3,-1,-3,5,3,6,7],3))
#Q6 sliding window optimized
def sliding_window_optimized(arr,k):
    res=[]
    q=collections.deque()
    for i in range(len(arr)):
        if q and q[0]==i-k:
            q.popleft()
        while q and arr[q[-1]]<arr[i]:
            q.pop()

        q.append(i)

        if i>=k-1:
            res.append(arr[q[0]])

    return res

print(sliding_window_optimized([1,3,-1,-3,5,3,6,7],3))


