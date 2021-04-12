import pygame

WIDTH = 320
HEIGHT = 224
LOCATION = (12, 176)
LIMIT = 296


def drawText(surface, text, color, rect, font, aa=False, bkg=None):
    rect = pygame.Rect(rect)
    y = rect.top
    lineSpacing = -2

    # get the height of the font
    fontHeight = font.size("Tg")[1]

    while text:
        i = 1

        # determine if the row of text will be outside our area
        if y + fontHeight > rect.bottom:
            break

        # determine maximum width of line
        while font.size(text[:i])[0] < rect.width and i < len(text):
            i += 1

        # if we've wrapped the text, then adjust the wrap to the last word
        if i < len(text):
            i = text.rfind(" ", 0, i) + 1

        # render the line and blit it to the surface
        if bkg:
            image = font.render(text[:i], 1, color, bkg)
            image.set_colorkey(bkg)
        else:
            image = font.render(text[:i], aa, color)

        surface.blit(image, (rect.left, y))
        y += fontHeight + lineSpacing

        # remove the text we just blitted
        text = text[i:]

    return text


class Dialog():
    def __init__(self, *args):
        self.box = pygame.image.load('resources/dialog.png')
        self.font = pygame.font.Font('resources/monogram.ttf', 16)
        self.texts = list(args)
        self.actual_text = ''
        self.leave = False
        self.ended = True

    def draw(self, display: pygame.surface.Surface):
        if not self.ended:
            display.blit(self.box, (0, 0))
        pressed = pygame.key.get_pressed()

        if not pressed[pygame.K_z] and self.leave:
            self.leave = False

        if len(self.texts) > 0:
            if self.actual_text == '':
                self.actual_text = self.texts.pop(0)
                self.ended = False
            if pressed[pygame.K_z] and not self.leave:
                self.actual_text = self.texts.pop(0)
                self.ended = False
                self.leave = True
        else:
            if pressed[pygame.K_z] and not self.leave:
                self.ended = True
                self.leave = True

        if self.actual_text == '':
            self.ended = True

        if not self.ended:
            drawText(display,
                     self.actual_text,
                     pygame.Color("White"),
                     (LOCATION, (WIDTH-24, HEIGHT-24)),
                     self.font)

    def append(self, text, *args):
        self.texts.append(text)
        for t in args:
            self.texts.append(t)
        self.actual_text = self.texts.pop(0)
        self.ended = False
