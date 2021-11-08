# the snake is made of coordinates
# to move the snake, we add the co-ordinates from the next point on the grid by adding dir
# dir is the direction the snake is moving in
# we add this new co-ordinate to the front of the list
# we remove the final item in the list (the snakes tail)
# we can KEEP the final item, if the player grabbed an apple
import sys
import numpy as np
import time
import random
import collections

class SnakeMove:
    snake = [[5, 2], [5, 3], [5, 4], [5, 5], [5, 6]]
    apple = [8, 8]
    snakesize = 5
    gridsize = 20
    # 0, 1 = right
    # 0, -1 = left
    # 1, 0 = up
    # -1, 0 = down
    def move_snake(self, dir):
        headPos = self.snake[len(self.snake) - 1]
        newHead = [headPos[0] + dir[0], headPos[1] + dir[1]]
        self.snake.append(newHead)
        print(f"Snake head is: {self.snake[len(self.snake) - 1]}")
        print(f"Apple is: {self.apple}")
        if self.is_apple() == True:
            self.apple = self.new_apple()
        else:
            self.snake.pop(0)

        self.display_game_state()

    def move_to_apple(self):
        start = self.snake[len(self.snake) - 1]
        print (f"Snake Head = {start}")
        end = self.apple
        dir = self.calc_path(start, end)
        self.move_snake(dir)

    def is_apple(self):
        snakehead = self.snake[len(self.snake) - 1]
        compare = lambda x, y: collections.Counter(x) == collections.Counter(y)
        if compare(snakehead, self.apple):
            self.snakesize += 1
            print(f"Snake Size: {self.snakesize}")
            print("We got the apple!")
            return True
        else:
            print("No apple here!")
            return False

    def new_apple(self):
        newapple = [random.randint(0, self.gridsize - 1), random.randint(0, self.gridsize - 1)]
        if self.snake.count(newapple) > 0:
            self.new_apple()
        else:
            return newapple

    def display_game_state(self):
        grid = self.create_grid(self.gridsize)
        for body in self.snake:
            grid[body[0]][body[1]] = 1

        grid[self.apple[0]][self.apple[1]] = 2
        print(np.matrix(grid))

    def create_grid(self, gridsize):
        return [[0 for x in range(0, gridsize)] for x in range(0, gridsize)]

    def calc_path(self, start, end):
        dist = [start[0] - end[0], start[1] - end[1]]
        distY = dist[0]
        distX = dist[1]
        print(f"Dist X = {distX}")
        print(f"Dist Y = {distY}")
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
        print (dirs)
        return dirs[len(dirs) - 1]

    def main(self):
        running = True
        self.display_game_state()
        while running:
            time.sleep(0.1)
            self.move_to_apple()


s = SnakeMove()
s.main()
