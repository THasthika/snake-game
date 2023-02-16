## Font management class

import pygame


class FontManager(object):

    _instance = None
    fonts = {}

    def __init__(self):

        # if not hasattr(FontManager, 'fonts'):
        #     FontManager.fonts = {}

        pass

    def __new__(cls):
        if cls._instance is None:
            
            print("Creating FontManager class!")
            cls._instance = super(FontManager, cls).__new__(cls)


        return cls._instance


    def get_font(self, name: str, size) -> pygame.font.Font:

        if not name in self.fonts:
            self.fonts[name] = {}

        if not size in self.fonts:
            try:
                if name.endswith(".ttf"):
                    self.fonts[name][size] = pygame.font.Font(name, size)
                else:
                    self.fonts[name][size] = pygame.font.SysFont(name, size)
            except Exception as e:
                print("FAILED TO LOAD FONT {}".format(name))
                raise e

        return self.fonts[name][size]
