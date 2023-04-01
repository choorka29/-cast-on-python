def cast(t):
    def decorator(f):
        def wrapper(*args, **kwargs):
            result = f(*args, **kwargs)
            try:
                return t(result)
            except (TypeError, ValueError):
                return result
        return wrapper
    return decorator



@cast(int)
def some_function():
    return "42"

result = some_function()
print(type(result), result) 