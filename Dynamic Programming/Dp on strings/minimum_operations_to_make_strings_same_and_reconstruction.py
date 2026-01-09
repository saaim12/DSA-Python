# ---------------------------------------------
# Longest Common Subsequence (LCS)
# ---------------------------------------------

def longest_common_subsequence_length(s1: str, s2: str) -> int:
    n, m = len(s1), len(s2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[n][m]


# ---------------------------------------------
# Minimum Insertions + Deletions
# to make two strings identical
# ---------------------------------------------

def min_insertions_deletions_to_make_strings_equal(s1: str, s2: str) -> int:
    lcs_len = longest_common_subsequence_length(s1, s2)
    return len(s1) + len(s2) - 2 * lcs_len


# ---------------------------------------------
# Shortest Common Supersequence (SCS)
# + Minimum operations
# ---------------------------------------------

def shortest_common_supersequence_with_cost(s1: str, s2: str):
    n, m = len(s1), len(s2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # Build LCS DP table
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Reconstruct Shortest Common Supersequence
    i, j = n, m
    scs = []

    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            scs.append(s1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            scs.append(s1[i - 1])
            i -= 1
        else:
            scs.append(s2[j - 1])
            j -= 1

    while i > 0:
        scs.append(s1[i - 1])
        i -= 1

    while j > 0:
        scs.append(s2[j - 1])
        j -= 1

    scs.reverse()

    operations = len(s1) + len(s2) - 2 * dp[n][m]
    return "".join(scs), operations


# ---------------------------------------------
# Driver Code
# ---------------------------------------------

if __name__ == "__main__":
    s1 = "brute"
    s2 = "groot"

    print("String 1:", s1)
    print("String 2:", s2)

    print("\nLCS Length:")
    print(longest_common_subsequence_length(s1, s2))

    print("\nMinimum Insertions + Deletions:")
    print(min_insertions_deletions_to_make_strings_equal(s1, s2))

    print("\nShortest Common Supersequence + Operations:")
    scs, ops = shortest_common_supersequence_with_cost(s1, s2)
    print("SCS:", scs)
    print("Operations:", ops)
