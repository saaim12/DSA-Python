import math
from platform import version


# -------------------------------
# 1️⃣ Single element in sorted array
# -------------------------------
def single_element_in_sorted_arr(arr):
    n = len(arr)
    if n == 1:
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

print("Single element:", single_element_in_sorted_arr([1,1,2,3,3,4,4,8,8]))

# -------------------------------
# 2️⃣ Peak index in mountain array
# -------------------------------
def peakIndexInMountainArray(arr):
    n = len(arr)
    if n == 1:
        return arr[0]
    if arr[0] > arr[1]:
        return arr[0]
    if arr[n - 1] > arr[n - 2]:
        return arr[n - 1]

    left, right = 0, n - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid - 1] < arr[mid] > arr[mid + 1]:
            return mid
        if arr[mid] < arr[mid + 1]:
            left = mid + 1
        else:
            right = mid - 1
    return -1

print("Peak index:", peakIndexInMountainArray([18,29,38,59,98,100,99,98,90]))

# -------------------------------
# 3️⃣ Square root
# -------------------------------
def mySqrt(x):
    if x == 0:
        return 0
    l, h = 1, x
    ans = 0
    while l <= h:
        m = (l + h) // 2
        if m * m == x:
            return m
        if m * m < x:
            ans = m
            l = m + 1
        else:
            h = m - 1
    return ans

print("Sqrt:", mySqrt(28))

# -------------------------------
# 4️⃣ Nth root of integer
# -------------------------------
def nth_root_of_integer(num, n):
    def find_val(base, times):
        result = 1
        for _ in range(times):
            result *= base
        return result

    if num == 0:
        return 0

    l, h = 1, num
    ans = -1
    while l <= h:
        mid = (l + h) // 2
        val = find_val(mid, n)

        if val == num:
            return mid
        elif val < num:
            l = mid + 1
        else:
            h = mid - 1

    return ans

# Functional tests
tests = [
    (27, 3, 3),
    (64, 3, 4),
    (32, 5, 2),
    (100, 3, -1),
    (10, 2, -1),
    (81, 4, 3),
    (1, 7, 1),
    (0, 5, 0),
    (125, 3, 5),
]

for x, n, expected in tests:
    result = nth_root_of_integer(x, n)
    print(f"nth_root({x}, {n}) = {result}, expected = {expected}")

# -------------------------------
# 5️⃣ Koko Eating Bananas
# -------------------------------
def koko_eating_bananas(piles, hr_max):
    def check(arr, speed):
        total_hrs = 0
        for pile in arr:
            total_hrs += math.ceil(pile / speed)
        return total_hrs

    l, h = 1, max(piles)
    while l <= h:
        mid = (l + h) // 2
        if check(piles, mid) > hr_max:
            l = mid + 1
        else:
            h = mid - 1
    return l

print("Koko:", koko_eating_bananas([3,6,7,11], 8))
print("Koko:", koko_eating_bananas([30,11,23,4,20],5))
print("Koko:", koko_eating_bananas([30,11,23,4,20],6))

# -------------------------------
# 6️⃣ Min Days to Make M Bouquets
# -------------------------------
def minDays(bloomDay, m, k):
    if len(bloomDay) < m * k:
        return -1

    def possible(arr, day, m, k):
        counter = 0
        bouquets = 0
        for val in arr:
            if val <= day:
                counter += 1
            else:
                bouquets += counter // k
                counter = 0
        bouquets += counter // k
        return bouquets >= m

    l, h = 1, max(bloomDay)
    ans = -1
    while l <= h:
        mid = (l + h) // 2
        if possible(bloomDay, mid, m, k):
            ans = mid
            h = mid - 1
        else:
            l = mid + 1
    return ans

print("Min Days:", minDays([1,10,3,10,2], 3, 1))

# -------------------------------
# 7️⃣ Smallest Divisor
# -------------------------------
def smallestDivisor(nums, threshold):
    def check(arr, divisor):
        total = 0
        for val in arr:
            total += (val + divisor - 1) // divisor
        return total

    l, h = 1, max(nums)
    ans = h
    while l <= h:
        mid = (l + h) // 2
        val = check(nums, mid)
        if val <= threshold:
            ans = mid
            h = mid - 1
        else:
            l = mid + 1
    return ans

print("Smallest Divisor:", smallestDivisor([1,2,5,9], 6))

# -------------------------------
# 8️⃣ Ship Within Days
# -------------------------------
def shipWithinDays(weights, days):
    def check(arr, capacity):
        current_sum = 0
        day = 1
        for w in arr:
            if current_sum + w > capacity:
                day += 1
                current_sum = 0
            current_sum += w
        return day <= days

    l, h = max(weights), sum(weights)
    ans = -1
    while l <= h:
        mid = (l + h) // 2
        if check(weights, mid):
            ans = mid
            h = mid - 1
        else:
            l = mid + 1
    return ans

print("Ship Within Days:", shipWithinDays([1,2,3,4,5,6,7,8,9,10], 5))


def findKthPositive(arr, k):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        missing = arr[mid] - (mid + 1)

        if missing < k:
            left = mid + 1
        else:
            right = mid - 1

    # After binary search, left = number of elements in arr where missing < k
    return left + k

