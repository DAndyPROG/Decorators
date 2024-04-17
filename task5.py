import time


def sleeper(seconds):
    def decorator(func):
        def wrapper(*args, **kwargs):
            time.sleep(seconds)
            return func(*args, **kwargs)
        return wrapper
    return decorator

@sleeper(5)
def some_function(a, b, c):
    return a + b + c


print(some_function(5, 32, 2))

