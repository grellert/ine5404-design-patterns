
# exemplo de singleton
# a classe abaixo serve como classe base para outras
class Singleton(object):
    __instance = None

    # sobrescrita do magic method __new__ para
    # ser nosso getInstance
    def __new__(cls, *args):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls, *args)
        return cls.__instance

class DBDriver(Singleton):
    def __init__(self):
        pass

    def connect(self, url, user):
        pass
    
    def select_db(self, db_name):
        pass
    
db1 = DBDriver()
print(id(db1))

db2 = DBDriver()
print(id(db2))


