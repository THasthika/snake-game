from abc import ABC, abstractmethod

import pygame

from scenes.scene_manager import SceneManager

class Scene(ABC):

    def __init__(self) -> None:
        super().__init__()

        self.scene_manager = SceneManager()

    @abstractmethod
    def setup(self):
        pass

    @abstractmethod
    def osbcuring(self):
        pass

    @abstractmethod
    def handle_event(self, event: pygame.event.Event) -> bool:
        pass

    @abstractmethod
    def update(self, dt):
        pass

    @abstractmethod
    def render(self, display):
        pass

    @abstractmethod
    def revealed(self):
        pass

    @abstractmethod
    def cleanup(self):
        pass