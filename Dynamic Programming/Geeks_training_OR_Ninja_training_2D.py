# geek_training.py

def geek_training_recursive(arr):
    """
    Recursive solution (no memoization)
    """
    total_days = len(arr)
    total_tasks = len(arr[0])

    def check(day, last):
        if day == 0:
            maxi = 0
            for i in range(total_tasks):
                if i != last:
                    maxi = max(maxi, arr[0][i])
            return maxi

        maxi = 0
        for i in range(total_tasks):
            if i != last:
                points = arr[day][i] + check(day - 1, i)
                maxi = max(maxi, points)
        return maxi

    return check(total_days - 1, total_tasks)


def geek_training_memo(arr):
    """
    Recursive solution with memoization
    """
    total_days = len(arr)
    total_tasks = len(arr[0])
    memo = {}

    def check(day, last):
        if day == 0:
            maxi = 0
            for i in range(total_tasks):
                if i != last:
                    maxi = max(maxi, arr[0][i])
            return maxi

        if (day, last) in memo:
            return memo[(day, last)]

        maxi = 0
        for i in range(total_tasks):
            if i != last:
                points = arr[day][i] + check(day - 1, i)
                maxi = max(maxi, points)

        memo[(day, last)] = maxi
        return maxi

    return check(total_days - 1, total_tasks)


def geek_training_tabulation(arr):
    """
    Iterative DP solution (tabulation)
    """
    days = len(arr)
    tasks = len(arr[0])

    # DP table: dp[day][last_task]
    # last_task = 0..tasks-1, or tasks=dummy for "no restriction yesterday"
    dp = [[0] * (tasks + 1) for _ in range(days)]

    # Base case: day 0
    for last in range(tasks + 1):
        maxi = 0
        for task in range(tasks):
            if task != last:
                maxi = max(maxi, arr[0][task])
        dp[0][last] = maxi

    # Fill the table
    for day in range(1, days):
        for last in range(tasks + 1):
            dp[day][last] = 0
            for task in range(tasks):
                if task != last:
                    points = arr[day][task] + dp[day - 1][task]
                    dp[day][last] = max(dp[day][last], points)

    # Final answer: last day with "no restriction yesterday"
    return dp[days - 1][tasks]


def geek_training_space_optimized(arr):
    """
    Space-optimized DP solution
    """
    days = len(arr)
    tasks = len(arr[0])

    prev = [0] * (tasks + 1)

    # Base case: day 0
    for last in range(tasks + 1):
        maxi = 0
        for task in range(tasks):
            if task != last:
                maxi = max(maxi, arr[0][task])
        prev[last] = maxi

    # Fill for remaining days
    for day in range(1, days):
        curr = [0] * (tasks + 1)
        for last in range(tasks + 1):
            maxi = 0
            for task in range(tasks):
                if task != last:
                    maxi = max(maxi, arr[day][task] + prev[task])
            curr[last] = maxi
        prev = curr

    return prev[tasks]


if __name__ == "__main__":
    test_cases = [
        ([[1, 2, 5], [3, 1, 1], [3, 3, 3]], 11),
        ([[1, 1, 1], [2, 2, 2], [3, 3, 3]], 6),
        ([[4, 2, 6]], 6)
    ]

    print("=== Geek Training Solutions ===")
    for arr, expected in test_cases:
        print(f"Input: {arr}")
        print(f"Recursive Result: {geek_training_recursive(arr)} | Expected: {expected}")
        print(f"Memoization Result: {geek_training_memo(arr)} | Expected: {expected}")
        print(f"Tabulation Result: {geek_training_tabulation(arr)} | Expected: {expected}")
        print(f"Space-Optimized Result: {geek_training_space_optimized(arr)} | Expected: {expected}")
        print("-" * 50)
