def log_by_verbosity(verbosity):
    def decorator(function):
        def wrapped(x, y):
            if verbosity > 0:
                print(f"About to call {function.__name__}!")
            output = function(x, y)
            if verbosity > 1:
                print("Finished calculation!")
            return output
        return wrapped
    return decorator


@log_by_verbosity(1)
def multiply(x, y):
    return x * y


@log_by_verbosity(2)
def add(x, y):
    return x + y


def main():
    print(multiply(2, 3))
    print(add(4, 5))
    print(multiply.__name__)


if __name__ == '__main__':
    main()
