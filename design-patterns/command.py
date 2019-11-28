from abc import ABCMeta, abstractmethod
from collections import deque

class Command(metaclass=ABCMeta):
    """The COMMAND interface"""
    def __init__(self, obj):
        self._obj = obj

    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass


class Account:
    def __init__(self, owner, content):
        self._owner = owner
        self._content = content

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, owner):
        self._owner = owner

    @property
    def content(self):
        return self._content

    def credit(self, amount):
        self._content += amount

    def withdraw(self, amount):
        self._content -= amount


class TranserCommand(Command):
    def __init__(self, src_account, dest_account, amount):
        self._src_account = src_account
        self._dest_account = dest_account
        self._amount = amount

    def execute(self):
        self._src_account.withdraw(self._amount)
        self._dest_account.credit(self._amount)

    def undo(self):
        self._src_account.credit(self._amount)
        self._dest_account.withdraw(self._amount)


class RenameOwnerCommand(Command):
    def __init__(self, account, new_owner):
        self._account = account
        self._new_owner = new_owner
        self._old_owner = None

    def execute(self):
        if self._old_owner is not None:
            raise Exception("Attempt to execute command twice")

        self._old_owner = self._account.owner
        self._account.owner = self._new_owner

    def undo(self):
        if self._old_owner == None:
            raise Exception("Cannot undo non-executed command")

        self._account.owner = self._old_owner


if __name__ == "__main__":
    acc1 = Account("Stefano", 1000)
    acc2 = Account("Bill", 1000000)

    c1 = TranserCommand(acc1, acc2, 500)
    c1.execute()
    print(acc1.content)
    print(acc2.content)

    c2 = RenameOwnerCommand(acc2, "Melinda")
    c2.execute()
    print(acc2.owner)
    c2.undo()
    print(acc2.owner)
    c1.undo()
    print(acc1.content)
    print(acc2.content)




