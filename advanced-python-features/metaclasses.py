MyClass = type("MyClass", (), {})
obj = object.__new__(MyClass)

class AClass(object):
    def __new__(cls, *args, **kwargs):
        print(cls, *args, **kwargs)
        self = object.__new__(cls)
        self.tagged = True
        return self

    def __init__(self, a, b, c):
        print(self.tagged)
        self.a = a
        self.b = b
        self.c = c

a = AClass(1,2,3)


class Whatever(metaclass=type):
    pass


class MyMeta(type):
    def __new__(mcls, name, bases, dct):
        return super().__new__(mcls, name, bases, dct)

    def whatever(cls):
        print("Hello")


class Whatever2(metaclass=MyMeta):
    def foo(self):
        pass

w = Whatever2()

Whatever2.whatever()
w.whatever()

