from collections import Counter

# =========================================================
# MAJORITY ELEMENT
# =========================================================

def majority_element_bruteforce(arr):
    """
    Brute force using hashmap
    Time: O(n)
    Space: O(n)
    Returns: (frequency, element)
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


def majority_element_optimal(arr):
    """
    Boyer-Moore Voting Algorithm
    Time: O(n)
    Space: O(1)
    Returns majority element if exists, else -1
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
# BEST TIME TO BUY AND SELL STOCK
# =========================================================

def best_time_to_buy_and_sell(prices):
    """
    One pass solution
    Time: O(n)
    Space: O(1)
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
# DRIVER CODE (TESTING)
# =========================================================

if __name__ == "__main__":

    # Majority Element
    print("-" * 50)
    arr1 = [1, 2, 3, 3, 3, 3, 4]
    print("Majority Brute Force:", majority_element_bruteforce(arr1))
    print("Majority Optimal:", majority_element_optimal(arr1))
    print("Using Counter:", Counter(arr1))

    print("-" * 50)

    # Best Time to Buy and Sell Stock
    prices = [7, 1, 5, 3, 6, 4]
    print("Max Profit:", best_time_to_buy_and_sell(prices))

    print("-" * 50)



def medianSlidingWindow( nums, k):
    """
    Find the median for every sliding window of size k.
    :type nums: List[int]
    :type k: int
    :rtype: List[float]
    """
    def find_median(arr):
        arr_sorted = sorted(arr)
        n = len(arr_sorted)
        mid = n // 2
        if n % 2 == 0:
            return (arr_sorted[mid-1] + arr_sorted[mid]) / 2.0
        else:
            return float(arr_sorted[mid])

    res = []
    left = 0
    for i in range(len(nums)):
        if i-left+1==k:
            win=nums[left:i+1]
            res.append(find_median(win))
            left+=1
    return res


print(medianSlidingWindow([1,3,-1,-3,5,3,6,7],3))