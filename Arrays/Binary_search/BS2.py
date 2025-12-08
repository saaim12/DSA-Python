def single_element_in_sorted_arr(arr):
    n = len(arr)
    if len(arr) == 1:
        return arr[0]
    if arr[0] != arr[1]:
        return arr[0]
    if arr[n - 1] != arr[n - 2]:
        return arr[n - 1]

    l = 1
    h = n - 2
    while l <= h:
        mid = (l + h) // 2
        if arr[mid] != arr[mid - 1] and arr[mid] != arr[mid + 1]:
            return arr[mid]
        if (mid % 2 == 1 and arr[mid - 1] == arr[mid]) or (mid % 2 == 0 and arr[mid] == arr[mid + 1]):
            l = mid + 1
        else:
            h = mid - 1

    return -1

print(single_element_in_sorted_arr([1,1,2,3,3,4,4,8,8]))


def peakIndexInMountainArray(arr):
    n = len(arr)
    if len(arr) == 1:
        return arr[0]
    if arr[0] > arr[1]:
        return arr[0]
    if arr[n - 1] > arr[n - 2]:
        return arr[n - 1]
    left = 0
    right = len(arr) - 1
    while left <=right:
        mid = left + (right - left) // 2
        if arr[mid - 1] < arr[mid] > arr[mid + 1]:
            return mid
        if arr[mid] < arr[mid + 1]:
            left = mid + 1
        else:
            right = mid - 1

    return -1

print(peakIndexInMountainArray([18,29,38,59,98,100,99,98,90]))
