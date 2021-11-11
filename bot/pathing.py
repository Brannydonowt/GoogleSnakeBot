import numpy as np

    # 0, 1 = right
    # 0, -1 = left
    # 1, 0 = up
    # -1, 0 = down
lastdir = []

def set_last_dir(dir):
    global lastdir
    lastdir = dir

def get_last_dir():
    global lastdir
    return lastdir

def get_next_Dir(pos):
    global lastdir
    if pos[1] == 15:
        if pos[0] < 14:
            # we have space if we are bottom right
            print ("moving down")
            lastdir = [1, 0]
            return lastdir
        else:
            print ("moving left")
            lastdir = [0, -1]
            return lastdir

    if pos[1] == 2:
        if pos[0] > 1:
            print ("moving up")
            lastdir = [-1, 0]
            return lastdir
        else:
            lastdir = [0, 1]
            return lastdir

    return lastdir

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
