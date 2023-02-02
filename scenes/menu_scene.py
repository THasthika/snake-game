


import pygame
from scenes.scene_manager import SceneManager
from ui.button import Button

from ui.text import AnchorType, Text
from util import Vec2


class MenuScene:

    name = "MENU"

    def __init__(self, display: pygame.Surface):

        self.display = display

    def handle_new_game(self):

        print("Moving to new game!")

        SceneManager(self.display).load_scene("GAME")

    def setup(self):

        self.title = Text("Snake Game", color=(0, 255, 0), size=50, pos=Vec2(400, 200), anchor=AnchorType.CENTER)

        self.new_game_button = Button("New Game", color=(255, 0, 0), size=30, pos=Vec2(400, 400), anchor=AnchorType.CENTER, on_click=self.handle_new_game)
        pass

    def handle_event(self, event: pygame.event.Event):

        self.new_game_button.handle_event(event)

        pass

    # def handle_game_command(self, command: GameCommand):
    #     if command.type == CommandType.DIRECTION:
    #         self.snake.set_direction(command.payload)

    def update(self, dt):

        pass

    def render(self):
        self.title.render(self.display)
        self.new_game_button.render(self.display)
        pass

    def cleanup(self):
        pass