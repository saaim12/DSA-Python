##################################
# fibonacci problem with dp      #
##################################

def fibonacci(n):
    if n<=1:
        return n
    return fibonacci(n-1)+fibonacci(n-2)

print(fibonacci(6))

def fibonacci_with_memo(n):
    memo={}
    def f(n):
        if n<=1:
            memo[n]=n
            return memo[n]
        if n in memo:
            return memo[n]

        memo[n]=f(n-1)+f(n-2)
        return memo[n]

    return f(n)

print(fibonacci_with_memo(6))

def fibonacci_with_tabulation(n):
    if n<=1:
        return n
    dp=[None]*(n+1)
    dp[0]=0
    dp[1]=1
    for i in range(2,n+1):
        dp[i]=dp[i-1]+dp[i-2]
    return dp[n]

print(fibonacci_with_tabulation(6))

def fibonacci_most_optimized(n):
    if n<=1:
        return n
    prev2=0
    prev1=1
    for i in range(2,n+1):
        curr=prev2+prev1
        prev2=prev1
        prev1=curr

    return prev1

print(fibonacci_most_optimized(6))
