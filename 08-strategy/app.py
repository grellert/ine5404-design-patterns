# fonte: adaptado de https://refactoring.guru/design-patterns/strategy/python/example

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


# define a interface de interesse a clientes
class Context:
    def __init__(self, strategy: Strategy) -> None:
        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        # Usualmente podemos mudar a estratégia em tempo de execução.
        self._strategy = strategy

    def do_some_business_logic(self) -> None:
        print("Chamando algum tipo de sort (não importa qual)")
        result = self._strategy.do_algorithm(["a", "b", "c", "d", "e"])
        print(",".join(result))


# declara operações comuns a todas as versões suportadas dos algoritmos
class Strategy(ABC):
    @abstractmethod
    def do_algorithm(self, data: List):
        pass

# Estratégias concretas que seguem a interface
class ConcreteStrategyA(Strategy):
    def do_algorithm(self, data: List) -> List:
        return sorted(data)


class ConcreteStrategyB(Strategy):
    def do_algorithm(self, data: List) -> List:
        return reversed(sorted(data))

if __name__ == "__main__":
    # Código cliente seleciona alguma estratégia e passa para Context.
    # Cliente deve saber sobre as diferentes estratégias para escolher corretamente.
    
    context = Context(ConcreteStrategyA())
    print("Client: estratégia setada para sort normal.")
    context.do_some_business_logic()
    print()

    print("Client: estratégia setada para sort reverso.")
    context.strategy = ConcreteStrategyB()
    context.do_some_business_logic()
