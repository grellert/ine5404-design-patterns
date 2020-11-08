# fonte: https://refactoring.guru/pt-br/design-patterns/adapter/python/example

class ITarget:
    #essa interface contém o método que deve ser executado
    def request(self) -> str:
        pass

class Adaptee:
    # contém métodos úteis, mas incompatíveis com  interface
    def specific_request(self) -> (int, str):
        return (1, "Mateus Grellert")


class Adapter(ITarget):
    __adaptee = Adaptee()
    # Adapter torna a interface do Adaptado (Adaptee) compatível com o Alvo através de herança múltipla
    def request(self) -> str:
        (id, name) = self.__adaptee.specific_request()
        return f'{name}\n'

# Target implementa a interface ITarget com compartamento esperado
class Target(ITarget):
    def request(self) -> str:
        return 'Mateus Grellert'


def client_code(target: Target) -> None:
    # código cliente suporta qualquer classe que siga a interface Alvo
    print(target.request(), end="")


if __name__ == "__main__":
    print('Client: Consigo trabalhar bem com objetos do tipo Alvo')
    target = Target()
    client_code(target)
    print("\n")

    adaptee = Adaptee()
    print("Client: A Classe Adaptado tem uma interface estranha que não entendo: ")
    print(f"Adaptado: {adaptee.specific_request()}\n")

    print("Client: Mas com o Adaptador isso é resolvido:")
    adapter = Adapter()
    client_code(adapter)
