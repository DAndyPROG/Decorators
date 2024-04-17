def type_checker(*types):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for arg, exepted_types in zip(args, types):
                if not isinstance(arg, exepted_types):
                    raise TypeError(f"Argument{arg} Is not Expected {exepted_types}, got {type(arg)}")
            return func(*args, **kwargs)
        return wrapper
    return decorator


@type_checker(int, str)
def add(a, b, c):
    print( a, b , c)


add(1, "2", 3)

#add('1', "2", True)
