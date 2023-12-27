from src.CryGame import SceneInterface, SaveManager, Pos
from src.Render import Render
from src.Entity import Dwarf, ProbeFlag
import pygame as pg
import sys
import copy
from constants import CHUNK_SIZE


class WorldScene(SceneInterface):
    def __init__(self):
        super().__init__()
        render = Render(Pos(0, 0))
        self.add_scene_object(render)
        self.sm = SaveManager()
        self.player = Dwarf(Pos(0, 0))
        self.sm.current.players.append(self.player)
        self.sm.current.players.append(ProbeFlag(Pos(10, 10), pg.Color(255, 0, 0), ''))

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_b:
                    x = int(self.player.position.x // CHUNK_SIZE)
                    y = int(self.player.position.y // CHUNK_SIZE)
                    xb = int(self.player.position.x % CHUNK_SIZE)
                    yb = int(self.player.position.y % CHUNK_SIZE)
                    print(self.sm.current.chunks[(x, y)].blocks[xb][yb].contain)
                    if "Iron" in self.sm.current.chunks[(x, y)].blocks[xb][yb].contain:
                        self.sm.current.entities.append(ProbeFlag(copy.copy(self.player.position), pg.Color(115, 58, 25), 'Бурый железняк'))
                    elif "Copper" in self.sm.current.chunks[(x, y)].blocks[xb][yb].contain:
                        self.sm.current.entities.append(ProbeFlag(copy.copy(self.player.position), pg.Color(252, 126, 48), 'Малахит'))
                    elif "Silver" in self.sm.current.chunks[(x, y)].blocks[xb][yb].contain:
                        self.sm.current.entities.append(ProbeFlag(copy.copy(self.player.position), pg.Color(174, 232, 220), 'Самородное серебро'))
                    elif "Lead" in self.sm.current.chunks[(x, y)].blocks[xb][yb].contain:
                        self.sm.current.entities.append(ProbeFlag(copy.copy(self.player.position), pg.Color(85, 115, 109), 'Галенит'))
                    else:
                        self.sm.current.entities.append(ProbeFlag(copy.copy(self.player.position), pg.Color(255, 0, 0), 'Ничего'))
