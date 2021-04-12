import pygame

WIDTH = 320
HEIGHT = 224


class Camera():
    camera = pygame.Rect(0, 0, WIDTH, HEIGHT)
    width = WIDTH
    height = HEIGHT

    def apply(self, entity) -> pygame.Rect:
        return entity.rect.move(self.camera.topleft)

    def Update(self, target):
        x = -target.rect.x + int(WIDTH / 2)
        y = -target.rect.y + int(HEIGHT / 2)

        x = min(0, x)
        x = max(-8*100, x)
        y = min(0, y)
        y = max(-8*100, y)

        self.camera = pygame.Rect(x, y, self.width, self.height)
