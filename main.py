import pygame

import random
from enum import Enum

from config import WINDOW_HEIGHT, WINDOW_WIDTH, SCREEN_COLOR, FPS
import scenes
from scenes.scene_manager import SceneManager
from ui.font_manager import FontManager

from util import init_fonts

pygame.init()

init_fonts()

display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

running = True

# scene manager
scene_manager = SceneManager()
scene_manager.push(scenes.get_scene_cls(scenes.MENU_SCENE)())

while running:

    dt = clock.tick(FPS) / 1000.0

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
            break

        # scene handle event

        scene_manager.handle_event(event)

    # scene update
    scene_manager.update(dt)

    display.fill(SCREEN_COLOR)

    # scene render
    scene_manager.render(display)

    pygame.display.update()

    dt = clock.tick(FPS)

pygame.quit()
