import pygame as pg
from abc import ABC
from paths import entities_path
from constants import HEIGHT, WIDTH
import os
from src.CryGame.position import Pos


class Entity(ABC):
    def __init__(self, position: Pos):
        self.texture = None
        self.position: Pos = position
        self.texture: pg.Surface
        self.controllable: bool = False

    def control(self):
        self.controllable = True

    def update(self):
        self.move()

    def move(self):
        pass

    def draw(self, screen: pg.Surface):
        pass

    def teleport(self, x: float, y: float):
        self.position = [x, y]


class Dwarf(Entity):
    def __init__(self, position: [float, float]):
        super().__init__(position)
        self.speed = 0.7
        self.texture = pg.image.load(os.path.join(entities_path, 'down left1.png'))
        self.animation = [[pg.image.load(os.path.join(entities_path, f'{el}{i}.png')) for i in range(1, 5)] for el in ('up', 'up right', 'right', 'down right', 'down', 'down left', 'left', 'up left')]
        self.clock = pg.time.Clock()
        self.time_delay = 0
        self.animation_step = 0
        self.heading = 0

    def move(self):
        keys = pg.key.get_pressed()
        ax = 0
        ay = 0
        if keys[pg.K_LEFT]:
            ax -= self.speed
        if keys[pg.K_RIGHT]:
            ax += self.speed
        if keys[pg.K_UP]:
            ay -= self.speed
        if keys[pg.K_DOWN]:
            ay += self.speed

        if ax == 0 and ay == -self.speed:
            self.heading = 0
        if ax == self.speed and ay == -self.speed:
            self.heading = 1
        if ax == self.speed and ay == 0:
            self.heading = 2
        if ax == self.speed and ay == self.speed:
            self.heading = 3
        if ax == 0 and ay == self.speed:
            self.heading = 4
        if ax == -self.speed and ay == self.speed:
            self.heading = 5
        if ax == -self.speed and ay == 0:
            self.heading = 6
        if ax == -self.speed and ay == -self.speed:
            self.heading = 7

        tick = self.clock.tick()
        self.time_delay += tick
        self.position.x += ax * tick / 100
        self.position.y += ay * tick / 100
        if ay == ax == 0:
            self.texture = self.animation[4][0]
        elif self.time_delay > 100:
            self.time_delay = 0
            self.animation_step += 1
            if self.animation_step == 4:
                self.animation_step = 0
            self.texture = self.animation[self.heading][self.animation_step]
        self.texture = pg.transform.scale(self.texture, (40, 40))

    def draw(self, screen: pg.Surface):
        screen.blit(self.texture, (WIDTH // 2, HEIGHT // 2))


class ProbeFlag(Entity):
    def __init__(self, position: Pos, color: pg.Color):
        super().__init__(position)
        self.texture = pg.Surface((50, 50))
        self.texture.fill(color)