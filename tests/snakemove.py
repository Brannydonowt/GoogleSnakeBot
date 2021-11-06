# the snake is made of coordinates
# to move the snake, we add the co-ordinates from the next point on the grid by adding dir
# dir is the direction the snake is moving in
# we add this new co-ordinate to the front of the list
# we remove the final item in the list (the snakes tail)
# we can KEEP the final item, if the player grabbed an apple 
import numpy as np

snake = [[5, 2], [5, 3], [5, 4], [5, 5], [5, 6]]
apple = [8, 8]
# 0, 1 = right
# 0, -1 = left
# 1, 0 = up
# -1, 0 = down
def move_snake(dir):
    headPos = snake[len(snake) - 1]
    newHead = [headPos[0] + dir[0], headPos[1] + dir[1]]
    snake.insert(len(snake), newHead)
    snake.pop(0)
    display_snake_on_grid(10)

def display_snake_on_grid(gridsize):
    grid = create_grid(gridsize)
    for body in snake:
        grid[body[0]][body[1]] = 1
    print(np.matrix(grid))

def create_grid(gridsize):
    return [[0 for x in range(0, gridsize)] for x in range(0, gridsize)]

move_snake([0, 1])
move_snake([0, 1])
move_snake([-1, 0])
move_snake([-1, 0])
move_snake([0, -1])