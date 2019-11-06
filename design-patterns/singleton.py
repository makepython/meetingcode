class OnlyOne(object):
    class __OnlyOne:
        def __init__(self):
            self.val = None

    instance = None
    def __new__(cls): # __new__ always a classmethod
        if not OnlyOne.instance:
            OnlyOne.instance = OnlyOne.__OnlyOne()
        return OnlyOne.instance
    def __getattr__(self, name):
        return getattr(self.instance, name)
    def __setattr__(self, name):
        return setattr(self.instance, name)


one = OnlyOne()
two = OnlyOne()

one.val = 4
print(two.val)
print(type(two))

