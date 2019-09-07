class NonDataDescriptor(object):
    def __get__(self, *args, **kwargs):
        print("NonDataDescriptor __get__", args, kwargs)
        return 5


class DataDescriptor(object):
    def __get__(self, *args, **kwargs):
        print("DataDescriptor __get__", args, kwargs)
        return 5

    def __set__(self, *args, **kwargs):
        print("DataDescriptor __set__", args, kwargs)



class MyClass(object):
    nondata = NonDataDescriptor()
    data = DataDescriptor()



my = MyClass()
print(my.nondata)
print(my.data)
my.data = 3
