def check_for_integer(function):
    def wrapped(x, y):
        assert isinstance(x, int)
        assert isinstance(y, int)
        return function(x, y)
    return wrapped


@check_for_integer
def multiply(x, y):
    return x * y


@check_for_integer
def add(x, y):
    return x + y


def main():
    print(multiply(2, 3))
    print(add(4, 5))
    print([0] * 4)
    print(multiply([0], 4))


if __name__ == '__main__':
    main()
