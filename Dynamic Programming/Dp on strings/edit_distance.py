# Edit Distance Implementations in one file

# ----------------------------
# 1️⃣ Recursive (Naive)
# ----------------------------
def editDistanceRecursive(s1, s2):
    n, m = len(s1), len(s2)

    def check(i, j):
        if i < 0:
            return j + 1
        if j < 0:
            return i + 1
        if s1[i] == s2[j]:
            return check(i - 1, j - 1)
        else:
            return min(
                1 + check(i - 1, j),  # deletion
                1 + check(i, j - 1),  # insertion
                1 + check(i - 1, j - 1)  # replacement
            )

    return check(n - 1, m - 1)


# ----------------------------
# 2️⃣ Recursive + Memoization
# ----------------------------
def editDistanceMemo(s1, s2):
    n, m = len(s1), len(s2)
    dp = {}

    def check(i, j):
        if i < 0:
            return j + 1
        if j < 0:
            return i + 1
        if (i, j) in dp:
            return dp[(i, j)]
        if s1[i] == s2[j]:
            dp[(i, j)] = check(i - 1, j - 1)
        else:
            dp[(i, j)] = min(
                1 + check(i - 1, j),  # deletion
                1 + check(i, j - 1),  # insertion
                1 + check(i - 1, j - 1)  # replacement
            )
        return dp[(i, j)]

    return check(n - 1, m - 1)


# ----------------------------
# 3️⃣ Tabulation (Bottom-Up DP)
# ----------------------------
def editDistanceTab(s1, s2):
    n, m = len(s1), len(s2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(
                    dp[i - 1][j],  # deletion
                    dp[i][j - 1],  # insertion
                    dp[i - 1][j - 1]  # replacement
                )
    return dp[n][m]


# ----------------------------
# 4️⃣ Space-Optimized Tabulation
# ----------------------------
def editDistanceOptimized(s1, s2):
    n, m = len(s1), len(s2)
    prev = list(range(m + 1))

    for i in range(1, n + 1):
        curr = [i] + [0] * m
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                curr[j] = prev[j - 1]
            else:
                curr[j] = 1 + min(
                    prev[j],  # deletion
                    curr[j - 1],  # insertion
                    prev[j - 1]  # replacement
                )
        prev = curr
    return prev[m]


# ----------------------------
# Test Cases
# ----------------------------
if __name__ == "__main__":
    tests = [
        ("kitten", "sitting"),
        ("flaw", "lawn"),
        ("intention", "execution"),
        ("abc", "abc"),
        ("", "test"),
        ("test", "")
    ]

    for s1, s2 in tests:
        print(f"Strings: '{s1}' -> '{s2}'")
        print("Recursive:", editDistanceRecursive(s1, s2))
        print("Memoization:", editDistanceMemo(s1, s2))
        print("Tabulation:", editDistanceTab(s1, s2))
        print("Optimized:", editDistanceOptimized(s1, s2))
        print("-" * 40)
