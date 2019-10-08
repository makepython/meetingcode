from __future__ import print_function

from abc import ABCMeta, abstractmethod

class Button:
    __metaclass__ = ABCMeta

    @abstractmethod
    def paint(self):
        pass

class LinuxButton(Button):
    def paint(self):
        return "Render a button in a Linux style"

class WindowsButton(Button):
    def paint(self):
        return "Render a button in a Windows style"

class MacOSButton(Button):
    def paint(self):
        return "Render a button in a MacOS style"

class GUIFactory:
    __metaclass__ = ABCMeta

    @abstractmethod
    def create_button(self):
        pass

class LinuxFactory(GUIFactory):
    def create_button(self):
        return LinuxButton()

class WindowsFactory(GUIFactory):
    def create_button(self):
        return WindowsButton()

class MacOSFactory(GUIFactory):
    def create_button(self):
        return MacOSButton()

appearance = "linux"

if appearance == "linux":
    factory = LinuxFactory()
elif appearance == "osx":
    factory = MacOSFactory()
elif appearance == "win":
    factory = WindowsFactory()
else:
    raise NotImplementedError(
        "Not implemented for your platform: {}".format(appearance)
    )

if factory:
    button = factory.create_button()
    result = button.paint()
    print(result)
