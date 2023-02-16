import pygame
from scenes.game_scene import GameScene
from scenes.scene import Scene
from ui.anchor_type import AnchorType
from ui.button import Button
from ui.text import Text
from util import Vec2

from config import WINDOW_HEIGHT, WINDOW_WIDTH

class PauseGameScene(Scene):

    def __init__(self, game_ref: GameScene):
        super().__init__()

        self.game_ref = game_ref

    def on_resume(self):

        self.scene_manager.pop()

    def on_quit(self):

        self.game_ref.should_exit()
        self.scene_manager.pop()

    def setup(self):

        self.title = Text("Game Paused", color=(0, 0, 255), size=50, pos=Vec2(400, 200), anchor=AnchorType.CENTER)
        self.btn_resume = Button("Resume", size=30, pos=Vec2(400, 400), color=(0, 255, 0), anchor=AnchorType.CENTER, on_click=self.on_resume)
        self.btn_quit = Button("Quit", size=30, pos=Vec2(400, 450), color=(255, 0, 0), anchor=AnchorType.CENTER, on_click=self.on_quit)

    def osbcuring(self):
        pass

    def handle_event(self, event: pygame.event.Event):

        if event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE:
            self.scene_manager.pop()
            return True

        if self.btn_resume.handle_event(event):
            return True

        if self.btn_quit.handle_event(event):
            return True


    def update(self, dt):
        pass

    def render(self, display: pygame.Surface):
        
        ## render alpha channeled rect
        s = pygame.Surface((WINDOW_WIDTH,WINDOW_HEIGHT), pygame.SRCALPHA)   # per-pixel alpha
        s.fill((100,100,100,200))                         # notice the alpha value in the color
        display.blit(s, (0,0))

        self.title.render(display)

        self.btn_resume.render(display)

        self.btn_quit.render(display)

    def revealed(self):
        pass

    def cleanup(self):
        pass