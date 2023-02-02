from abc import ABC, abstractmethod
from typing import Optional

import pygame

from game_command import GameCommand

class Controller(ABC):

    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def handle_event(self, event: pygame.event.Event) -> Optional[GameCommand]:
        pass

    @abstractmethod
    def handle_update(self) -> Optional[GameCommand]:
        pass