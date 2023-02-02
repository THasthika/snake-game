from enum import Enum

from direction import Direction


class CommandType(Enum):

    DIRECTION = 1

class GameCommand():

    def __init__(self, type: CommandType, payload: Direction):
        self.type = type
        self.payload = payload

    def __str__(self) -> str:
        
        return "Type: {} | Payload: {}".format(self.type, self.payload)
