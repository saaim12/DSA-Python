"""
=========================================================
ARRAY & MATRIX CLASSIC PROBLEMS
=========================================================

This file contains clean and optimized implementations of:
1. Majority Element (Brute Force & Optimal)
2. Best Time to Buy and Sell Stock
3. Sliding Window Median (Brute Force)
4. Rotate Matrix by 90 Degrees (Brute Force & Optimal)

Each problem includes:
- Clear explanation
- Time & space complexity
- Interview-ready code structure
"""

from collections import Counter


# =========================================================
# 1. MAJORITY ELEMENT
# =========================================================

def majority_element_bruteforce(arr):
    """
    Finds the majority element using a hashmap.

    Majority element:
    Element that appears more than n/2 times.

    Time Complexity: O(n)
    Space Complexity: O(n)

    Returns:
        (frequency, element)
    """
    freq = {}

    # Count frequency of each element
    for num in arr:
        freq[num] = freq.get(num, 0) + 1

    max_count = 0
    element = None

    # Find element with maximum frequency
    for k, v in freq.items():
        if v > max_count:
            max_count = v
            element = k

    return max_count, element


def majority_element_optimal(arr):
    """
    Boyer-Moore Voting Algorithm

    Idea:
    - Cancel out different elements
    - Majority element survives if it exists

    Time Complexity: O(n)
    Space Complexity: O(1)

    Returns:
        Majority element if exists, else -1
    """
    count = 0
    candidate = None

    for num in arr:
        if count == 0:
            candidate = num
        count += 1 if num == candidate else -1

    # Verification step (IMPORTANT)
    if arr.count(candidate) > len(arr) // 2:
        return candidate
    return -1


# =========================================================
# 2. BEST TIME TO BUY AND SELL STOCK
# =========================================================

def best_time_to_buy_and_sell(prices):
    """
    One-pass solution to maximize profit.

    Idea:
    - Track minimum price so far
    - Compute profit at each step

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if not prices:
        return 0

    min_price = prices[0]
    max_profit = 0

    for price in prices[1:]:
        max_profit = max(max_profit, price - min_price)
        min_price = min(min_price, price)

    return max_profit


# =========================================================
# 3. SLIDING WINDOW MEDIAN (BRUTE FORCE)
# =========================================================

def median_sliding_window(nums, k):
    """
    Finds median of every sliding window of size k.

    Brute Force:
    - Sort each window
    - Compute median

    Time Complexity: O(n * k log k)
    Space Complexity: O(k)
    """

    def find_median(window):
        window.sort()
        mid = len(window) // 2

        if len(window) % 2 == 0:
            return (window[mid - 1] + window[mid]) / 2.0
        return float(window[mid])

    res = []
    left = 0

    for right in range(len(nums)):
        if right - left + 1 == k:
            res.append(find_median(nums[left:right + 1]))
            left += 1

    return res


# =========================================================
# 4. ROTATE MATRIX BY 90 DEGREES
# =========================================================

def rotate_matrix_bruteforce(matrix):
    """
    Rotate matrix 90 degrees clockwise using extra space.

    Mapping rule:
        rotated[j][n - 1 - i] = matrix[i][j]

    NOTE:
    We cannot use the original matrix here because
    writing directly would overwrite values that are
    still needed later.

    Time Complexity: O(n^2)
    Space Complexity: O(n^2)
    """
    n = len(matrix)
    rotated = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            rotated[j][n - 1 - i] = matrix[i][j]

    return rotated


def rotate_matrix_optimal(matrix):
    """
    Rotate matrix 90 degrees clockwise IN-PLACE.

    Steps:
    1. Transpose the matrix
    2. Reverse each row

    This works in-place because:
    - Transpose uses swapping
    - No data is overwritten

    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    n = len(matrix)

    # Transpose matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for row in matrix:
        row.reverse()

    return matrix


# =========================================================
# DRIVER CODE
# =========================================================

if __name__ == "__main__":

    print("=" * 50)
    print("MAJORITY ELEMENT")
    arr = [1, 2, 3, 3, 3, 3, 4]
    print("Brute Force:", majority_element_bruteforce(arr))
    print("Optimal:", majority_element_optimal(arr))
    print("Counter:", Counter(arr))

    print("=" * 50)
    print("BEST TIME TO BUY AND SELL STOCK")
    prices = [7, 1, 5, 3, 6, 4]
    print("Max Profit:", best_time_to_buy_and_sell(prices))

    print("=" * 50)
    print("SLIDING WINDOW MEDIAN")
    print(median_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3))

    print("=" * 50)
    print("ROTATE MATRIX (BRUTE FORCE)")
    print(rotate_matrix_bruteforce([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

    print("=" * 50)
    print("ROTATE MATRIX (OPTIMAL IN-PLACE)")
    print(rotate_matrix_optimal([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
