import pygame as pg

from .container import Container


class ContainerRows(Container):
    def move(self, x: int, y: int) -> None:
        self.rect.topleft = x, y

    def resize(self, width: int, height: int) -> None:
        self.rect.size = width, height

    def draw(self, display: pg.Surface) -> None:
        for i, el in enumerate(self.contain):
            el.move(self.rect.x + self.padding,
                    self.rect.y + (self.rect.height // len(self.contain)) * i + self.padding)
            el.resize(self.rect.width - self.padding * 2,
                      self.rect.height // len(self.contain) - self.padding * 2)
            el.draw(display)
