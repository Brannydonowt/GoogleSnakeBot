


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
    return dirs