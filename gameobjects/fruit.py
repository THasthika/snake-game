import random
from config import max_x_units, max_y_units, FRUIT_COLOR
from util import Vec2, draw_cell

class Fruit():

    def check_overlap(p, search_pos):

        return p in search_pos

    def __init__(self, snake_positions):

        x_snake_pos = map(lambda x: x.x, snake_positions)
        y_snake_pos = map(lambda x: x.y, snake_positions)

        x_rand = random.randint(0, max_x_units - 1)
        y_rand = random.randint(0, max_y_units - 1)

        while Fruit.check_overlap(x_rand, x_snake_pos):
            x_rand = random.randint(0, max_x_units - 1)

        while Fruit.check_overlap(y_rand, y_snake_pos):
            y_rand = random.randint(0, max_y_units - 1)

        self.pos = Vec2(x_rand, y_rand)

    def draw(self, display):

        draw_cell(display, self.pos, FRUIT_COLOR)

    def get_position(self):
        
        return self.pos