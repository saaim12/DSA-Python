### merge sort with O(n log n) time and space complexity
def merge_sort(arr):
    if len(arr)==1:
        return arr
    mid=len(arr)//2
    left=merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left,right)

def merge(arr1,arr2):
    result=[]
    i=j=0
    while i<len(arr1) and j<len(arr2):
        if arr1[i]< arr2[j]:
            result.append(arr1[i])
            i+=1
        else:
            result.append(arr2[j])
            j+=1

    result.extend(arr1[i:])
    result.extend(arr2[j:])
    return result


print(merge_sort([5,4,3,2,1]))


###### now optimized version ###
##### it does not do log n slices on every point #####
def merge_sort_2(arr, left, right):
    if left >= right:
        return

    mid = (left + right) // 2
    merge_sort_2(arr, left, mid)
    merge_sort_2(arr, mid + 1, right)
    merging(arr, left, mid, right)


def merging(arr, left, mid, right):
    i = left
    j = mid + 1
    temp = []

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1

    while i <= mid:
        temp.append(arr[i])
        i += 1

    while j <= right:
        temp.append(arr[j])
        j += 1

    # Copy back into original array starting at index 'left'
    for k in range(len(temp)):
        arr[left + k] = temp[k]


arr = [5, 4, 3, 2, 1]
merge_sort_2(arr, 0, len(arr) - 1)
print(arr)

def countInversions(arr):
    total_inv=0
    def merge_sort(arr):
        if len(arr) == 1:
            return arr,0
        mid = len(arr) // 2
        left,left_inv = merge_sort(arr[:mid])
        right,right_inv = merge_sort(arr[mid:])
        arr,cross_inv=merge(left, right)

        return arr,cross_inv+left_inv+right_inv

    def merge(arr1, arr2):
        result = []
        i = j = 0
        inv=0
        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                result.append(arr1[i])
                i += 1
            else:
                result.append(arr2[j])
                inv+=len(arr1)-i
                j += 1

        result.extend(arr1[i:])
        result.extend(arr2[j:])
        return result,inv


    sorted_array,total_inv=merge_sort(arr)
    print(sorted_array)
    return total_inv


print(countInversions([5,3,2,4,1]))

