# -------------------------------
# 1. Generate all subsets (brute)
# -------------------------------
def making_subsets(arr):
    res = []

    def subs(idx, path):
        res.append(list(path))
        for i in range(idx, len(arr)):
            path.append(arr[i])
            subs(i + 1, path)
            path.pop()

    subs(0, [])
    return res


# -------------------------------
# 2. Recursive (no memo)
# -------------------------------
def subsequence_contain_k_recursive(arr, k):
    def check(idx, target):
        if target == 0:
            return True
        if idx == 0:
            return arr[0] == target

        not_take = check(idx - 1, target)
        take = False
        if target >= arr[idx]:
            take = check(idx - 1, target - arr[idx])

        return take or not_take

    return check(len(arr) - 1, k)


# -------------------------------
# 3. Memoization
# -------------------------------
def subsequence_contain_k_memo(arr, k):
    memo = {}

    def check(idx, target):
        if target == 0:
            return True
        if idx == 0:
            return arr[0] == target

        if (idx, target) in memo:
            return memo[(idx, target)]

        not_take = check(idx - 1, target)
        take = False
        if target >= arr[idx]:
            take = check(idx - 1, target - arr[idx])

        memo[(idx, target)] = take or not_take
        return memo[(idx, target)]

    return check(len(arr) - 1, k)


# -------------------------------
# 4. Pretty printer (DP + choice)
# -------------------------------
def print_dp_with_choice(dp, choice, arr, k, step):
    print(f"\nStep {step}  (using arr[0..{step}])")
    print("       ", end="")
    for j in range(k + 1):
        print(f"{j:4}", end="")
    print("\n       " + "-" * (5 * (k + 1)))

    for i in range(len(dp)):
        label = f"a[{i}]={arr[i]}" if i <= step else "     "
        print(f"{label:7} |", end="")
        for j in range(k + 1):
            if dp[i][j]:
                print(f"{choice[i][j]:>4}", end="")
            else:
                print("   .", end="")
        print()


# -------------------------------
# 5. Tabulation with TAKE / NT
# -------------------------------
def subsequence_contain_k_tabulation(arr, k):
    n = len(arr)

    dp = [[False] * (k + 1) for _ in range(n)]
    choice = [["."] * (k + 1) for _ in range(n)]

    # base case
    for i in range(n):
        dp[i][0] = True
        choice[i][0] = "NT"

    if arr[0] <= k:
        dp[0][arr[0]] = True
        choice[0][arr[0]] = "T"

    print_dp_with_choice(dp, choice, arr, k, 0)

    for i in range(1, n):
        for j in range(1, k + 1):
            not_take = dp[i - 1][j]
            take = False

            if j >= arr[i]:
                take = dp[i - 1][j - arr[i]]

            dp[i][j] = take or not_take

            if take and not_take:
                choice[i][j] = "B"
            elif take:
                choice[i][j] = "T"
            elif not_take:
                choice[i][j] = "NT"

        print_dp_with_choice(dp, choice, arr, k, i)

    return dp[n - 1][k]


# -------------------------------
# 6. Driver Code
# -------------------------------
if __name__ == "__main__":
    arr = [1, 2, 3]
    k = 3

    print("All subsets:")
    print(making_subsets(arr))

    print("\nRecursive:", subsequence_contain_k_recursive(arr, k))
    print("Memoized:", subsequence_contain_k_memo(arr, k))

    print("\nTabulation + Decisions:")
    print("Result:", subsequence_contain_k_tabulation(arr, k))
