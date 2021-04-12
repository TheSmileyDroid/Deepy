import pygame
import objects
import camera
from pytmx.util_pygame import load_pygame
from states.base_state import State

WIDTH = 320
HEIGHT = 224


class GameState(State):
    def __init__(self):
        self.cam = camera.Camera()

        self.all_objects = pygame.sprite.Group()

        tiled_map = load_pygame("./resources/deepy_tilemap.tmx")
        self.tiles = pygame.sprite.Group()
        for i in range(tiled_map.width):
            for j in range(tiled_map.height):
                sur = tiled_map.get_tile_image(i, j, 0)
                if sur is not None:
                    sprite = pygame.sprite.Sprite()
                    sprite.surf = sur
                    sprite.rect = pygame.Rect(i*8, j*8, 8, 8)
                    self.tiles.add(sprite)

        p = tiled_map.get_object_by_name("Player")
        self.Player = objects.Submarino(
            self.tiles, pygame.Vector2(p.x, p.y))
        self.all_objects.add(self.Player)

        self.vignette = pygame.image.load("./resources/vig.png")

    def Loop(self, DISPLAY, dt):
        self.all_objects.update(dt)
        self.cam.Update(self.Player)

        for tile in self.tiles:
            DISPLAY.blit(tile.surf, self.cam.apply(tile))

        for obj in self.all_objects:
            DISPLAY.blit(obj.surf, self.cam.apply(obj))

        dark = pygame.surface.Surface((WIDTH, HEIGHT))

        dark.fill(pygame.color.Color('White'))

        ppos = self.cam.apply(self.Player).center
        dark.blit(self.vignette, (ppos[0]-WIDTH/2, ppos[1]-HEIGHT/2))

        DISPLAY.blit(dark, (0, 0), special_flags=pygame.BLEND_RGBA_SUB)
