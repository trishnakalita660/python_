#  decorator is a function that takes function as a parameter, adds some functionality and returns another function


def decorator_func(original_function):
    def wrapper(*args, **kwargs):
         original_function(*args, **kwargs)
    return wrapper

@decorator_func
def display():
    print("This is the display function")

@decorator_func
def display_info(name, age):
    print('display_inf0 ({}, {})'.format(name, age)) 

display()
display_info("Trishna",22)