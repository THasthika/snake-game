from typing import Optional
import pygame
from controllers import Controller, AIControllerV1, AIControllerV2, AIControllerV3, HumanController
from game_command import CommandType, GameCommand

from gameobjects import Fruit, Snake
import scenes
from scenes.scene import Scene

from util import draw_text

from config import WINDOW_WIDTH

PERSIST_CONTROLLER = True


def create_controller(snake: Snake, fruit: Optional[Fruit]) -> Controller:
    return AIControllerV2(snake, fruit)

class GameScene(Scene):

    score = 0
    is_paused = False
    is_quitting = False

    def __init__(self):

        super().__init__()

    def setup(self):

        self.snake = Snake()
        self.fruit = Fruit(self.snake.body)
        self.controller = create_controller(self.snake, self.fruit)

    def osbcuring(self):

        self.is_paused = True

    def handle_event(self, event: pygame.event.Event):

        if self.is_paused:
            return

        if event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE:
            self.scene_manager.push(scenes.get_scene_cls(scenes.PAUSE_GAME_SCENE)(self))

        c = self.controller.handle_event(event)
        if c is not None:
            self.handle_game_command(c)

    def handle_game_command(self, command: GameCommand):

        if command.type == CommandType.DIRECTION:
            self.snake.set_direction(command.payload)

    def update(self, dt):

        if self.is_paused:
            return

        if self.is_quitting:
            self.scene_manager.pop()

        c = self.controller.handle_update()
        if c is not None:
            self.handle_game_command(c)

        self.snake.update(dt)

        if self.snake.self_collide():
            # new snake needed
            self.snake = Snake()
            if PERSIST_CONTROLLER:
                self.controller.set_snake(self.snake)
            else:
                self.controller = create_controller(self.snake, self.fruit)
            self.score = 0

        if self.snake.check_collision(self.fruit):
            self.snake.add_tail()
            self.snake.increment_speed()
            self.fruit = Fruit(self.snake.body)
            self.score += 1
            self.controller.set_fruit(self.fruit)

        self.controller.set_score(self.score)

    def render(self, display: pygame.Surface):

        self.snake.draw(display)

        self.fruit.draw(display)

        draw_text(display, "Score: {}".format(self.score), WINDOW_WIDTH - 100, 50)

    def revealed(self):

        self.is_paused = False

    def cleanup(self):
        pass

    def should_exit(self):

        self.is_quitting = True