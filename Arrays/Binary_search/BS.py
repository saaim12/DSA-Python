# =====================================================================
#                    BINARY SEARCH COMPLETE CHEATSHEET
# =====================================================================
# All functions are cleaned, commented, and organized.
# All your test cases are included at the bottom.
# =====================================================================


# -----------------------------------------------------
# 1. BASIC BINARY SEARCH (ITERATIVE)
# -----------------------------------------------------
def binary_search(arr, target):
    l = 0
    r = len(arr) - 1

    while l <= r:
        mid = (l + r) // 2

        if arr[mid] == target:
            return mid
        elif target > arr[mid]:
            l = mid + 1
        else:
            r = mid - 1

    return -1


# -----------------------------------------------------
# 2. BASIC BINARY SEARCH (RECURSIVE)
# -----------------------------------------------------
def binary_search_recursive(arr, l, h, target):
    if l > h:
        return -1

    mid = (l + h) // 2

    if arr[mid] == target:
        return mid
    elif target > arr[mid]:
        return binary_search_recursive(arr, mid + 1, h, target)
    else:
        return binary_search_recursive(arr, l, mid - 1, target)


# -----------------------------------------------------
# 3. LOWER BOUND: first index >= target
# -----------------------------------------------------
def lower_bound(arr, target):
    l, h = 0, len(arr) - 1
    ans = len(arr)

    while l <= h:
        mid = (l + h) // 2

        if arr[mid] >= target:
            ans = mid
            h = mid - 1
        else:
            l = mid + 1

    return ans


# -----------------------------------------------------
# 4. UPPER BOUND: first index > target
# -----------------------------------------------------
def upperBound(arr, target):
    l, h = 0, len(arr) - 1
    ans = len(arr)

    while l <= h:
        mid = (l + h) // 2

        if arr[mid] > target:
            ans = mid
            h = mid - 1
        else:
            l = mid + 1

    return ans


# -----------------------------------------------------
# 5. Search Insert Position (LC35) --> lower_bound logic
# -----------------------------------------------------
def searchInsert(arr, target):
    l, h = 0, len(arr) - 1
    ans = len(arr)

    while l <= h:
        mid = (l + h) // 2

        if arr[mid] >= target:
            ans = mid
            h = mid - 1
        else:
            l = mid + 1

    return ans


# -----------------------------------------------------
# 6. Ceil (first element > target), Floor (largest < target)
# -----------------------------------------------------
def find_ceil(arr, target):
    l, h = 0, len(arr) - 1
    ans = len(arr)

    while l <= h:
        mid = (l + h) // 2

        if arr[mid] > target:
            ans = mid
            h = mid - 1
        else:
            l = mid + 1

    return ans


def find_floor(arr, target):
    l, h = 0, len(arr) - 1
    ans = -1  # valid floor index

    while l <= h:
        mid = (l + h) // 2

        if arr[mid] < target:
            ans = mid
            l = mid + 1
        else:
            h = mid - 1

    return ans


# -----------------------------------------------------
# 7. First & Last occurrence (Linear)
# -----------------------------------------------------
def first_and_last_occourance_of_element_in_array_linearly(arr, target):
    first = -1
    last = -1

    for i in range(len(arr)):
        if arr[i] == target:
            if first == -1:
                first = i
            last = i

    return first, last


# -----------------------------------------------------
# 8. First & Last occurrence using lower/upper bounds
# -----------------------------------------------------
def searchRange(nums, target):

    def lower_bound(arr, target):
        l, h = 0, len(arr) - 1
        ans = len(arr)
        while l <= h:
            mid = (l + h) // 2
            if arr[mid] >= target:
                ans = mid
                h = mid - 1
            else:
                l = mid + 1
        return ans

    def upper_bound(arr, target):
        l, h = 0, len(arr) - 1
        ans = len(arr)
        while l <= h:
            mid = (l + h) // 2
            if arr[mid] > target:
                ans = mid
                h = mid - 1
            else:
                l = mid + 1
        return ans

    first = lower_bound(nums, target)

    # Target does NOT exist
    if first == len(nums) or nums[first] != target:
        return [-1, -1]

    last = upper_bound(nums, target) - 1
    return [first, last]


# -----------------------------------------------------
# 9. First & Last occurrence using plain binary search twice
# -----------------------------------------------------
def searchRange_with_plain_binary_search(nums, target):

    def binary_search_in(arr, target, is_first):
        l, h = 0, len(arr) - 1
        ans = -1

        while l <= h:
            mid = (l + h) // 2
            if arr[mid] == target:
                ans = mid
                if is_first:
                    h = mid - 1
                else:
                    l = mid + 1
            elif target < arr[mid]:
                h = mid - 1
            else:
                l = mid + 1

        return ans

    first = binary_search_in(nums, target, True)
    last = binary_search_in(nums, target, False)
    return [first, last]


# -----------------------------------------------------
# 10. Search in Rotated Sorted Array (No duplicates)
# -----------------------------------------------------
def search_in_rotated_array(arr, target):
    l, h = 0, len(arr) - 1

    while l <= h:
        mid = (l + h) // 2

        if arr[mid] == target:
            return mid

        # Left half sorted
        if arr[l] <= arr[mid]:
            if arr[l] <= target <= arr[mid]:
                h = mid - 1
            else:
                l = mid + 1

        # Right half sorted
        else:
            if arr[mid] <= target <= arr[h]:
                l = mid + 1
            else:
                h = mid - 1

    return -1


