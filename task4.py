def function_info(func):
    def wrapper(*args, **kwargs):
        print(f"Function is called {func.__name__}, args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"After function called {func.__name__}, result:{result}")
        return result
    return wrapper

@function_info
def some_func(a, b, c):
    return a + b + c

some_func(3, 5, 9)