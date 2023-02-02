from typing import Optional

import pygame
from controllers.controller import Controller

from direction import Direction
from game_command import CommandType, GameCommand

from gameobjects import Snake, Fruit

class HumanController(Controller):

    def __init__(self, snake: Snake, fruit: Optional[Fruit] = None):
        self.snake = snake
        self.fruit = fruit

    def set_fruit(self, fruit: Fruit):
        self.fruit = fruit

    ## called on every event
    def handle_event(self, event: pygame.event.Event) -> Optional[GameCommand]:
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                return GameCommand(CommandType.DIRECTION, Direction.WEST)
            if event.key == pygame.K_s:
                return GameCommand(CommandType.DIRECTION, Direction.SOUTH)
            if event.key == pygame.K_d:
                return GameCommand(CommandType.DIRECTION, Direction.EAST)
            if event.key == pygame.K_w:
                return GameCommand(CommandType.DIRECTION, Direction.NORTH)

    ## called on every frame
    def handle_update(self) -> Optional[GameCommand]:

        return None