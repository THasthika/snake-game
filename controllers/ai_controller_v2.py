
from typing import List, Optional

import pygame
from controllers.controller import Controller
from config import max_x_units, max_y_units

from direction import Direction
from game_command import CommandType, GameCommand

from gameobjects import Snake, Fruit
from util import Vec2

class SearchTree:

    def __init__(self, snake: Snake, fruit: Fruit, depth = 3):

        self.root = TreeNode(snake.body, snake.direction, fruit.pos)
        

class TreeNode:

    children = []
    parent = None

    def __str__(self) -> str:
        return "#Children: {} | Points: {} | Direction: {}".format(len(self.children), self.points, self.direction)

    def __init__(self, snake_body: List[Vec2], direction: Direction, fruit_position: Vec2):
        
        snake_head_position = snake_body[0]

        fruit_direction = (fruit_position - snake_head_position).unit_vector()
        dir_direction = direction.get_vector()

        points = fruit_direction.dot_product(dir_direction)

        self.points = points
        self.direction = direction
        self.snake_body = self.update_snake_body(snake_body, direction)
        self.fruit_position = fruit_position
        self.children = []

        self.possible_directions = list(filter(lambda x: Direction.get_opposite(direction) != x, [Direction.EAST, Direction.WEST, Direction.NORTH, Direction.SOUTH]))

    def update_snake_body(self, snake_body: List[Vec2], direction: Direction):

        for i in range(len(snake_body) - 1, 0, -1):
            ## set body of i to i - 1
            snake_body[i] = snake_body[i-1]

        snake_body[0] += direction.get_vector()

        head_x = snake_body[0].x
        head_y = snake_body[0].y

        if head_x < 0:
            head_x = max_x_units
        elif head_x >= max_x_units:
            head_x = 0
        
        if head_y < 0:
            head_y = max_y_units
        elif head_y >= max_y_units:
            head_y = 0

        snake_body[0] = Vec2(head_x, head_y)

        return snake_body

    def expand_node(self):

        if len(self.children) != 0:
            return

        max_points = 0

        for dir in self.possible_directions:

            node = TreeNode(self.snake_body, dir, self.fruit_position)
            node.parent = self
            self.children.append(node)

            if node.points > max_points:
                max_points = node.points

        t = self
        while t is not None:
            if t.points < max_points:
                t.points = max_points
            else:
                max_points = t.points
            t = t.parent


## AI with tree searching for optimal move
class AIControllerV2(Controller):

    def __init__(self, snake: Snake, fruit: Optional[Fruit] = None):

        self.snake = snake
        self.fruit = fruit

    def set_fruit(self, fruit: Fruit):
        self.fruit = fruit

    def set_snake(self, snake):
        self.snake = snake

    def set_score(self, score):
        self.score = score

    def construct_search_tree(self):

        pass

    ## called on every event
    def handle_event(self, _event: pygame.event.Event) -> Optional[GameCommand]:
        
        return None

    ## called on every frame
    def handle_update(self) -> Optional[GameCommand]:

        head_pos = self.snake.body[0]
        snake_direction = self.snake.get_direction()

        fruit_pos = self.fruit.pos

        diff = (head_pos - fruit_pos) // 1

        if diff.x == 0 and diff.y == 0:
            return None

        if abs(diff.x) > 0:

            if diff.x < 0:
                return GameCommand(CommandType.DIRECTION, Direction.EAST)
            elif diff.x > 0:
                return GameCommand(CommandType.DIRECTION, Direction.WEST)


        if abs(diff.y) > 0:

            if diff.y < 0:
                return GameCommand(CommandType.DIRECTION, Direction.SOUTH)
            elif diff.y > 0:
                return GameCommand(CommandType.DIRECTION, Direction.NORTH)

        return None


