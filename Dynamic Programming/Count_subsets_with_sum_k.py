def Count_Subsets_with_sum_k(arr,k):
    n=len(arr)
    def check(idx,s):
        if s==0:
            return 1
        if idx<0:
            return 0

        not_pick=check(idx-1,s)
        pick=0
        if arr[idx]<=s:
            pick=check(idx-1,s-arr[idx])

        return pick+not_pick

    return check(n-1,k)


def Count_Subsets_with_sum_k_with_memo(arr,k):
    n=len(arr)
    memo={}
    def check(idx,s):
        if s==0:
            return 1
        if idx<0:
            return 0
        if (idx,s) in memo:
            return memo[(idx,s)]
        not_pick=check(idx-1,s)
        pick=0
        if arr[idx]<=s:
            pick=check(idx-1,s-arr[idx])
        memo[(idx,s)]=pick+not_pick
        return pick+not_pick

    return check(n-1,k)


def Count_subsets_with_sum_k_with_tabulation(arr,k):
    n = len(arr)
    dp = [[0] * (k + 1) for _ in range(n)]

    # Base case: sum 0 can always be made by empty subset
    for i in range(n):
        dp[i][0] = 1

    # Base case: first element
    if arr[0] <= k:
        dp[0][arr[0]] = 1

    # Fill DP table
    for i in range(1, n):
        for s in range(1, k + 1):
            not_pick = dp[i - 1][s]
            pick = dp[i - 1][s - arr[i]] if arr[i] <= s else 0
            dp[i][s] = pick + not_pick

    return dp[n - 1][k]


arr = [1,2,3]
k = 3
print(Count_Subsets_with_sum_k(arr, k))

def Count_Subsets_with_sum_k_if_contain_zeros(arr,k):
    n=len(arr)
    def check(idx,s):
        if idx==0:
            if s==0 and arr[idx]==0:
                return 2
            if s==0 and s==arr[0]:
                return 1
            return 0

        not_pick=check(idx-1,s)
        pick=0
        if arr[idx]<=s:
            pick=check(idx-1,s-arr[idx])

        return pick+not_pick

    return check(n-1,k)

print(Count_Subsets_with_sum_k_if_contain_zeros([0,0,1],1))