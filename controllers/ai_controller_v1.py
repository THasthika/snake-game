
import pygame
from typing import Optional
from controllers.controller import Controller
from direction import Direction
from game_command import CommandType, GameCommand
from gameobjects import Snake, Fruit


class AIControllerV1(Controller):

    def __init__(self, snake: Snake, fruit: Optional[Fruit] = None):

        self.snake = snake
        self.fruit = fruit

    def set_fruit(self, fruit: Fruit):
        self.fruit = fruit

    def set_score(self, score):
        self.score = score

    def set_snake(self, snake):
        self.snake = snake

    # called on every event
    def handle_event(self, _event: pygame.event.Event) -> Optional[GameCommand]:

        return None

    # called on every frame
    def handle_update(self) -> Optional[GameCommand]:

        head_pos = self.snake.body[0]
        # snake_direction = self.snake.get_direction()

        fruit_pos = self.fruit.pos

        diff = (head_pos - fruit_pos) // 1

        if diff.x == 0 and diff.y == 0:
            return None

        if abs(diff.x) > 0:

            if diff.x < 0:
                return GameCommand(CommandType.DIRECTION, Direction.EAST)
            elif diff.x > 0:
                return GameCommand(CommandType.DIRECTION, Direction.WEST)

        if abs(diff.y) > 0:

            if diff.y < 0:
                return GameCommand(CommandType.DIRECTION, Direction.SOUTH)
            elif diff.y > 0:
                return GameCommand(CommandType.DIRECTION, Direction.NORTH)

        return None
