class Borg:
    _consciousness = {}
    def __new__(cls):
        instance = super().__new__(cls)
        instance.__dict__ = cls._consciousness
        return instance

def foo():
    b1=Borg()
    b1.foo = 5
    b2=Borg()
    b2.bar = 23



foo()

b3 = Borg()
print(b3.foo, b3.bar)
