from enum import Enum
from config import TEXT_COLOR
from ui.anchor_type import AnchorType
from ui.font_manager import FontManager
from util import Vec2

class Text():

    def __init__(self, text: str, font = None, size = 30, pos: Vec2 = Vec2(0, 0), color = TEXT_COLOR, anchor = AnchorType.CENTER):
        font = font if font is not None else "arial"
        self.size = size
        self.pos = pos
        self.color = color
        self.text = text
        self.anchor = anchor
        self.font = FontManager().get_font(font, self.size)

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
        self.surface = self.font.render(self.text, True, self.color)
        self.rect = self.surface.get_rect()
        self.update_rect_anchor()

    def render(self, display):
        display.blit(self.surface, self.rect)

    def set_text(self, text: str):
        self.text = text
        self.update_surface()

    def set_pos(self, pos: Vec2):
        self.pos = pos
        self.update_surface()
