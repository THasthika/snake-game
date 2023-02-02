from enum import Enum

from util import Vec2

class Direction(Enum):
    NORTH = 1
    SOUTH = 2
    EAST = 3
    WEST = 4

    def get_opposite(dir):
        if dir == Direction.NORTH:
            return Direction.SOUTH
        if dir == Direction.SOUTH:
            return Direction.NORTH
        if dir == Direction.EAST:
            return Direction.WEST
        if dir == Direction.WEST:
            return Direction.EAST

    def get_vector(self):

        if self == Direction.EAST:
            return Vec2(1, 0)
        if self == Direction.WEST:
            return Vec2(-1, 0)
        if self == Direction.NORTH:
            return Vec2(0, -1)
        if self == Direction.SOUTH:
            return Vec2(0, 1)

        return Vec2(0, 0)