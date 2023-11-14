from abc import ABC, abstractmethod
from pygame.surface import Surface


class SceneObjectInterface(ABC):
    @abstractmethod
    def draw(self, display: Surface) -> None:
        pass
