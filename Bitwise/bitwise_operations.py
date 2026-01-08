# Q1 : find if the number is even or odd
num=2
print(" even " if num & 1 ==1 else "odd")
#Q2 : find the number which is not repeated
arr=[1,1,2,3,3,-4,-4]
unique=0
for num in arr:
    unique^=num
print(unique)
# Q3 : positive as well as negative of numbers
arr=[1,-2,2,-1,3]
#first way
num=0
for i in range(len(arr)):
    num+=arr[i]
print(num)

# Q4 : find ith bit of number
# we want to find the 6th bit
# for this we create MASK
number = 256
i = 6  # bit_position (1-indexed)
mask = 1 << (i - 1)

print("Mask:", mask)
print("number & mask:", number & mask)

if number & mask:
    print(f"{i}th bit is 1")
else:
    print(f"{i}th bit is 0")
# same logic can be used for the set or reset ith bit
# for set we use OR with 1
# for rest we use and with 0

# Q5 : find the right most set bit
n=0
number=128
flag=True
while flag:
    if number & 1:
        flag=False
    number=number>>1
    n+=1
print(n)

# Q6 : turn a number in negative also 2s complement
number =10
print(number)
bits=8
two_complement = ((~number) + 1) & ((1 << bits) - 1)
print(f"Binary: {bin(two_complement)}")
print(f"Decimal: {two_complement}")

# Q7 : find the number appeared once if the other numbers appeared three times
arr=[2,2,-3,2,7,7,8,7,8,8]
result=0
for i in range(32):
    bit_sum=0
    for num in arr:
        if (num>>i) & 1:
            bit_sum+=1
    bit_sum %=3
    if bit_sum:
        result |=(1<<i)
# only in case it is positive
if result>=2**31:
    result-=2**32
print(result)

# Q8 : magic number problem
# Problem Statement (Amazon style)
#
# A number’s magic value is defined as a sum of powers of 5 corresponding to the set bits in its binary representation.
#
# Given a number n, find its magic number.

number =4
base=5
answer=0
power=1
while number:
    if number&1:
        answer+=base**power
    power+=1
    number=number>>1

print(answer)

#Q 10: sum of ntH row in pascal triangle
# # 🧠 Pattern Observed
#
# Sum of each row = 2ⁿ
#
# ✅ Example:
#
# Row 0 → sum = 1 = 2⁰
#
# Row 1 → sum = 2 = 2¹
#
# Row 2 → sum = 4 = 2²
#
# Row 3 → sum = 8 = 2³
#
# So the sum of the nth row = 2ⁿ
row=1
print(2**row)
# in terms of bitwise
print(1<<(row))

# Q11: no of set bits
number=101838
count=0
while number:
    if number& 1:
        count+=1
    number>>=1
print(count)

# Q12 : reverse bits in number
n =10
resut=0
for i in range(32):
    resut<<=1
    resut |=n&1
    n>>=1

print(bin(number))
print(bin(resut))

#Q13 : prime number program
number = 13
is_prime = True  # flag to track if number is prime

if number < 2:
    is_prime = False
else:
    for i in range(2, int(number**0.5) + 1):  # check up to sqrt(number)
        if number % i == 0:
            is_prime = False
            break

if is_prime:
    print(f"{number} is prime")
else:
    print(f"{number} is not prime")
# Q14 : numbers till num which are prime like prime numbers till 40
#brute force is that we send every num to a functions d then check if it is prime or not
#optimized solution is that if 2 is not prime then all the multiples of 2 till that number are discarded
def prime_numbers_till_given_number(num):
   primes=[True]*(num+1)
   primes[0]=primes[1]=False
   for i in range(2,int(num**0.5)+1):
       if primes[i]:
           for j in range(i*i,num+1,i):
               primes[j]=False

   primes_arr=[i for i ,is_prime in enumerate(primes) if is_prime]
   return primes_arr



print(prime_numbers_till_given_number(40))
#Q15 : number if it perfect sqrt or not
def isPerfectSquare(num):
    if num < 2:
        return True  # 0 and 1 are perfect squares

    st, end = 2, num // 2  # No need to check above num//2

    while st <= end:
        m = (st + end) // 2
        square = m * m

        if square == num:
            return True
        elif square < num:
            st = m + 1
        else:
            end = m - 1

    return False

print(isPerfectSquare(4))