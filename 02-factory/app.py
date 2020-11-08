# fonte: adaptado de https://en.wikipedia.org/wiki/Factory_method_pattern

from abc import ABC, abstractmethod

# Factory MazeGame que criar jogos do tipo labirinto com salas (produtos) distintas
class MazeGame(ABC):
    def __init__(self) -> None:
        self.rooms = []
        self._prepare_rooms()
   
    # Factory method make_room será especializado para cada tipo de sala
    @abstractmethod
    def make_room(self):
        raise NotImplementedError("You should implement this!")

    def _prepare_rooms(self) -> None:
        room1 = self.make_room()
        room2 = self.make_room()

        room1.connect(room2)
        self.rooms.append(room1)
        self.rooms.append(room2)

    def play(self) -> None:
        print('Playing using "{}"'.format(self.rooms[0]))



# classe derivada 1 - escializa make_room criando uma sala mágica
class MagicMazeGame(MazeGame):
    def make_room(self):
        return MagicRoom()

# classe derivada 2
class OrdinaryMazeGame(MazeGame):
    def make_room(self):
        return OrdinaryRoom()


# versão abstrata da classe Room (sala)
class Room(ABC):
    def __init__(self) -> None:
        self.connected_rooms = []

    def connect(self, room) -> None:
        self.connected_rooms.append(room)

# versão concreta de Room 1 - usada pela classe derivada 1
class MagicRoom(Room):
    def __str__(self):
        return "Magic room"

# versão concreta de Room 2 - usada pela classe derivada 2
class OrdinaryRoom(Room):
    def __str__(self):
        return "Ordinary room"


ordinaryGame = OrdinaryMazeGame()
ordinaryGame.play()

magicGame = MagicMazeGame()
magicGame.play()