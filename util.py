import math
import pygame

from config import CELL_SIZE, FONT_SIZE, TEXT_COLOR, SCREEN_COLOR

fonts = {}

def init_fonts():
    global fonts
    fonts = {
        "arial": pygame.font.SysFont("arial", FONT_SIZE)
    }

def draw_cell(display, pos, color):
    pygame.draw.rect(display, color,
        (
            pos.x * CELL_SIZE,
            pos.y * CELL_SIZE,
            CELL_SIZE,
            CELL_SIZE
        )
    )

def draw_text(display, text, x, y, font_name = "arial"):
    font = fonts[font_name]
    text_surf = font.render(text, True, TEXT_COLOR)
    textRect = text_surf.get_rect()
    textRect.center = (x, y)
    display.blit(text_surf, textRect)


class Vec2:

    x = 0
    y = 0

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Vec2(self.x + other, self.y + other)

        if hasattr(other, 'x') and hasattr(other, 'y'):
            return Vec2(self.x + other.x, self.y + other.y)

        raise TypeError()

    def __sub__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Vec2(self.x - other, self.y - other)

        if hasattr(other, 'x') and hasattr(other, 'y'):
            return Vec2(self.x - other.x, self.y - other.y)

        raise TypeError()

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Vec2(self.x * other, self.y * other)

        if hasattr(other, 'x') and hasattr(other, 'y'):
            return Vec2(self.x * other.x, self.y * other.y)

        raise TypeError()

    def __truediv__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Vec2(self.x / other, self.y / other)

        if hasattr(other, 'x') and hasattr(other, 'y'):
            return Vec2(self.x / other.x, self.y / other.y)

        raise TypeError()

    def __floordiv__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Vec2(self.x // other, self.y // other)

        if hasattr(other, 'x') and hasattr(other, 'y'):
            return Vec2(self.x // other.x, self.y // other.y)

        raise TypeError()

    def dot_product(self, other):
        return self.x * other.x + self.y * other.y

    def distance(self, other):
        return self.distanceL2(other)

    def distanceL2(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def distanceL1(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)

    def magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def unit_vector(self):
        return self / self.magnitude()

    def __repr__(self) -> str:
        return "Vec2({}, {})".format(self.x, self.y)

    def __hash__(self) -> int:
        return (self.x, self.y).__hash__()

    def __iter__(self):
        for x in (self.x, self.y):
            yield x