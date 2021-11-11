import numpy as np

def calc_path_direct(start, end):
    dirs = []
    dist = [start[0] - end[0], start[1] - end[1]]
    distY = dist[0]
    distX = dist[1]

    #print(f"Dist X = {distX}")
    #print(f"Dist Y = {distY}")
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

    if len(dirs) == 0:
        print ("ROAMING")
        return calc_path_direct(start, [1, 1])
    return dirs

def calc_safe_path(start, end, game):
    dirs = calc_path_direct(start, end)
    
    dirs = validate_dir(start, dirs[len(dirs) - 1], game)
    return dirs

def validate_dir(start, dir, game):
    res = start[0] + dir[0], start[1] + dir[1]
    if game[res[0]][res[1]] == 0:
        #print (f"normal pathing {dir}")
        return dir
    if game[res[0]][res[1]] == 1:
        #print("special pathing")
        return get_backwards_dir(dir)

def get_backwards_dir(dir):
    if not dir[0] == 0:
        # we are moving vertically
        mDir = [0, 1]
        rDir = [dir[0] * -1, dir[1] * -1]
        return [mDir, rDir]
    else:
        # we are moving horizontally
                # we are moving vertically
        mDir = [1, 0]
        rDir = [dir[0] * -1, dir[1] * -1]
        return [mDir, rDir]


def get_roam():
    return get_backwards_dir([0, 1])
