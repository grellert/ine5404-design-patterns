# fonte: adaptado de https://en.wikipedia.org/wiki/Abstract_factory_pattern


from abc import ABC, abstractmethod
from sys import platform

# Abstract interfaces da família de widgets (produtos)
class Window(ABC):
    @abstractmethod
    def paint(self):
        pass

class Button(ABC):
    @abstractmethod
    def paint(self):
        pass

# implementacões concreta para cada OS
class LinuxButton(Button):
    def paint(self):
        return "Render a button in a Linux style"

class LinuxWindow(Window):
    def paint(self):
        return "Render a window in a Linux style"


class WindowsButton(Button):
    def paint(self):
        return "Render a button in a Windows style"

class WindowsWindow(Window):
    def paint(self):
        return "Render a window in a Windows style"


class MacOSButton(Button):
    def paint(self):
        return "Render a button in a MacOS style"

class MacOSWindow(Window):
    def paint(self):
        return "Render a window in a MacOS style"

# Abstract factory para GUIs
class GUIFactory(ABC):
    @abstractmethod
    def create_button(self):
        pass
    def create_window(self):
        pass


# implementações concretas das GUIs
class LinuxFactory(GUIFactory):
    def create_button(self):
        return LinuxButton()

    def create_window(self):
        return LinuxWindow()


class WindowsFactory(GUIFactory):
    def create_button(self):
        return WindowsButton()

    def create_window(self):
        return WindowsWindow()


class MacOSFactory(GUIFactory):
    def create_button(self):
        return MacOSButton()

    def create_window(self):
        return MacOSWindow()


# Aplicação cliente
class Application:
    def __init__(self, factory: GUIFactory):
        self.__factory = factory

    def createUI(self):
        self.__button = self.__factory.create_button()
        self.__window = self.__factory.create_window()
        print(self.__window.paint())
        print(self.__button.paint())

class ApplicationConfigurator:
    def __init__(self):
        if platform == "linux":
            factory = LinuxFactory()
        elif platform == "darwin":
            factory = MacOSFactory()
        elif platform == "win32":
            factory = WindowsFactory()
        else:
            raise NotImplementedError(f"Not implemented for your platform: {platform}")

        self.__app = Application(factory)

    def app(self):
        return self.__app

app = ApplicationConfigurator().app()
app.createUI()