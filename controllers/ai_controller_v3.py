from typing import Optional
import pygame
from controllers.controller import Controller
from config import max_x_units, max_y_units
from direction import Direction
from game_command import CommandType, GameCommand
from gameobjects import Snake, Fruit
import numpy as np
import sys


np.set_printoptions(threshold=sys.maxsize)


class GameState():

    def __init__(self, board, prev_outcome):

        self.board = board
        self.prev_outcome = prev_outcome

    def __str__(self) -> str:
        return "{}\n{}".format(self.board, self.prev_outcome)

# AI with RL


class AIControllerV3(Controller):

    def __init__(self, snake: Snake, fruit: Optional[Fruit] = None):
        self.snake = snake
        self.fruit = fruit
        self.score = 0
        self.prev_score = 0

    def set_score(self, score: int):
        self.prev_score = self.score
        self.score = score

    def set_fruit(self, fruit: Fruit):
        self.fruit = fruit

    def set_snake(self, snake):
        self.snake = snake

    def get_state(self) -> GameState:

        snake_body = self.snake.body[1:]
        head_location = self.snake.body[0]
        fruit_location = self.fruit.pos
        prev_outcome = 0

        b = np.zeros((max_x_units, max_y_units), dtype=np.ushort)

        b[head_location.y % max_y_units, head_location.x % max_x_units] = 2

        for x in snake_body:
            b[x.y % max_y_units, x.x % max_x_units] = 1

        b[fruit_location.y % max_y_units, fruit_location.x % max_x_units] = 3

        diff = self.score - self.prev_score
        if diff > 0:
            prev_outcome = 1
        elif diff < 0:
            prev_outcome = -1

        game_state = GameState(b, prev_outcome)
        return game_state

    # called on every event

    def handle_event(self, _event: pygame.event.Event)\
            -> Optional[GameCommand]:

        return None

    # called on every frame
    def handle_update(self) -> Optional[GameCommand]:

        game_state = self.get_state()

        print(game_state)

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
