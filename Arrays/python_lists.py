# ----------------------
# Two Sum - Naive O(n^2)
# ----------------------
def two_sum(arr, target):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                return [i, j]
    return -1

def twoSum_with_hashmap(nums, target):
    mp = {}  # value -> index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in mp:
            return [mp[complement], i]
        mp[num] = i
    return []
nums = [2, 7, 11, 15]
target = 9
print(twoSum_with_hashmap(nums, target))  # Output: [0, 1]

# ----------------------
# Two Sum - Better O(n log n)
# ----------------------
def two_sum_better(arr, target):
    if not arr:
        return []

    arr2 = arr[:]  # original array copy
    arr.sort()

    st, end = 0, len(arr) - 1
    result = [-1, -1]

    while st < end:
        s = arr[st] + arr[end]
        if s == target:
            result = [arr[st], arr[end]]
            break
        elif s > target:
            end -= 1
        else:
            st += 1

    # Map values back to indices in original array
    end_result = [-1, -1]
    found = 0
    for i in range(len(arr2)):
        if arr2[i] == result[0] and end_result[0] == -1:
            end_result[0] = i
            found += 1
        elif arr2[i] == result[1] and end_result[1] == -1:
            end_result[1] = i
            found += 1
        if found == 2:
            break

    return end_result


# ----------------------
# Missing and Repeating
# ----------------------
def missing_and_repeating_values(arr):
    flat_list = [val for row in arr for val in row]

    seen = set()
    repeating = -1
    for val in flat_list:
        if val in seen:
            repeating = val
        seen.add(val)

    actual_sum = sum(seen) + repeating
    n = len(flat_list)
    expected_sum = (n * (n + 1)) // 2
    missing = expected_sum + repeating - actual_sum

    print("Flattened:", flat_list)
    print("Repeating:", repeating)
    print("Missing:", missing)


# ----------------------
# Binary Search
# ----------------------
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


# ----------------------
# Binary Search in Rotated Sorted Array
# ----------------------
def binary_search_in_rotated_array(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        if arr[left] <= arr[mid]:
            if arr[left] <= target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if arr[mid] < target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1


# ----------------------
# Merge Sort (Fixed)
# ----------------------
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def merge(left, right):
    i = j = 0
    arr = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr.append(left[i])
            i += 1
        else:
            arr.append(right[j])
            j += 1
    arr.extend(left[i:])
    arr.extend(right[j:])
    return arr


# ----------------------
# Testing
# ----------------------
print("Naive two sum:", two_sum([1, 2, 3, 4, 5], 3))
print("Better two sum:", two_sum_better([1, 2, 3, 4, 5], 3))
print("Rotated binary search:", binary_search_in_rotated_array([3,4,5,6,7,0,1,2], 0))
print("Merge Sort:", merge_sort([19, 33, 44, -98, 0, 1, 2, 3]))
missing_and_repeating_values([[9,1,7],[8,9,2],[3,4,6]])
