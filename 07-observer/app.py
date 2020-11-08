from abc import ABC, abstractmethod

class Publisher:
    def __init__(self):
        self._observers = []
    
    def register_observer(self, observer):
        self._observers.append(observer)
    
    def notify_observers(self, *args, **kwargs):
        for observer in self._observers:
            observer.notify(self, *args, **kwargs)

class Subscriber(ABC):
    def __init__(self, pub: Publisher):
        pub.register_observer(self)
    
    @abstractmethod
    def notify(self):
        pass

class Subscriber1(Subscriber):
    def notify(self, observable, *args):
        print('Recebido', args, 'de', observable)
        print('Atualizando BD')

class Subscriber2(Subscriber):    
    def notify(self, observable, *args):
        print('Recebido', args, 'de', observable)
        print('Notificando usuários do canal')


pub = Publisher()
sub1= Subscriber1(pub)
sub2 = Subscriber2(pub)

pub.notify_observers('test')