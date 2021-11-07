# auto path to apple

# say we have two positions
# [8, 3] = apple 
# [2, 5] = snake head

# apple - snake head =
# [6, -2]

# deduce the difference in x & y into a list of move directions, e.g
# [[1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [0, 1], [0, 1]]
# x = 6
# y = -2

# figure out the direction we are going in (for x and y)
# start = snake head
# end = apple
def calc_path(start, end):
    dist = [start[0] - end[0], start[1] - end[1]]
    distX = dist[0]
    distY = dist[1]
    dirX = []
    for i in range(abs(distX - 1)):
        if i > 0:
            dirX.append([0, 1])
        if i < 0:
            dirX.append([0, -1])
    
    dirY = []
    for i in range(abs(distY - 1)):
        if i > 0:
            dirY.append([-1, 0])
        if i < 0:
            dirY.append([1, 0])
    
    dirs = dirX + dirY

    print(dirs)

calc_path([2, 2], [8, 1])

# apply these movements 1 by 1
# for dir in dirs:
#   move_snake(dir)