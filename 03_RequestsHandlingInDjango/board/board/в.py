def print_gte(val):
    def decorate(func):
        def wrapped(x):
            if x>val:
                return func(x)
            else:
                return 'eror'
        return wrapped
    return decorate

@print_gte(3)
def foo(x):
    print(x)
foo(4)