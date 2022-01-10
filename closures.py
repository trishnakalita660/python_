#  similar to js

# msg= 'outer Hi'
def outer():
    msg = 'Hi'
    def inner():
        print(msg)
    return inner
outer()()