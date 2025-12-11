#  basic input
name=input("Enter you name :  ")
print(name)

#integer input
age = int(input("Enter your age: "))
print("Your age is", age)
#float input
height = float(input("Enter your height in meters: "))
print("Your height is", height, "m")

# multiple inputs in one line
a, b = input("Enter two numbers separated by space: ").split()
print("First:", a)
print("Second:", b)


# multiple inputs with spaces for like lists
numbers=list(map(int,input("enter numbers separated by spaces : ").split()))
print("Numbers:", numbers)
