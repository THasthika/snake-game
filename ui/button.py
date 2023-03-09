import pygame
from config import TEXT_COLOR, DEFAULT_FONT
from ui.anchor_type import AnchorType
from ui.font_manager import FontManager
from util import Vec2, hex_to_color_tuple


BUTTON_BG_COLOR = hex_to_color_tuple("#aaa")
BUTTON_BG_HOVER_COLOR = hex_to_color_tuple("#555")


class Button():

    def __init__(self, text: str, font=None, size=30, pos: Vec2 = Vec2(0, 0),
                 color=TEXT_COLOR, anchor=AnchorType.CENTER, on_click=None,
                 pad_x=10, pad_y=10):
        font = font if font is not None else DEFAULT_FONT
        self.size = size
        self.pos = pos
        self.color = color
        self.text = text
        self.anchor = anchor
        self.font = FontManager().get_font(font, self.size)
        self.on_click = on_click
        self.focused = False
        self.padding_x = pad_x
        self.padding_y = pad_y

        self.update_surface()

    def update_rect_anchor(self):
        if self.anchor == AnchorType.CENTER:
            self.rect.center = (self.pos.x, self.pos.y)
        elif self.anchor == AnchorType.TOP_LEFT:
            self.rect.topleft = (self.pos.x, self.pos.y)
        elif self.anchor == AnchorType.TOP_RIGHT:
            self.rect.topright = (self.pos.x, self.pos.y)
        elif self.anchor == AnchorType.BOTTOM_LEFT:
            self.rect.bottomleft = (self.pos.x, self.pos.y)
        elif self.anchor == AnchorType.BOTTOM_RIGHT:
            self.rect.bottomright = (self.pos.x, self.pos.y)

    def update_surface(self):

        text_surface = self.font.render(self.text, True, self.color if not
                                        self.focused else
                                        (255 - self.color[0],
                                         255 - self.color[1],
                                         255 - self.color[2]))
        self.surface = pygame.Surface((
            text_surface.get_size()[0] + self.padding_x * 2,
            text_surface.get_size()[1] + self.padding_y * 2))
        if self.focused:
            self.surface.fill(BUTTON_BG_HOVER_COLOR)
        else:
            self.surface.fill(BUTTON_BG_COLOR)
        self.surface.blit(text_surface, (self.padding_x, self.padding_y))
        self.rect = self.surface.get_rect()
        self.update_rect_anchor()

    def handle_event(self, event: pygame.event.Event):

        if event.type == pygame.MOUSEMOTION:

            (x, y) = event.pos
            if x >= self.rect.left and x <= self.rect.right and \
                    y >= self.rect.top and y <= self.rect.bottom \
                    and not self.focused:
                self.focused = True
                self.update_surface()
            elif not (x >= self.rect.left and
                      x <= self.rect.right and y >= self.rect.top
                      and y <= self.rect.bottom) and self.focused:
                self.focused = False
                self.update_surface()

        if event.type == pygame.MOUSEBUTTONUP:

            (x, y) = event.pos
            if x >= self.rect.left and x <= self.rect.right and \
                    y >= self.rect.top and y <= self.rect.bottom and \
                    self.on_click is not None:
                self.on_click()

    def render(self, display: pygame.Surface):
        display.blit(self.surface, self.rect)

    def set_text(self, text: str):
        self.text = text
        self.update_surface()

    def set_pos(self, pos: Vec2):
        self.pos = pos
        self.update_surface()
