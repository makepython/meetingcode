# Don't do this


_instance = None

class MySingleton:
    pass


def instance():
    global _instance

    if _instance is None:
        _instance = MySingleton()

    return _instance


print(instance())
print(instance())
