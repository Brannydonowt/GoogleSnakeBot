# the snake is made of coordinates
# to move the snake, we add the co-ordinates from the next point on the grid by adding dir
# dir is the direction the snake is moving in
# we add this new co-ordinate to the front of the list
# we remove the final item in the list (the snakes tail)
# we can KEEP the final item, if the player grabbed an apple
import sys
import cv2
import numpy as np
import time
import random
import collections
import vision as vis
import input
import pathing

class SnakeMove:

    io = input.Input()

    # the grid is currently working in reverse... [y, x]
    snake = [[8, 2], [8, 3], [8, 4], [8, 5]]
    apple = [8, 13]
    snakesize = 4
    gridsizeX = 17
    gridsizeY = 15

    cur_path = []

    v = vis.vision()
    # 0, 1 = right
    # 0, -1 = left
    # 1, 0 = up
    # -1, 0 = down
    def move_snake(self, dir):
        headPos = self.snake[len(self.snake) - 1]
        print (headPos)
        print (dir)
        newHead = [headPos[0] + dir[0], headPos[1] + dir[1]]
        self.snake.append(newHead)
        #print(f"Snake head is: {self.snake[len(self.snake) - 1]}")
        #print(f"Apple is: {self.apple}")
        if not self.is_apple():
            self.snake.pop(0)
        else:
            return True

    def move_to_apple(self):
        dir = self.calc_path()
        return self.move_snake(dir), dir

    def has_dir(self):
        if len(self.cur_path) == 0:
            #print(self.cur_path)
            return True
        else:
            return False

    def is_apple(self):
        snakehead = self.snake[len(self.snake) - 1]
        compare = lambda x, y: collections.Counter(x) == collections.Counter(y)
        if compare(snakehead, self.apple):
            self.snakesize += 1
            #print(f"Snake Size: {self.snakesize}")
            #print("We got the apple!")
            return True
        else:
            #print("No apple here!")
            return False

    def move_apple(self, loc):
        self.apple = loc

    def display_game_state(self):
        grid = self.create_grid(self.gridsizeX, self.gridsizeY)
        for body in self.snake:
            grid[body[0] - 1][body[1] -1] = 1

        grid[self.apple[0] - 1][self.apple[1] - 1] = 2
        #print(np.matrix(grid))
        return grid

    def create_grid(self, gx, gy):
        return [[0 for x in range(0, gx)] for x in range(0, gy)]

    def calc_path(self):
        start = self.snake[len(self.snake) - 1]
        end = self.apple

        dirs = pathing.calc_safe_path(start, end, self.display_game_state())
        if type(dirs[0]) == int: 
            return dirs
        else:
            return dirs[len(dirs) - 1]

    def main(self):
        running = True
        self.display_game_state()
        while running:
            time.sleep(0.15)
            self.move_to_apple()
