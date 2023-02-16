
from typing import List, Optional

import pygame
from controllers.controller import Controller
from config import max_x_units, max_y_units

from direction import Direction
from game_command import CommandType, GameCommand

from gameobjects import Snake, Fruit
from util import Vec2

from dataclasses import dataclass, field

import heapq

def guess_score(x: Vec2, y: Vec2):
    return x.distanceL2(y)

@dataclass(order=True)
class PrioritizedVec2:
    f: float
    g: float
    h: float
    item: Vec2=field(compare=False)


def get_p_vec2(x:Vec2, y: Vec2, g: float):
    h = guess_score(x, y)
    return PrioritizedVec2(h, g, h, x)

ABLE_MOVES = [(-1, 0), (1, 0), (0, 1), (0, -1)]

# AI with A* Search
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

    def search(self):

        node_queue: List[PrioritizedVec2] = []

        parent = {}

        visited_nodes = {}

        heapq.heappush(node_queue, get_p_vec2(self.snake.body[0], self.fruit.get_position(), 0))

        i = 0

        while len(node_queue) > 0:

            current_node = heapq.heappop(node_queue)

            visited_nodes[current_node.item] = current_node.f

            if current_node.item.distanceL1(self.fruit.get_position()) < 1.0:
                parent[self.fruit.get_position()] = parent[current_node.item]
                break

            for move in ABLE_MOVES:
                move_vec = Vec2(*move)

                if i == 0:
                    if move_vec.dot_product(self.snake.direction.get_opposite().get_vector()) > 0:
                        continue

                check_pos = current_node.item + move_vec
                for p in self.snake.body:
                    if check_pos.distanceL1(p) < 1.0:
                        continue
                
                # valid moves
                p_node = get_p_vec2(check_pos, self.fruit.get_position(), current_node.g + 1.0)
                
                if p_node.item in visited_nodes:
                    if visited_nodes[p_node.item] < p_node.f:
                        continue

                heapq.heappush(node_queue, p_node)
                parent[p_node.item] = current_node.item
                
                # if p_node.item in closed:

            i += 1


                # heapq.heappush(node_queue, )

        x = self.fruit.get_position()
        path = [x]
        while path[-1] != self.snake.body[0]:
            path.append(parent[x])
            x = path[-1]

        if len(path) > 1:
            dir_vec = path[-1] - path[-2]
            
            return dir_vec
        
        return Vec2(0, 0)


    ## called on every event
    def handle_event(self, _event: pygame.event.Event) -> Optional[GameCommand]:
        
        return None

    ## called on every frame
    def handle_update(self) -> Optional[GameCommand]:

        diff = self.search()

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


