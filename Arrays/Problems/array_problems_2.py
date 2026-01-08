# Pivot Index using prefix sum
def pivotIndex(nums):
    prefix = [nums[0]]
    for i in range(1, len(nums)):
        prefix.append(prefix[i - 1] + nums[i])
    for i in range(len(nums)):
        left = prefix[i - 1] if i > 0 else 0
        right = prefix[-1] - prefix[i]
        if left == right:
            return i
    return -1

# Optimized pivot index O(n) time, O(1) space
def pivot_index_optimized(arr):
    total = sum(arr)
    left = 0
    for i, num in enumerate(arr):
        if left == total - left - num:
            return i
        left += num
    return -1

# Count subarrays with product less than k
def numSubarrayProductLessThanK(nums, k):
    if k <= 1:  # edge case: no product < 1 is possible
        return 0
    product = 1
    left = 0
    res = 0
    for i in range(len(nums)):
        product *= nums[i]
        while product >= k and left <= i:
            product //= nums[left]
            left += 1
        res += i - left + 1
    return res

# Test function for pivot index
def test_pivot_index():
    test_cases = [
        ([1, 7, 3, 6, 5, 6], 3),
        ([1, 2, 3], -1),
        ([2, 1, -1], 0),
        ([1, -1, 0], 2),
        ([1], 0),
        ([1, 2, 3, 4, 6], -1)
    ]
    print("Testing Pivot Index:")
    for arr, expected in test_cases:
        result1 = pivotIndex(arr)
        result2 = pivot_index_optimized(arr)
        print(f"Array: {arr}")
        print(f"Prefix Sum Result: {result1}, Optimized Result: {result2}, Expected: {expected}")
        print("Pass" if result1 == expected and result2 == expected else "Fail")
        print("-" * 50)

# Test function for subarray product < k
def test_numSubarrayProductLessThanK():
    test_cases = [
        ([10, 5, 2, 6], 100, 8),
        ([1, 2, 3], 0, 0),
        ([1, 2, 3, 4], 10, 7),
        ([1, 1, 1], 2, 6),
        ([10, 5, 2], 50, 4)
    ]
    print("Testing Subarray Product < K:")
    for nums, k, expected in test_cases:
        result = numSubarrayProductLessThanK(nums, k)
        print(f"Array: {nums}, k={k}")
        print(f"Result: {result}, Expected: {expected}")
        print("Pass" if result == expected else "Fail")
        print("-" * 50)

# Run all tests
if __name__ == "__main__":
    test_pivot_index()
    test_numSubarrayProductLessThanK()

