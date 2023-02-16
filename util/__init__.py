import pygame

from config import CELL_SIZE, FONT_SIZE, TEXT_COLOR

from .vec2 import Vec2

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

def hex_to_short(hex: str):

        r = 0
        if len(hex) > 2:
            raise Exception("Invalid Hex Value: {}".format(hex))
        
        t_v = ord(hex[0]) - ord('0')
        if t_v > 10:
            t_v = ord(hex[0]) - ord('a') + 10

        r += t_v * 16

        t_v = ord(hex[1]) - ord('0')
        if t_v > 10:
            t_v = ord(hex[1]) - ord('a') + 10
        
        r += t_v

        return r

def hex_to_color_tuple(hex: str):
    

    t_hex = hex

    if hex.startswith("#"):
        t_hex = hex[1:]

    t_hex = t_hex.lower()

    if len(t_hex) == 3:
        t_hex = "{}{}{}{}{}{}".format(t_hex[0], t_hex[0], t_hex[1], t_hex[1], t_hex[2], t_hex[2])
    if len(t_hex) == 4:
        t_hex = "{}{}{}{}{}{}{}{}".format(t_hex[0], t_hex[0], t_hex[1], t_hex[1], t_hex[2], t_hex[2], t_hex[3], t_hex[3])

    if len(t_hex) != 6 and len(t_hex) != 8:
        raise Exception("Invalid Hex Color Code: {}".format(hex))
    
    if len(t_hex) == 6:
        return (hex_to_short(t_hex[0:2]), hex_to_short(t_hex[2:4]), hex_to_short(t_hex[4:6]))
    
    return (hex_to_short(t_hex[0:2]), hex_to_short(t_hex[2:4]), hex_to_short(t_hex[4:6]), hex_to_short(t_hex[6:8]))