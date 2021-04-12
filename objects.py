import pygame

FRICTION = -0.12


class GameObject(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.pos = pygame.Vector2(100, 100)
        self.vel = pygame.Vector2(0, 0)
        self.acc = pygame.Vector2(0, 0)

    def update(self, delta):
        pass

    def move(self, delta):
        self.acc.y += self.vel.y * FRICTION
        self.acc.x += self.vel.x * FRICTION

        self.vel += self.acc
        self.pos += self.vel * delta + 0.5 * self.acc * delta
        self.rect.midbottom = self.pos


class Submarino(GameObject):
    def __init__(self, tiles: pygame.sprite.Group, position: pygame.Vector2):
        super().__init__()
        self.surf = pygame.image.load("./resources/submarino.png")
        self.flip = False
        self.rect = self.surf.get_rect()
        self.tiles = tiles
        self.pos = position
        self.rect.midbottom = position

    def update(self, delta):
        self.acc = pygame.Vector2(0, 0)
        pressed_keys = pygame.key.get_pressed()
        self.acc.x = int(pressed_keys[pygame.K_d]) - \
            int(pressed_keys[pygame.K_a])
        self.acc.y = int(pressed_keys[pygame.K_s]) - \
            int(pressed_keys[pygame.K_w])
        if self.acc.x > 0 and self.flip:
            self.flip = False
            self.surf = pygame.transform.flip(self.surf, True, False)
        if self.acc.x < 0 and not self.flip:
            self.flip = True
            self.surf = pygame.transform.flip(self.surf, True, False)
        self.move(delta*10)

    def move(self, delta):
        self.acc.y += self.vel.y * FRICTION
        self.acc.x += self.vel.x * FRICTION

        self.vel += self.acc
        ppos = self.pos.xy
        self.pos += self.vel * delta + 0.5 * self.acc * delta
        self.rect.midbottom = self.pos
        for tile in self.tiles:
            if abs(tile.rect.centerx - self.rect.centerx) < 16:
                if abs(tile.rect.centery - self.rect.centery) < 16:
                    if pygame.sprite.collide_rect(self, tile):
                        self.pos = ppos
                        self.rect.midbottom = ppos
                        self.vel.x = 0
                        self.vel.y = 0
                        self.acc.x = 0
                        self.acc.y = 0


class SubmarinoVazio(Submarino):
    def __init__(self, x, tiles):
        super().__init__(tiles, pygame.Vector2(x, 40))
        self.rect.midbottom = self.pos

    def update(self, delta):
        pass
