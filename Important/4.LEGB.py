# Local, Enclosing, Global, Built-in
#  scope search: local -> Enclosing -> Global -> Builtin

# Python gives you the power to redefine the builtin functions due to its scope hierarchy!  

import builtins

print(dir(builtins))
x = 'global x'

def scope(z):
    global x
    x = 'x is changed'
    y = 'local y'
    print(y)
    print(x)
    print(z)


scope('local z')
print(x)

# Enclosing -> nested functions ( similar to javascript closures)

def outer():
    x = 'outer x'
    def inner():
        # x = 'inner x'
        nonlocal x
        x ='inner x'
        print(x)
    inner()
    print(x)
outer()
print(x)
