import random
from typing import Optional, List

from config import max_x_units, max_y_units, SNAKE_COLOR
from util import Vec2, draw_cell

from direction import Direction


class Snake:

    body: List[Vec2] = []
    speed = 30  # units per second
    prev_move = 0
    top_speed = 40

    prev_direction: Direction

    def __init__(self):

        x_rand = random.randint(0, max_x_units - 1)
        y_rand = random.randint(0, max_y_units - 1)

        d_rand = random.randint(1, 4)
        self.direction = Direction(d_rand)
        self.prev_direction = self.direction

        self.body = [Vec2(x_rand, y_rand)]

    def draw(self, display):

        for cell in self.body:
            draw_cell(display, cell, SNAKE_COLOR)

    def set_direction(self, dir: Direction):

        # check if direction change is possible
        if self.direction == Direction.get_opposite(dir) or\
                self.prev_direction == Direction.get_opposite(dir):
            return

        self.direction = dir

        # self.direction = dir

    def get_direction(self) -> Optional[Direction]:
        return self.direction

    def self_collide(self):

        position_list = list(map(lambda x: (x.x, x.y), self.body))
        dictx = {}
        for i in range(len(position_list)):
            if not position_list[i] in dictx:
                dictx[position_list[i]] = 0
            dictx[position_list[i]] += 1
            if dictx[position_list[i]] > 1:
                return True

        return False

    def update(self, dt):

        self.prev_move += dt

        # calculate if a move is needed to be made by the snake
        if (self.prev_move) < (1 / self.speed):
            return

        self.prev_move = 0

        dir = self.direction

        d_change = Vec2(0, 0)
        if dir is not None:
            d_change = dir.get_vector()

        for i in range(len(self.body) - 1, 0, -1):
            # set body of i to i - 1
            self.body[i] = self.body[i-1]

        self.body[0] += d_change

        head_x = self.body[0].x
        head_y = self.body[0].y

        if head_x < 0:
            head_x = max_x_units
        elif head_x >= max_x_units:
            head_x = 0

        if head_y < 0:
            head_y = max_y_units
        elif head_y >= max_y_units:
            head_y = 0

        self.body[0] = Vec2(head_x, head_y)

        self.prev_direction = self.direction

    def check_collision(self, fruit):

        if self.body[0].distanceL1(fruit.pos) == 0:
            return True

        return False

    def increment_speed(self):
        speed = self.speed + 1 / self.speed
        if speed > self.top_speed:
            speed = self.top_speed
        self.speed = speed

    def add_tail(self):

        dir = self.direction

        d_change = Vec2(0, 0)
        if dir is not None:
            d_change = dir.get_vector()

        pos = d_change + self.body[0]

        self.body = [pos, *self.body]
