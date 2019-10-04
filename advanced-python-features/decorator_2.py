import functools


def integer_arguments(func):
    def wrapped(x, y):
        assert isinstance(x, int)
        assert isinstance(y, int)
        return func(x, y)
    return wrapped


def integer_arguments_v2(func):
    @functools.wraps(func)
    def wrapped(x, y):
        assert isinstance(x, int)
        assert isinstance(y, int)
        return func(x, y)
    return wrapped


@integer_arguments_v2
def multiply(x, y):
    """Multiplies two integers

    Args:
        x (int): First number
        y (int): Second number

    Returns:
        int: Product
    """
    return x * y


@integer_arguments
def add(x, y):
    """Adds two integers

    Args:
        x (int): First integer
        y (int): Second integer

    Returns:
        int: Sum
    """
    return x + y


def main():
    print("Name is:", add.__name__)
    print(help(add))
    print()
    print("Name is:", multiply.__name__)
    print(help(multiply))


if __name__ == '__main__':
    main()
