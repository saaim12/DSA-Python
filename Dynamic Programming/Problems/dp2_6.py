def climbing_stairs(n):
    if n==0:
        return 1
    if n==1:
        return 1
    return climbing_stairs(n-1)+climbing_stairs(n-2)

print(climbing_stairs(3))

## with memo
def climbStairs_with_Memo( n):
    memo = {}

    def fun(n):
        if n == 0:
            return 1
        if n == 1:
            return 1
        if n in memo:
            return memo[n]

        memo[n] = fun(n - 1) + fun(n - 2)
        return memo[n]

    return fun(n)

print(climbStairs_with_Memo(3))


def climbStairs_tabulation(n):
    if n <= 2:
        return n

    a, b = 1, 2
    for i in range(3, n + 1):
        a, b = b, a + b
    return b

print(climbStairs_tabulation(3))


#### problem 2
### frog jump
def frog_jump(arr):
    def jumping(idx):
        if idx==0:
            return 0
        left=jumping(idx-1)+abs(arr[idx]-arr[idx-1])
        right=float('inf')
        if idx>1:
            right=jumping(idx-2)+abs(arr[idx]-arr[idx-2])

        return min(left,right)
    n=len(arr)
    return jumping(n-1)

print(frog_jump([10,20,30,10]))

def frog_Jump_with_Memo(arr):
    dp={}
    def Jumping(idx):
        if idx ==0:
            return 0
        if idx in dp:
            return dp[idx]
        left=Jumping(idx-1)+abs(arr[idx]-arr[idx-1])
        right=float('inf')
        if idx>1:
            right=Jumping(idx-2)+abs(arr[idx]-arr[idx-2])
        dp[idx]=min(left,right)
        return dp[idx]
    return Jumping(len(arr)-1)

print(frog_Jump_with_Memo([10,20,30,10]))

def frog_jump_tabulation(arr):
    n=len(arr)
    dp=[0]*n
    for i in range(1,n):
        left=dp[i-1]+abs(arr[i]-arr[i-1])
        right=float('inf')
        if i>1:
            right=dp[i-2]+abs(arr[i]-arr[i-2])
        dp[i]=min(left,right)

    return dp[n-1]

print(frog_jump_tabulation([10,20,30,10]))

def frog_jump_tabulation_more_optimized(arr):
    n=len(arr)
    dp1=0
    dp2=0
    for i in range(1,n):
        left=dp1+abs(arr[i]-arr[i-1])
        right=float('inf')
        if i>1:
            right=dp2+abs(arr[i]-arr[i-2])
        curr=min(left,right)
        dp2=dp1
        dp1=curr

    return dp1
print(frog_jump_tabulation_more_optimized([10,20,30,10]))