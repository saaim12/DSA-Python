def longest_palindromic_subsequence(s1):
    s2 = s1[::-1]

    def check(idx1, idx2):
        if idx1 == 0 or idx2 == 0:
            return 0

        if s1[idx1 - 1] == s2[idx2 - 1]:
            return 1 + check(idx1 - 1, idx2 - 1)

        return max(
            check(idx1 - 1, idx2),
            check(idx1, idx2 - 1)
        )

    return check(len(s1), len(s2))

def longest_palindromic_subsequence_with_tab(s1):
    s2="".join(reversed(s1))
    n, m = len(s1), len(s2)
    dp = [[0] * (m + 1) for i in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[n][m]
def minimum_insertions_and_deletions_to_make_string_palindrome(s):
    n = len(s)
    lps = longest_palindromic_subsequence_with_tab(s)

    insertions = n - lps
    deletions = n - lps

    return insertions, deletions

print(minimum_insertions_and_deletions_to_make_string_palindrome("abcda"))
