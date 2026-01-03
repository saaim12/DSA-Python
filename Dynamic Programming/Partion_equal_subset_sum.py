
def partition_equal_subset(arr):
    if not arr:
        return False

    total=sum(arr)
    target=total//2
    if total%2!=0:
        return False

    n=len(arr)
    def check(idx,t):
        if t==0:
            return True
        if idx<0:
            return False

        not_take=check(idx-1,t)
        take=False
        if arr[idx]<=t:
            take=check(idx-1,t-arr[idx])

        return take or not_take

    return check(n-1,target)

print(partition_equal_subset([1,5,11,5]))
print(partition_equal_subset([1,2,3,5]))

def partition_equal_subset_with_memo(arr):
    if not arr:
        return False

    total=sum(arr)
    target=total//2
    if total%2!=0:
        return False
    memo={}
    n=len(arr)
    def check(idx,t):
        if t==0:
            return True
        if idx<0:
            return False
        if (idx,t) in memo:
            return memo[(idx,t)]
        not_take=check(idx-1,t)
        take=False
        if arr[idx]<=t:
            take=check(idx-1,t-arr[idx])
        memo[(idx,t)]=take or not_take
        return take or not_take

    return check(n-1,target)

def canPartitionTab( arr):
    if not arr:
        return False

    total = sum(arr)
    if total % 2 != 0:
        return False

    target = total // 2
    n = len(arr)

    # dp[i][t] = can we make sum t using first i elements
    dp = [[False] * (target + 1) for _ in range(n)]
    for row in dp:
        print(row)
    print("__________________" * 40)
    # Base cases
    for i in range(n):
        dp[i][0] = True  # sum 0 is always possible
    for row in dp:
        print(row)

    print("__________________"*40)
    if arr[0] <= target:
        dp[0][arr[0]] = True  # take first element if possible
    for row in dp:
        print(row)
    # Fill table
    for i in range(1, n):
        for t in range(1, target + 1):
            not_take = dp[i - 1][t]
            take = False
            if arr[i] <= t:
                take = dp[i - 1][t - arr[i]]
            dp[i][t] = not_take or take
    for row in dp:
        print(row)
    print("__________________" * 40)
    return dp[n - 1][target]
print(canPartitionTab([1,5,11,5]))