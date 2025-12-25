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
def rotate_arr_optimal(arr,k):
    n=len(arr)
    k=k%n
    def reverse(l,r):
        while l<r:
            arr[l],arr[r]=arr[r],arr[l]
            l+=1
            r-=1

    reverse(0,k-1)
    reverse(k,n-1)
    reverse(0,n-1)

    return arr


print(rotate_arr_optimal([1,2,3,4,5,6,7],3))
## not optimal
def move_all_zero_to_the_end(arr):
    res=[]
    count=0
    for num in arr:
        if num!=0:
            res.append(num)
        else:
            count+=1

    for i in range(count):
        res.append(0)

    return res

print(move_all_zero_to_the_end([1,0,2,0,3,4,5,0,6,7,0,9,10]))

## optimal
def move_zeros_to_end_optimal(arr):
    j = 0  # position to place next non-zero

    for i in range(len(arr)):
        if arr[i] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1

    return arr

def move_zeros_to_end_optimal_unordered(arr):
    j=len(arr)-1
    i=0
    while i<=j:
        if arr[i]==0:
            arr[j],arr[i]=arr[i],arr[j]
            j-=1
        else:
            i+=1

    return arr


print(move_zeros_to_end_optimal([1,0,2,0,3,4,5,0,6,7,0,9,10]))

print(move_zeros_to_end_optimal_unordered([1,0,2,0,3,4,5,0,6,7,0,9,10]))

def max_consecutive_ones(arr):
    count=0
    max_count=0
    for num in arr:
        if num==1:
            count+=1
        else:
            max_count=max(max_count,count)
            count=0
    max_count=max(count,max_count)
    return max_count

print(max_consecutive_ones([1,2,1,1,1,1,0,0,2,3,4,1,1,1,1,1,1,1]))

