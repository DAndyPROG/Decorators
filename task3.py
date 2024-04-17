def called_decorator(func):
    def inner(*args, **kwargs):
        print("Function is been called")
        result = func(*args, **kwargs)
        return result
    
    return inner


@called_decorator
def some_func(a, b, c):
    
    print("some code")
    return a + b + c

print(some_func(1, 4, 5))
