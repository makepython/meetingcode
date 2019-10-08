from collections import deque

class Switch(object):
    """The INVOKER class"""
    def __init__(self):
        self._history = deque()

    @property
    def history(self):
        return self._history

    def execute(self, command):
        self._history.appendleft(command)
        command.execute()

class Command(object):
    """The COMMAND interface"""
    def __init__(self, obj):
        self._obj = obj

    def execute(self):
        raise NotImplementedError

class TurnOnCommand(Command):
    """The COMMAND for turning on the light"""
    def execute(self):
        self._obj.turn_on()

class TurnOffCommand(Command):
    """The COMMAND for turning off the light"""
    def execute(self):
        self._obj.turn_off()

class Light(object):
    """The RECEIVER class"""
    def turn_on(self):
        print("The light is on")

    def turn_off(self):
        print("The light is off")

class LightSwitchClient(object):
    """The CLIENT class"""
    def __init__(self):
        self._lamp = Light()
        self._switch = Switch()

    @property
    def switch(self):
        return self._switch

    def press(self, cmd):
        cmd = cmd.strip().upper()
        if cmd == "ON":
            self._switch.execute(TurnOnCommand(self._lamp))
        elif cmd == "OFF":
            self._switch.execute(TurnOffCommand(self._lamp))
        else:
            print("Argument 'ON' or 'OFF' is required.")

# Execute if this file is run as a script and not imported as a module
if __name__ == "__main__":
    light_switch = LightSwitchClient()
    print("Switch ON test.")
    light_switch.press("ON")
    print("Switch OFF test.")
    light_switch.press("OFF")
    print("Invalid Command test.")
    light_switch.press("****")

    print("Command history:")
    print(light_switch.switch.history)
