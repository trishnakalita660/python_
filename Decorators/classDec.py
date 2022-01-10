# Decorators using class

class DecoratorClass(object):
    def __init__(self, original_funtion):
        self.original_funtion=original_funtion

    def __call__(self, *args, **kwargs):
        print("call method is executed")
        return self.original_funtion(*args, **kwargs)

@DecoratorClass
def display():
    print("Display function")

@DecoratorClass
def display_info(name, age):
    print('Disolay_info function with name:{} and age:{}'.format(name, age))

display()
display_info("Dhiman", 21)