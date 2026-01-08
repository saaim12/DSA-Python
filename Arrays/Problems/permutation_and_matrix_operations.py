# =========================================
# Array & Matrix Utility Implementations
# =========================================

# ---------------------------
# Next Permutation Implementations
# ---------------------------

# Brute Force Next Permutation (O(n!*n) time, O(n!*n) space)
def next_permutation_brute_force(arr):
    """
    Generate all permutations using recursion and return all permutations
    and the second permutation as an example.
    """
    res = []

    def permute(arr, path):
        if len(arr) == 0:
            res.append(list(path))
            return
        for i in range(len(arr)):
            path.append(arr[i])
            permute(arr[:i] + arr[i+1:], path)
            path.pop()

    permute(arr, [])
    return res, res[1] if len(res) > 1 else None


# Better Next Permutation (O(n!))
def next_permutation_better(arr):
    """
    Generate all permutations in-place (swapping) to avoid extra slicing.
    """
    res = []

    def permute(idx):
        if idx >= len(arr):
            res.append(arr[:])
            return
        for i in range(idx, len(arr)):
            arr[i], arr[idx] = arr[idx], arr[i]
            permute(idx + 1)
            arr[i], arr[idx] = arr[idx], arr[i]

    permute(0)
    return res, res[1] if len(res) > 1 else None


# ---------------------------
# Longest Consecutive Sequence Implementations
# ---------------------------

# O(n^2) Approach
def longest_consecutive_sequence(arr):
    """
    Find the length of the longest consecutive sequence using O(n^2) approach.
    """
    def exists(x):
        for num in arr:
            if num == x:
                return True
        return False

    if not arr:
        return 0

    max_l = 1
    for i in range(len(arr)):
        count = 1
        num = arr[i]
        while exists(num + 1):
            num += 1
            count += 1
        max_l = max(max_l, count)

    return max_l


# Sorted Array Approach (O(n log n))
def longest_consecutive_sequence_better(arr):
    """
    Sort the array and iterate to find the longest consecutive sequence.
    """
    if not arr:
        return 0

    arr = sorted(arr)
    cnt = 1
    max_l = 1
    last = arr[0]

    for i in range(1, len(arr)):
        if arr[i] == last:
            continue  # skip duplicates
        elif arr[i] == last + 1:
            cnt += 1
        else:
            cnt = 1
        last = arr[i]
        max_l = max(max_l, cnt)

    return max_l


# Optimal O(n) Approach using HashSet
def longest_consecutive_sequence_optimal(arr):
    """
    Use a set to find the start of sequences and expand. O(n) time.
    """
    if not arr:
        return 0

    seen = set(arr)
    max_l = 0

    for num in seen:
        if num - 1 not in seen:  # start of a sequence
            curr = num
            count = 1
            while curr + 1 in seen:
                curr += 1
                count += 1
            max_l = max(max_l, count)

    return max_l


# ---------------------------
# Matrix Zeroing Implementations
# ---------------------------

# Simple O(m*n*(m+n)) Approach
def set_matrix_zero(arr):
    rows = len(arr)
    cols = len(arr[0])
    mark = -1  # temporary marker for cells to be zeroed

    for i in range(rows):
        for j in range(cols):
            if arr[i][j] == 0:
                for k in range(cols):
                    if arr[i][k] != 0:
                        arr[i][k] = mark
                for k in range(rows):
                    if arr[k][j] != 0:
                        arr[k][j] = mark

    # Replace markers with 0
    for i in range(rows):
        for j in range(cols):
            if arr[i][j] == mark:
                arr[i][j] = 0

    return arr