def aggressiveCows(stalls, k):
    stalls.sort()
    def can_we_place(arr, cows,dist):
        cut_cows=1
        last=arr[0]
        for i in range(1,len(arr)):
            if arr[i]-last>=dist:
                cut_cows+=1
                last=arr[i]
        return True if cut_cows>=cows else False

    l=1
    h = stalls[-1] - stalls[0]
    ans=-1
    while l<=h:
        mid=(l+h)//2
        if can_we_place(stalls,k,mid):
            ans=mid
            h=mid-1
        else:
            l=mid+1

    return ans


def findPages(arr, k):
    if k>len(arr):
        return-1
    l=max(arr)
    h=sum(arr)
    def allocation(no_of_pages):
        student=1
        curr_sum=0
        for i in range(len(arr)):
            if curr_sum+arr[i]<=no_of_pages:
                curr_sum+=arr[i]
            else:
                student+=1
                curr_sum=arr[i]
            if student>k:
                return False
        return True
    ans=-1
    while l <= h:
        mid = (l + h) // 2
        if allocation(mid):
            ans = mid
            h = mid - 1
        else:
            l = mid + 1

    return ans

def painters_partition(arr, k):
    # Helper function to check if we can paint all boards with max length limit `mid`
    def is_possible(arr, k, max_len):
        painters = 1
        current_sum = 0

        for length in arr:
            if length > max_len:  # single board longer than max_len -> impossible
                return False
            if current_sum + length <= max_len:
                current_sum += length
            else:
                painters += 1
                current_sum = length
        return painters <= k

    # Binary search to find minimum time
    low = max(arr)       # at least one board's length
    high = sum(arr)      # at most all boards together
    result = high

    while low <= high:
        mid = (low + high) // 2
        if is_possible(arr, k, mid):
            result = mid
            high = mid - 1
        else:
            low = mid + 1

    return result


# Example usage:
boards = [10, 20, 30, 40]
painters = 2
print(painters_partition(boards, painters))  # Output: 60



### median of two sorted array  this is brute force
def median_OF_two_arrs(arr1, arr2):
    arr3 = []
    i, j = 0, 0

    # merge both arrays
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            arr3.append(arr1[i])
            i += 1
        else:
            arr3.append(arr2[j])
            j += 1

    # add remaining elements
    while i < len(arr1):
        arr3.append(arr1[i])
        i += 1

    while j < len(arr2):
        arr3.append(arr2[j])
        j += 1

    print("Merged:", arr3)

    n = len(arr3)

    # compute median
    if n % 2 == 1:
        # odd length → middle element
        median = arr3[n // 2]
    else:
        # even length → average of two middle elements
        median = (arr3[n//2] + arr3[n//2 - 1]) / 2

    print("Median:", median)
    return median

print(median_OF_two_arrs([1,3,4,7,10,12],[2,3,6,15]))
print(median_OF_two_arrs([2,3,4],[1,3]))


## find max ones
def rowAndMaximumOnes(mat):
    idx, max_ones = 0, 0
    for i, row in enumerate(mat):
        curr_sum = sum(row)
        if curr_sum > max_ones:
            idx = i
            max_ones = curr_sum

    return [idx, max_ones]


def row_and_max_ones_optimized(arr):
    def lower_bound(arr,x):
        l=0
        h=len(arr)-1
        ans=len(arr)
        while l<=h:
            mid=(l+h)//2
            if arr[mid]>=x:
                ans=mid
                h=mid-1
            else:
                l=mid+1

        return ans
    cols=len(arr[0])
    max_no=-1
    for i,row in enumerate(arr):
        curr_no=lower_bound(row,1)
        curr_no=cols-curr_no
        if curr_no>max_no:
            idx=i
            max_no=curr_no

    return [idx,max_no]




mat = [
    [0,0,1,1],
    [0,1,1,1],
    [0,0,0,1]
]

print(row_and_max_ones_optimized(mat))

## search in a 2D matrix
def search(arr, target):
    if not arr or not arr[0]:
        return -1

    row = 0
    col = len(arr[0]) - 1

    while row < len(arr) and col >= 0:
        if arr[row][col] == target:
            return [row, col]
        elif target > arr[row][col]:
            row += 1
        else:
            col -= 1

    return -1

matrix = [
    [1, 4, 7, 11],
    [2, 5, 8, 12],
    [3, 6, 9, 16]
]

print(search(matrix, 5))  # Output: [1, 1]
print(search(matrix, 10)) # Output: -1
def findPeakGrid(mat):
    max_val=float('-inf')
    pos = [-1, -1]

    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] > max_val:
                max_val = mat[i][j]
                pos = [i, j]

    return pos

print(findPeakGrid([[10,20,15],[21,30,14],[7,16,32]]))

###optimized version
def find_peak_grid_2(mat):
    rows = len(mat)
    cols = len(mat[0])
    left, right = 0, cols - 1

    while left <= right:
        mid_col = (left + right) // 2

        # Find row with max in mid_col
        max_row = 0
        for r in range(rows):
            if mat[r][mid_col] > mat[max_row][mid_col]:
                max_row = r

        # Left and right neighbors
        left_element = mat[max_row][mid_col - 1] if mid_col - 1 >= 0 else float('-inf')
        right_element = mat[max_row][mid_col + 1] if mid_col + 1 < cols else float('-inf')

        # Check if peak
        if mat[max_row][mid_col] >= left_element and mat[max_row][mid_col] >= right_element:
            return [max_row, mid_col], mat[max_row][mid_col]
        elif left_element > mat[max_row][mid_col]:
            right = mid_col - 1
        else:
            left = mid_col + 1

    return -1




















