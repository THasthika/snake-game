from typing import Optional
import pygame
from controllers import Controller, AIControllerV1, HumanController
from game_command import CommandType, GameCommand

from gameobjects import Fruit, Snake

from util import draw_text

from config import WINDOW_WIDTH

from direction import Direction

def create_controller(snake: Snake, fruit: Optional[Fruit]) -> Controller:
    return AIControllerV1(snake, fruit)

class GameScene():

    name = "GAME"

    score = 0

    def __init__(self, display: pygame.Surface):

        self.display = display

    def setup(self):

        self.snake = Snake()
        self.fruit = Fruit(self.snake.body)
        self.controller = create_controller(self.snake, self.fruit)

    def handle_event(self, event: pygame.event.Event):

        c = self.controller.handle_event(event)
        if c is not None:
            self.handle_game_command(c)

    def handle_game_command(self, command: GameCommand):
        if command.type == CommandType.DIRECTION:
            self.snake.set_direction(command.payload)

    def update(self, dt):

        c = self.controller.handle_update()
        if c is not None:
            self.handle_game_command(c)

        self.snake.update(dt)

        if self.snake.self_collide():
            # new snake needed
            self.snake = Snake()
            self.controller = create_controller(self.snake, self.fruit)
            self.score = 0

        if self.snake.check_collision(self.fruit):
            self.snake.add_tail()
            self.snake.increment_speed()
            self.fruit = Fruit(self.snake.body)
            self.score += 1
            self.controller.set_fruit(self.fruit)

    def render(self):

        self.snake.draw(self.display)

        self.fruit.draw(self.display)

        draw_text(self.display, "Score: {}".format(self.score), WINDOW_WIDTH - 100, 50)

    def cleanup(self):

        pass