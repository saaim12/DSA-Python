# ==============================================
# Wildcard Matching Module
# Supports '?', '*' patterns
# ==============================================

def wildcard_matching_recursive(s, p):
    """
    Pure recursive solution (slow for large strings)
    """
    def check(i, j):
        # Base case: both exhausted
        if i < 0 and j < 0:
            return True
        # Pattern exhausted but string remains
        if j < 0:
            return False
        # String exhausted but pattern remains
        if i < 0:
            return all(c == '*' for c in p[:j+1])
        # Match character or '?'
        if p[j] == s[i] or p[j] == '?':
            return check(i - 1, j - 1)
        # '*' matches zero or more characters
        if p[j] == '*':
            return check(i - 1, j) or check(i, j - 1)
        # No match
        return False

    return check(len(s) - 1, len(p) - 1)


def wildcard_matching_memo(s, p):
    """
    Memoized recursive solution (efficient)
    """
    memo = {}

    def check(i, j):
        if (i, j) in memo:
            return memo[(i, j)]

        # Base cases
        if i == 0 and j == 0:
            memo[(i, j)] = True
        elif j == 0:
            memo[(i, j)] = False
        elif i == 0:
            memo[(i, j)] = all(c == '*' for c in p[:j])
        else:
            if p[j-1] == s[i-1] or p[j-1] == '?':
                memo[(i, j)] = check(i-1, j-1)
            elif p[j-1] == '*':
                memo[(i, j)] = check(i-1, j) or check(i, j-1)
            else:
                memo[(i, j)] = False

        return memo[(i, j)]

    return check(len(s), len(p))


def wildcard_matching_tabulation(s, p):
    """
    Bottom-up DP (tabulation)
    """
    n = len(s)
    m = len(p)
    dp = [[False] * (m + 1) for _ in range(n + 1)]

    dp[0][0] = True  # empty string matches empty pattern

    # Handle empty string with pattern of '*'
    for j in range(1, m + 1):
        if p[j-1] == '*':
            dp[0][j] = dp[0][j-1]

    # Fill DP table
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if p[j-1] == s[i-1] or p[j-1] == '?':
                dp[i][j] = dp[i-1][j-1]
            elif p[j-1] == '*':
                dp[i][j] = dp[i][j-1] or dp[i-1][j]
            else:
                dp[i][j] = False

    return dp[n][m]


# ==============================================
# Quick Test Section
# ==============================================
if __name__ == "__main__":
    test_cases = [
        ("adceb", "*a*b", True),
        ("acdcb", "a*c?b", False),
        ("", "*", True),
        ("abc", "a*?", True),
        ("abc", "a*d", False)
    ]

    print("=== Wildcard Matching Tests ===\n")
    for s, p, expected in test_cases:
        res_recursive = wildcard_matching_recursive(s, p)
        res_memo = wildcard_matching_memo(s, p)
        res_dp = wildcard_matching_tabulation(s, p)
        print(f"s='{s}', p='{p}'")
        print(f"  Recursive: {res_recursive} | Memo: {res_memo} | DP: {res_dp} | Expected: {expected}\n")
