

class Observable:
    def __init__(self):
        self._observers = []
    
    def register_observer(self, observer):
        self._observers.append(observer)
    
    def notify_observers(self, *args, **kwargs):
        for observer in self._observers:
            observer.notify(self, *args, **kwargs)

class Observer:
    def __init__(self, observable):
        observable.register_observer(self)
    
    def notify(self, observable, *args):
        print('Recebido', args, 'de', observable)


subject = Observable()
observer1 = Observer(subject)
observer2 = Observer(subject)
subject.notify_observers('test')