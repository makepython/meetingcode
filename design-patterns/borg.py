class Borg:
    _consciousness = {}
    def __new__(cls):
        instance = super().__new__(cls)
        instance.__dict__ = cls._consciousness
        return instance


b1=Borg()
b1.foo = 5
b2=Borg()
print(b1.foo)
print(b2.foo)
b2.bar = 23
print(b1.bar)
print(Borg._consciousness)
