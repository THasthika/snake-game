import pygame

class SpriteSheet:

    def __init__(self, filename):

        try:
            self.sheet = pygame.image.load(filename)
        except pygame.error as message:
            print(('Unable to load spritesheet image:', filename))
            raise SystemExit(message)
        
    def image_at(self, rectangle, colorkey = None):
        """
        rectangle: (x, y, x-offset, y-offset)
        """

        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size).convert()
        image.blit(self.sheet, (0, 0), rect)
        if colorkey is not None:
            if colorkey == -1:
                colorkey = image.get_at((0,0))
            image.set_colorkey(colorkey, pygame.RLEACCEL)
        return image