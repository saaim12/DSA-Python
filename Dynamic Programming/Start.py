from collections import defaultdict
from email.policy import default


def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

# Example
print(fib(4))


def printing_fib(n):
    if n <=0:
        return str(n)

    a,b=0,1
    seq=[]
    for i in range(n+1):
        seq.append(str(a))
        a,b=b,a+b

    return " ".join(seq)

print(printing_fib(10))

# Fibonacci with Memoization
# | Method           | Time  | Space |
# | ---------------- | ----- | ----- |
# | Normal recursion | O(2ⁿ) | O(n)  |
# | Memoization      | O(n)  | O(n)  |

def fibonacci_plus_memorization(num,memo):
    if num<=1:
        return num
    if num in memo:
        return memo[num]
    memo[num]=fibonacci_plus_memorization(num-1,memo)+fibonacci_plus_memorization(num-2,memo)
    return memo[num]

print(fibonacci_plus_memorization(10,{}))

### now tabulation
# | Tabulation      | O(n)  | O(n)  |
def fib_with_tabulation(n):
    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


print(fib_with_tabulation(10))


## space optimization of tabulation
def fib_with_tabulation_and_space_optimization(n):
    if n <= 1:
        return n

    prev2 = 0  # F(0)
    prev1 = 1  # F(1)
    for i in range(2,n+1):
        curr=prev1+prev2
        prev2=prev1
        prev1=curr

    return prev1

print(fib_with_tabulation_and_space_optimization(10))