# Better O(m*n) using Sets
def set_matrix_zero_better(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    zero_rows = set()
    zero_cols = set()

    # Collect rows and columns that have zeros
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                zero_rows.add(i)
                zero_cols.add(j)

    # Set cells to zero
    for i in range(rows):
        for j in range(cols):
            if i in zero_rows or j in zero_cols:
                matrix[i][j] = 0

    return matrix


# Most Optimized O(1) Space
def set_matrix_zeroes_more_optimized(matrix):
    """
    Sets entire row and column to 0 if any cell is 0.
    Uses first row and first column as markers to achieve O(1) space.
    """
    rows = len(matrix)
    cols = len(matrix[0])

    # Step 1: Check if the first row or first column originally has any zeros
    first_row_has_zero = any(matrix[0][j] == 0 for j in range(cols))
    first_col_has_zero = any(matrix[i][0] == 0 for i in range(rows))

    # Step 2: Use first row and first column as markers
    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][j] == 0:
                matrix[i][0] = 0  # mark row
                matrix[0][j] = 0  # mark column

    # Step 3: Update inner cells based on markers
    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

    # Step 4: Update first row if it originally had zero
    if first_row_has_zero:
        for j in range(cols):
            matrix[0][j] = 0

    # Step 5: Update first column if it originally had zero
    if first_col_has_zero:
        for i in range(rows):
            matrix[i][0] = 0

    return matrix


# ===========================
# Test Cases
# ===========================

# Next Permutation Tests
print("Next Permutation Brute Force:", next_permutation_brute_force([3, 2, 1]))
print("Next Permutation Better:", next_permutation_better([3, 2, 1]))

    # Longest Consecutive Sequence Tests
test_arrays = [
    [1, 0, 1, 2],
    [0, 3, 7, 2, 5, 8, 4, 6, 0, 1],
    [100, 4, 200, 1, 3, 2]
]

print("\nLongest Consecutive Sequence (O(n^2)):")
for arr in test_arrays:
    print(arr, "->", longest_consecutive_sequence(arr))

print("\nLongest Consecutive Sequence (Sorted, O(n log n)):")
for arr in test_arrays:
    print(arr, "->", longest_consecutive_sequence_better(arr))

print("\nLongest Consecutive Sequence (Optimal, O(n)):")
for arr in test_arrays:
    print(arr, "->", longest_consecutive_sequence_optimal(arr))

    # Matrix Zeroing Tests
print("\nMatrix Zeroing Simple:")
print(set_matrix_zero([[1,1,1],[1,0,1],[1,1,1]]))

print("\nMatrix Zeroing Using Sets:")
print(set_matrix_zero_better([[1,2,1],[1,0,1],[1,1,1]]))

print("\nMatrix Zeroing Optimized (O(1) space):")
print(set_matrix_zeroes_more_optimized([[1,2,3],[4,0,6],[7,8,9]]))


# ---------------------------
# Remove Duplicates from Sorted Array
# ---------------------------

# Allow at most 2 duplicates
def remove_duplicates_two(arr):
    """
    Remove duplicates from a sorted array allowing at most 2 occurrences.
    Returns new length.
    """
    if len(arr) <= 2:
        return len(arr)

    k = 2  # first two elements are always valid

    for i in range(2, len(arr)):
        if arr[i] != arr[k-2]:
            arr[k] = arr[i]
            k += 1

    return k


# Allow at most 3 duplicates
def remove_duplicates_three(arr):
    """
    Remove duplicates from a sorted array allowing at most 3 occurrences.
    Returns new length.
    """
    if len(arr) <= 3:
        return len(arr)

    k = 3  # first three elements are always valid

    for i in range(3, len(arr)):
        if arr[i] != arr[k-3]:
            arr[k] = arr[i]
            k += 1

    return k
arr2 = [1,1,1,2,2,2,3,3,3]
length2 = remove_duplicates_two(arr2)
print(length2, arr2[:length2])  # [1,1,2,2,3,3]

arr3 = [1,1,1,2,2,2,3,3,3]
length3 = remove_duplicates_three(arr3)
print(length3, arr3[:length3])  # [1,1,1,2,2,2,3,3,3]
