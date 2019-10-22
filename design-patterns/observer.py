class Observable:
    def __init__(self):
        self._observers = []
        self._value = 0

    def register_observer(self, observer):
        self._observers.append(observer)

    def _notify_observers(self):
        for observer in self._observers:
            observer.notify(self)

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if value == self._value:
            return

        self._value = value
        self._notify_observers()


class Observer:
    def __init__(self, observable):
        observable.register_observer(self)

    def notify(self, observable):
        print(str(observable) + ' changed: '+str(observable.value))


subject = Observable()
observer = Observer(subject)
subject.value = 5
subject.value = 5
subject.value = 8
