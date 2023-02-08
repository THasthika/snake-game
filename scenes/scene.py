from abc import ABC, abstractmethod
from typing import Optional

import pygame

from scenes.scene_manager import SceneManager

class Scene(ABC):

    def __init__(self, display: pygame.surface.Surface) -> None:
        super().__init__()

        self.display = display
        self.scene_manager = SceneManager(self.display)

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
    def render(self):
        pass

    @abstractmethod
    def revealed(self):
        pass

    @abstractmethod
    def cleanup(self):
        pass