import pygame

import random
from enum import Enum

from config import WINDOW_HEIGHT, WINDOW_WIDTH, SCREEN_COLOR, FPS, START_SCENE
import scenes
from scenes.scene_manager import SceneManager
from ui.font_manager import FontManager

from util import init_fonts

from scenes import GameScene, MenuScene

pygame.init()

init_fonts()

display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

running = True

dt = clock.tick(30)

# scene manager
scene_manager = SceneManager(display)
scene_manager.push(scenes.get_scene_cls(scenes.MENU_SCENE)(display))

while running:

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
    scene_manager.render()

    pygame.display.update()

    dt = clock.tick(FPS)

pygame.quit()
