import functools


def counter(func):
    """Decorator that counts the number of calls to the decorated function."""
    @functools.wraps(func)
    def wrapper():
        wrapper.count += 1
        return func()
    wrapper.count = 0
    return wrapper


@counter
def foo():
    print("Hello, World!")


foo()
foo()
print(foo.__name__, "was called", foo.count, "times.")
