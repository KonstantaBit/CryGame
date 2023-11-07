from abc import ABC, abstractmethod
from pygame.surface import Surface


class SceneObjectInterface(ABC):
    @abstractmethod
    def draw(self, display: Surface) -> None:
        pass

    @abstractmethod
    def run(self, display: Surface) -> None:
        self.draw(display)
