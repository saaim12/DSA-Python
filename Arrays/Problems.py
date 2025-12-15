###### we can  make Subarrays by O(n^2) Complexity ######
array=[1,2,3]
result=[]
for i in range(len(array)):
    for j in range(i+1,len(array)+1):
        result.append(array[i:j])

print(result)

# first and second and third largest in arr
arr=[5,2,12,34,11,1,9,0,55]
def second_largest(arr):
    if len(arr) < 2:
        return -1  # no second largest exists

    largest = float('-inf')
    second = float('-inf')
    for num in arr:
        if num>largest:
            second=largest
            largest=num
        elif largest>num >second:
            second=num

    return largest,second


print(second_largest(arr = [-10, -20, -30]))


## remove duplicates form sorted array in place
def remove_duplicate(arr):
    if not arr:
        return 0, []

    idx = 0  # index of last unique element

    for i in range(1, len(arr)):
        if arr[i] != arr[idx]:
            idx += 1
            arr[idx] = arr[i]

    # idx + 1 = number of unique elements
    return idx + 1, arr[:idx + 1]


print(remove_duplicate(arr = [1,1,2,2,3,3]))
arr=[1,2,3,4,5]
print("array :: ",arr)
def right_rotate_array_by_K_times(arr,k):
    n=len(arr)
    for j in range(k):
        element=arr[n-1]
        i=n-1
        while i>=0:
            arr[i]=arr[i-1]
            i-=1
        arr[0]=element

    return arr

print("right rotate",right_rotate_array_by_K_times(arr,2))
def left_rotate_array_by_K_times(arr,k):
    n=len(arr)
    for j in range(k):
        element=arr[0]
        i=0
        while i<n-1:
            arr[i]=arr[i+1]
            i+=1
        arr[n-1]=element

    return arr
print("left rotate",left_rotate_array_by_K_times([1,2,3,4,5],2))

### now optimal solution
