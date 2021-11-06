# the snake is made of coordinates
# to move the snake, we add the co-ordinates from the next point on the grid by adding dir
# dir is the direction the snake is moving in
# we add this new co-ordinate to the front of the list
# we remove the final item in the list (the snakes tail)
# we can KEEP the final item, if the player grabbed an apple
import sys
import numpy as np
import random 

class SnakeMove:
    snake = [[5, 2], [5, 3], [5, 4], [5, 5], [5, 6]]
    apple = [8, 8, 4, 6]
    gridsize = 10
    # 0, 1 = right
    # 0, -1 = left
    # 1, 0 = up
    # -1, 0 = down
    def move_snake(self, dir):
        headPos = self.snake[len(self.snake) - 1]
        newHead = [headPos[0] + dir[0], headPos[1] + dir[1]]
        self.snake.append(newHead)
        if self.is_apple() == True:
            self.apple = self.new_apple()
        else:
            self.snake.pop(0)

        self.display_game_state()

    def is_apple(self):
        snakehead = self.snake[len(self.snake) - 1]
        if snakehead[0] == self.apple[0] & snakehead[1] == self.apple[1]:
            return True
        else:
            return False

    def new_apple(self):
        newapple = [random.randint(0, self.gridsize), random.randint(0, self.gridsize)]
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

    def main():
        running = True

s = SnakeMove()
s.move_snake([0, 1])
s.move_snake([0, 1])
s.move_snake([1, 0])
s.move_snake([1, 0])
s.move_snake([1, 0])
s.move_snake([1, 0])
