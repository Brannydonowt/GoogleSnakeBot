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

class SnakeMove:

    io = input.Input()

    # the grid is currently working in reverse... [y, x]
    snake = [[8, 2], [8, 3], [8, 4], [8, 5]]
    apple = [8, 13]
    snakesize = 4
    gridsizeX = 17
    gridsizeY = 15

    v = vis.vision()
    # 0, 1 = right
    # 0, -1 = left
    # 1, 0 = up
    # -1, 0 = down
    def move_snake(self, dir):
        headPos = self.snake[len(self.snake) - 1]
        newHead = [headPos[0] + dir[0], headPos[1] + dir[1]]
        self.snake.append(newHead)
        if not self.is_apple():
            self.snake.pop(0)
            return False
        else:
            return True
    
    # 0, 1 = right
    # 0, -1 = left
    # 1, 0 = up
    # -1, 0 = down
    def do_input(self, dir):
        if dir == [0, 1]:
            self.io.move_right()
        if dir == [0, -1]:
            self.io.move_left()
        if dir == [1, 0]:
            self.io.move_up()
        if dir == [-1, 0]:
            self.io.move_down

    def move_to_apple(self):
        start = self.snake[len(self.snake) - 1]
        end = self.apple
        dir = self.calc_path(start, end)
        return self.move_snake(dir), dir

    def is_apple(self):
        snakehead = self.snake[len(self.snake) - 1]
        compare = lambda x, y: collections.Counter(x) == collections.Counter(y)
        if compare(snakehead, self.apple):
            self.snakesize += 1
#            print(f"Snake Size: {self.snakesize}")
#            print("We got the apple!")
            return True
        else:
#            print("No apple here!")
            return False

    def move_apple(self, loc):
        self.apple = loc

    def display_game_state(self):
        grid = self.create_grid(self.gridsizeX, self.gridsizeY)
        for body in self.snake:
            grid[body[0] - 1][body[1] -1] = 1

        grid[self.apple[0] - 1][self.apple[1] - 1] = 2
        print(np.matrix(grid))

    def create_grid(self, gx, gy):
        return [[0 for x in range(0, gx)] for x in range(0, gy)]

    def calc_path(self, start, end):
        dist = [start[0] - end[0], start[1] - end[1]]
        distY = dist[0]
        distX = dist[1]
#        print(f"Dist X = {distX}")
#        print(f"Dist Y = {distY}")
        dirX = []
        for i in range(abs(distX)):
            if distX < 0:
                dirX.append([0, 1])
            if distX > 0:
                dirX.append([0, -1])
        dirY = []
        for i in range(abs(distY)):
            if distY < 0:
                dirY.append([1, 0])
            if distY > 0:
                dirY.append([-1, 0])
        dirs = dirX + dirY
        #print (dirs)
        return dirs[len(dirs) - 1]

    def main(self):
        running = True
        self.display_game_state()
        self.move_to_apple()