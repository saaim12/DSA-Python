
#Python String Methods Guide
#===========================

#🔁 1. Reversing a String
#------------------------
s = "hello"
reversed_s = s[::-1]
print(reversed_s)  # "olleh"

#✂️ 2. Slicing
#-------------
s = "abcdef"
print(s[1:4])    # 'bcd'
print(s[:3])     # 'abc'
print(s[-1])     # 'f'
print(s[::-1])   # 'fedcba' reversing

#🔡 3. Changing Case
#-------------------
s = "hello world"
print(s.upper())        # "HELLO WORLD"
print(s.lower())        # "hello world"
print(s.capitalize())   # "Hello world"
print(s.title())        # "Hello World"
print(s.swapcase())     # "HELLO world" -> "hello WORLD"

#🧹 4. Stripping and Padding
#---------------------------
s = "  hello  "
print(s.strip())         # "hello"
print(s.lstrip())        # "hello  "
print(s.rstrip())        # "  hello"

print(s.center(10, "*")) # "**hello***"
print(s.ljust(10, "-"))  # "hello-----"
print(s.rjust(10, "-"))  # "-----hello"

#🔍 5. Finding and Replacing
#---------------------------
s = "hello world"
print(s.find("world"))       # 6
print(s.find("notfound"))    # -1
print(s.index("world"))      # 6 (error if not found)

print(s.replace("world", "Python"))  # "hello Python"

#🧵 6. Splitting and Joining
#---------------------------
s = "a,b,c,d"
print(s.split(","))     # ['a', 'b', 'c', 'd']

s = "hello world"
print(s.split())        # ['hello', 'world']

words = ['hello', 'world']
print(" ".join(words))  # "hello world"

#🧪 7. String Checks (isX methods)
#--------------------------------
s = "hello"
print(s.isalpha())    # True
print(s.isdigit())    # False
print(s.isalnum())    # True
print(s.isspace())    # False
print(s.islower())    # True
print(s.isupper())    # False
print("Hello".istitle())  # True

#📏 8. Length
#------------
s = "hello"
print(len(s))  # 5

#🧊 9. Immutability
#------------------
# Strings are immutable, meaning:
s = "hello"
# s[0] = "H"  ❌ This will give an error
# Instead:
s = "H" + s[1:]  # "Hello"

str2="dabcabcbbabc"
print(str2.find("abc"))