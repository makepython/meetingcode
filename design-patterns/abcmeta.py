import abc

class Command(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def execute(self):
        pass

    @abc.abstractmethod
    def undo(self):
        pass

class RenameAccount(Command):
    def execute(self):
        print("executing")

c=RenameAccount()
c.execute()
