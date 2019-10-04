from math import sin, cos


def log_function_entry(func):
    def wrapped(self, x, y):
        print(type(self), x, y)
        return func(self, x, y)
    return wrapped


class Calculator:
    @log_function_entry
    def add(self, x, y):
        return x + y

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def from_polar_coords(r, t):
        x = r * sin(t)
        y = r * cos(t)
        return Point(x, y)


if __name__ == '__main__':
    pt = Point.from_polar_coords(5, 10)
    print(pt.x, pt.y)
    cart = Point(1, 2)
    print(cart.x, cart.y)

