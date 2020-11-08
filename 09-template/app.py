# fonte: adaptado de https://refactoring.guru/design-patterns/template-method

from abc import ABC, abstractmethod


# Classe abstrata que implementa o método template - nesse caso, turn()
class GameAI(ABC):
    # Método template define o esqueleto do algoritmo.
    def turn(self):
        self.collectResources()
        self.buildStructures()
        self.buildUnits()
        self.attack()

    # Alguns passos podem ser implementados aqui
    def collectResources(self):
        for s in self.builtStructures:
            s.collect()

    # Outros definidos como abstract
    @abstractmethod
    def buildStructures(self):
        pass

    @abstractmethod
    def buildUnits(self):
        pass
   
    def attack(self):
        enemy = self.closestEnemy()
        if not enemy:
            sendScouts(map.center)
        else:
            sendWarriors(enemy.position)
    
    @abstractmethod
    def sendScouts(self):
        pass
    
    @abstractmethod
    def sendWarriors(self):
        pass

# Classes concretas implementam todas as operações abstratas, mas não
# o método template
class OrcsAI(GameAI):
    def buildStructures(self):
        if self.resources:
            # Build farms, then barracks, then stronghold.
            pass
        
    def buildUnits(self):
        if self.resources > self.scout_cost:
            if not self.scouts:
                # Build peon, add it to scouts group.
                pass
            else:
                # Build grunt, add it to warriors group.
                pass

    # ...

    def sendScouts(self, position):
        if (self.scouts.length > 0):
            pass
            # Send scouts to position.

    def sendWarriors(position):
        if (warriors.length > 5):
            pass
            # Send warriors to position.


# Subclasses também podem sobrescrever algumas operações
# Monstros não coletam recursos por exemplo
class MonstersAI(GameAI):
    def collectResources(self):
        pass

    def buildStructures(self):
        pass

    def buildUnits(self):
        pass