# args_kwargs_example.py

# Function using only *args (positional arguments)
def print_args(*args):
    print("Using *args:")
    for i, arg in enumerate(args):
        print(f"Argument {i}: {arg}")
    print("-" * 30)


# Function using only **kwargs (keyword arguments)
def print_kwargs(**kwargs):
    print("Using **kwargs:")
    for key, value in kwargs.items():
        print(f"{key} = {value}")
    print("-" * 30)


# Function using both *args and **kwargs
def print_args_kwargs(*args, **kwargs):
    print("Using *args and **kwargs:")

    # Print positional arguments
    for i, arg in enumerate(args):
        print(f"Argument {i}: {arg}")

    # Print keyword arguments
    for key, value in kwargs.items():
        print(f"{key} = {value}")

    print("-" * 30)


# --------- Function Calls ---------
print_args("apple", "banana", "cherry")

print_kwargs(name="saaim", age=25, country="Pakistan")

print_args_kwargs("first", "second", name="saaim", age=25)
