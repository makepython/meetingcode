class NonDataDescriptor(object):
    def __get__(self, instance, owner):
        print("NonDataDescriptor __get__", instance, owner)
        return 5


class DataDescriptor(object):
    def __get__(self, instance, owner):
        print("DataDescriptor __get__", instance, owner)
        return 5

    def __set__(self, instance, value):
        print("DataDescriptor __set__", instance, value)



class MyClass(object):
    nondata = NonDataDescriptor()
    data = DataDescriptor()



my = MyClass()
print(my.nondata)
print(my.data)
print(MyClass.nondata)
print(MyClass.data)
my.data = 3
print("XXX")
print(MyClass.data)
MyClass.data = 7
print(MyClass.data)
my.data = 6
