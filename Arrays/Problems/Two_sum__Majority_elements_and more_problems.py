# =========================================================
# Two Sum Implementations
# =========================================================

def two_sum_brute_force(arr, target):
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == target:
                return [i, j]
    return [-1, -1]


def two_sum_optimized(arr, target):
    num_to_index = {}  # number -> index
    for i, num in enumerate(arr):
        diff = target - num
        if diff in num_to_index:
            return [num_to_index[diff], i]
        num_to_index[num] = i
    return [-1, -1]


arr = [2, 7, 11, 15]
target = 9

print("Brute-force result:", two_sum_brute_force(arr, target))
print("Optimized result:", two_sum_optimized(arr, target))


