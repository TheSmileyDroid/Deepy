import pygame
from states.base_state import State
from states.game_state import GameState
import pytweening as tween

WIDTH = 320
HEIGHT = 224


class SplashState(State):
    def __init__(self, state):
        self.img = pygame.image.load("./resources/SmileyDroid.png")
        self.img_rect = self.img.get_rect()
        self.state = state

        self.img_rect.center = (WIDTH/2, HEIGHT/2)
        self.time = 0
        self.font = pygame.font.Font('resources/monogram.ttf', 32)
        self.text = self.font.render(
            "By SmileyDroid", False, pygame.Color('White'))

    def Loop(self, DISPLAY: pygame.surface.Surface, dt):
        DISPLAY.blit(self.img, self.img_rect)
        DISPLAY.blit(
            self.text,
            (WIDTH/2 - self.text.get_width()/2,
             HEIGHT*3/4 - self.text.get_height()/2)
        )
        self.time += dt
        if self.time <= 4:
            sur = pygame.surface.Surface((WIDTH, HEIGHT))
            sur.fill(pygame.Color(0, 0, 0))
            sur.set_alpha(255-255*tween.easeInOutSine(self.time/4))
            DISPLAY.blit(sur, (0, 0))
        elif self.time <= 8:
            sur = pygame.surface.Surface((WIDTH, HEIGHT))
            sur.fill(pygame.Color(0, 0, 0))
            sur.set_alpha(255*tween.easeInOutSine((self.time-4)/4))
            DISPLAY.blit(sur, (0, 0))
        else:
            self.state["atual"] = GameState()
