# Don't do this.


class MySingleton:
    _instance = None
    @classmethod
    def instance(cls):
        if cls._instance == None:
            cls._instance = cls()

        return cls._instance


print(MySingleton.instance())
print(MySingleton.instance())

# Problem: nothing prevents you to instantiate a new MySingleton instance.



