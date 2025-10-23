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