# -----------------------------------------------------
# 11. Search in Rotated Array WITH duplicates
# -----------------------------------------------------
def search(arr, target):
    l, h = 0, len(arr) - 1

    while l <= h:
        mid = (l + h) // 2

        if arr[mid] == target:
            return True

        # Duplicates destroy logic
        if arr[l] == arr[mid] == arr[h]:
            l += 1
            h -= 1
            continue

        # Left part sorted
        if arr[l] <= arr[mid]:
            if arr[l] <= target < arr[mid]:
                h = mid - 1
            else:
                l = mid + 1

        # Right part sorted
        else:
            if arr[mid] < target <= arr[h]:
                l = mid + 1
            else:
                h = mid - 1

    return False


# -----------------------------------------------------
# 12. Find Minimum element in Rotated Sorted Array
# -----------------------------------------------------
def findMin(arr):
    l, h = 0, len(arr) - 1
    ans = float('inf')

    while l <= h:
        mid = (l + h) // 2

        # Left half sorted
        if arr[l] <= arr[mid]:
            ans = min(ans, arr[l])
            l = mid + 1
        else:
            ans = min(ans, arr[mid])
            h = mid - 1

    return ans


# -----------------------------------------------------
# 13. Find rotation count (index of minimum)
# -----------------------------------------------------
def find_how_many_times_arr_is_rotated(arr):
    l, h = 0, len(arr) - 1
    ans = float('inf')
    idx = 0

    while l <= h:
        mid = (l + h) // 2

        # Left part sorted
        if arr[l] <= arr[mid]:
            if arr[l] < ans:
                ans = arr[l]
                idx = l
            l = mid + 1

        # Right part unsorted
        else:
            if arr[mid] < ans:
                ans = arr[mid]
                idx = mid
            h = mid - 1

    return idx
### not fully correct
def rotation_count2(arr):
    #find_how_many_times_arr_is_rotated_with_dublicates
    l, h = 0, len(arr) - 1
    ans = float('inf')
    idx = 0

    while l <= h:
        mid = (l + h) // 2
        if arr[l]==arr[mid]==arr[h]:
            l+=1
            h-=1
            continue

        # Left part sorted
        if arr[l] <= arr[mid]:
            if arr[l] < ans:
                ans = arr[l]
                idx = l
            l = mid + 1

        # Right part unsorted
        else:
            if arr[mid] < ans:
                ans = arr[mid]
                idx = mid
            h = mid - 1

    return idx

# =====================================================================
#                           TEST CASES
# =====================================================================

arr = [3, 4, 6, 7, 9, 12, 6, 17]
print(binary_search(arr, 6))

print(binary_search_recursive(arr, 0, len(arr) - 1, 12))

# lower bound tests
print("lower bound tests")
arr2 = [1, 2, 4, 4, 5, 7]
print(lower_bound(arr2, 4))
print(lower_bound(arr2, 3))
print(lower_bound(arr2, 8))

# upper bound tests
print("upper bound tests")
print(upperBound([2, 3, 6, 7, 8, 8, 11, 11, 11, 12], 6))
print(upperBound([2, 3, 6, 7, 8, 8, 11, 11, 11, 12], 11))
print(upperBound([2, 3, 6, 7, 8, 8, 11, 11, 11, 12], 12))
print(upperBound([2, 3, 6, 7, 8, 8, 11, 11, 11, 12], 13))
print(upperBound([2, 3, 6, 7, 8, 8, 11, 11, 11, 12], 0))

# searchInsert
print("searchInsert")
print(searchInsert([1, 3, 5, 6], 2))

# floor / ceil
arr3 = [10, 20, 30, 40, 50]
print("floor and ceil")
print(find_floor(arr3, 25))
print(find_floor(arr3, 30))
print(find_floor(arr3, 50))
print(find_ceil(arr3, 25))
print(find_ceil(arr3, 40))
print(find_ceil(arr3, 50))

# linear first/last
print("linear first/last")
print(first_and_last_occourance_of_element_in_array_linearly([2, 4, 6, 8, 8, 8, 11, 13], 11))
print(first_and_last_occourance_of_element_in_array_linearly([2, 4, 6, 8, 8, 8, 11, 13], 8))
print(first_and_last_occourance_of_element_in_array_linearly([2, 4, 6, 8, 8, 8, 11, 13], 10))

# binary search version
print("linear first/last binary search version")
print(searchRange([5, 7, 7, 8, 8, 10], 8))
print(searchRange([5, 7, 7, 8, 8, 10], 6))
print(searchRange([], 0))

# plain binary search version
print("plain binary search version")
print(searchRange_with_plain_binary_search([5, 7, 7, 8, 8, 10], 8))
print(searchRange_with_plain_binary_search([5, 7, 7, 8, 8, 10], 6))
print(searchRange_with_plain_binary_search([], 0))

# search in rotated array
print("search in rotated array")
print(search_in_rotated_array([4, 5, 6, 7, 0, 1, 2], 0))
print(search_in_rotated_array([4, 5, 6, 7, 0, 1, 2], 3))
print(search_in_rotated_array([], 1))

# find minimum
print("find minimum")
print(findMin([3, 4, 5, 1, 2]))
print(findMin([4, 5, 6, 7, 0, 1, 2]))

# rotation count
print("rotation count")
print(find_how_many_times_arr_is_rotated([3, 4, 5, 1, 2]))
print(rotation_count2([4,5,6,7,0,1,2]))     # 4
print(rotation_count2([3,4,5,1,2]))         # 3
print(rotation_count2([2,2,2,3,4,2]))       # 5 X
print(rotation_count2([10,10,10]))          # 0
print(rotation_count2([1,2,3,4,5]))         # 0
print(rotation_count2([2,1,2,2,2]))         # 1
print(rotation_count2([1,1,1,1,1,0,1]))     # 5 X




