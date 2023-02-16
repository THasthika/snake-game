


import pygame
import scenes
from scenes.scene import Scene
from ui.button import Button

from ui.text import AnchorType, Text
from util import Vec2


class MenuScene(Scene):

    name = "MENU"

    def __init__(self):
        super().__init__()
        
        self.should_run = True

    def handle_new_game(self):

        self.scene_manager.push(scenes.get_scene_cls(scenes.GAME_SCENE)())

    def exit_game(self):

        pygame.event.post(pygame.event.Event(pygame.QUIT))

    def setup(self):

        self.title = Text("Snake Game", color=(0, 0, 255), size=50, pos=Vec2(400, 200), anchor=AnchorType.CENTER)

        self.btn_new_game = Button("New Game", color=(0, 255, 0), size=30, pos=Vec2(400, 400), anchor=AnchorType.CENTER, on_click=self.handle_new_game)
        self.btn_quit = Button("Quit", color=(255, 0, 0), size=30, pos=Vec2(400, 450), anchor=AnchorType.CENTER, on_click=self.exit_game)

    def osbcuring(self):

        self.should_run = False

    def handle_event(self, event: pygame.event.Event):

        if not self.should_run:
            return

        self.btn_new_game.handle_event(event)
        self.btn_quit.handle_event(event)

    # def handle_game_command(self, command: GameCommand):
    #     if command.type == CommandType.DIRECTION:
    #         self.snake.set_direction(command.payload)

    def update(self, dt):

        if not self.should_run:
            return

    def render(self, display: pygame.Surface):

        if not self.should_run:
            return

        self.title.render(display)
        self.btn_new_game.render(display)
        self.btn_quit.render(display)

    def revealed(self):

        self.should_run = True

    def cleanup(self):
        pass