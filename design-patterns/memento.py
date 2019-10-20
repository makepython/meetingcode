# Add memento
import copy

class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def memento(self):
        return copy.deepcopy(self.__dict__)

    def restore(self, memento):
        self.__dict__.update(memento)

    def __str__(self):
        return " ".join([self.name, self.surname, str(self.age)])



p = Person("Stefano", "Borini", 42)
# memento is an opaque object. It should not be interacted with, or
# its state made visible
memento = p.memento()

print(p)

p.name = "Bill"
p.surname = "Gates"

print(p)

p.restore(memento)

print(p)






