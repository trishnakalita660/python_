#  decorator with args
def prefix_decorator(prefix):
    def decorator_func(original_function):
        def wrapper(*args, **kwargs):
            print(prefix, "Executed before ", original_function.__name__ )
            res = original_function(*args, *kwargs)
            print(prefix, "Exec after", original_function.__name__,'\n')
            return res
        return wrapper
    return decorator_func

@prefix_decorator('Testing')
def display(name, age):
    print('Display {} {}'.format(name,age))

display("Trishna", 22)