'''Um jogo sobre submarinos'''
import sys
import pygame
from states.game_state import GameState
from states.splash_state import SplashState

pygame.init()


WIDTH = 320
HEIGHT = 224
RESIZE = 2

CLOCK = pygame.time.Clock()
FPS = 30
dt = 0

SCREEN = pygame.display.set_mode(size=(WIDTH*RESIZE, HEIGHT*RESIZE))
DISPLAY = pygame.surface.Surface((WIDTH, HEIGHT))
pygame.display.set_caption("Deepy")
state = {}
state["atual"] = GameState()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    DISPLAY.fill(pygame.Color(0, 0, 0))
    state["atual"].Loop(DISPLAY, dt)

    SCREEN.blit(pygame.transform.scale(
        DISPLAY, (WIDTH*RESIZE, HEIGHT*RESIZE)), (0, 0))
    pygame.display.update()
    dt = CLOCK.tick(FPS)/1000.0
