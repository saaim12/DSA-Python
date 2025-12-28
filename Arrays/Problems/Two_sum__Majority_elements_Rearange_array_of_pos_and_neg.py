from collections import Counter

# =========================================================
# Two Sum Implementations
# =========================================================

def two_sum_brute_force(arr, target):
    """
    Brute-force approach
    Time: O(n^2)
    Space: O(1)
    """
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == target:
                return [i, j]
    return [-1, -1]


def two_sum_optimized(arr, target):
    """
    Optimized using hashmap
    Time: O(n)
    Space: O(n)
    """
    num_to_index = {}  # number -> index
    for i, num in enumerate(arr):
        diff = target - num
        if diff in num_to_index:
            return [num_to_index[diff], i]
        num_to_index[num] = i
    return [-1, -1]


# =========================================================
# Sort an array of 0s, 1s, and 2s
# =========================================================

def sort_0_1_2_brute_force(arr):
    """
    Bubble sort
    Time: O(n^2)
    Space: O(1)
    """
    n = len(arr)
    for _ in range(n):
        for j in range(1, n):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
    return arr


def sort_0_1_2_better(arr):
    """
    Counting approach
    Time: O(n)
    Space: O(1)
    """
    count0 = count1 = count2 = 0

    for num in arr:
        if num == 0:
            count0 += 1
        elif num == 1:
            count1 += 1
        else:
            count2 += 1

    index = 0
    for _ in range(count0):
        arr[index] = 0
        index += 1
    for _ in range(count1):
        arr[index] = 1
        index += 1
    for _ in range(count2):
        arr[index] = 2
        index += 1

    return arr


def sort_0_1_2_optimal(arr):
    """
    Dutch National Flag Algorithm
    Time: O(n)
    Space: O(1)
    """
    low = 0
    mid = 0
    high = len(arr) - 1

    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:  # arr[mid] == 2
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1

    return arr


# =========================================================
# Majority Element
# =========================================================

def majority_element_brute_force(arr):
    """
    Frequency counting using hashmap
    Time: O(n)
    Space: O(n)
    """
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1

    max_count = 0
    element = None
    for k, v in freq.items():
        if v > max_count:
            max_count = v
            element = k

    return max_count, element


def majority_element_counter(arr):
    """
    Using Python Counter
    Time: O(n)
    Space: O(n)
    """
    counter = Counter(arr)
    element, count = counter.most_common(1)[0]
    return count, element


def majority_element_optimized(arr):
    """
    Boyer-Moore Voting Algorithm
    Time: O(n)
    Space: O(1)
    """
    count = 0
    candidate = None

    for num in arr:
        if count == 0:
            candidate = num
        count += 1 if num == candidate else -1

    # Verification step (important!)
    if arr.count(candidate) > len(arr) // 2:
        return candidate
    return None


def rearrangeArray(nums):
    pos = []
    neg = []
    for num in nums:
        if num < 0:
            neg.append(num)
        else:
            pos.append(num)

    for i in range(len(nums) // 2):
        nums[2 * i] = pos[i]
        nums[2 * i + 1] = neg[i]

    return nums

def rearrange_array_more_optimized_interms_of_time_complexity(arr):
    ans=[0]*len(arr)
    neg_idx=1
    pos_idx=0
    for num in arr:
        if num<0:
            ans[neg_idx]=num
            neg_idx+=2
        else:
            ans[pos_idx]=num
            pos_idx+=2

    return ans


def rearrange(arr):
        # code here
    pos = []
    neg = []
    for num in arr:
        if num < 0:
            neg.append(num)
        else:
            pos.append(num)

    if len(pos) > len(neg):
        for i in range(len(neg)):
            arr[i * 2] = pos[i]
            arr[i * 2 + 1] = neg[i]
        idx = len(neg) * 2
        for i in range(len(neg), len(pos)):
            arr[idx] = pos[i]
            idx += 1

    else:
        for i in range(len(pos)):
            arr[i * 2] = pos[i]
            arr[i * 2 + 1] = neg[i]
        idx = len(pos) * 2
        for i in range(len(pos), len(neg)):
            arr[idx] = neg[i]
            idx += 1

    return arr


# =========================================================
# Example Usage
# =========================================================

if __name__ == "__main__":

    # Two Sum
    arr = [2, 7, 11, 15]
    target = 9
    print("Two Sum Brute Force:", two_sum_brute_force(arr, target))
    print("Two Sum Optimized:", two_sum_optimized(arr, target))

    # Sort 0, 1, 2
    nums = [2, 0, 2, 1, 1, 0]
    print("Sort Brute Force:", sort_0_1_2_brute_force(nums.copy()))
    print("Sort Better:", sort_0_1_2_better(nums.copy()))
    print("Sort Optimal:", sort_0_1_2_optimal(nums.copy()))

    # Majority Element
    arr2 = [1, 2, 3, 3, 3, 3, 4]
    print("Majority (Brute Force):", majority_element_brute_force(arr2))
    print("Majority (Counter):", majority_element_counter(arr2))
    print("Majority (Boyer-Moore):", majority_element_optimized(arr2))






