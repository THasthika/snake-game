from abc import ABC, abstractmethod
from typing import Optional

import pygame

class Scene(ABC):

    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def setup(self):
        pass

    @abstractmethod
    def handle_event(self, event: pygame.event.Event):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def render(self):
        pass

    @abstractmethod
    def cleanup(self):
        pass