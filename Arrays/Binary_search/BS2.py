import math

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
