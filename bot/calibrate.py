import mss
import numpy as np
import cv2 as cv
import vision as v
import time
import input as i

def Screen_Shot(left=0, top=0, width=600, height=668):
    stc = mss.mss()
    scr = stc.grab({
        'left': left,
        'top': top,
        'width': width,
        'height': height
    })

    img = np.array(scr)
    img = cv.cvtColor(img, 0)

    return img

def get_move_speed(game_cells):
    print("Getting move speed")

    game = Screen_Shot()

    vis = v.vision()
    input = i.Input()
    start = [5, 8]

    input.move_right()
    time.sleep(1)

    game2 = Screen_Shot()
    head2 = vis.get_target_rect(game2, 'img/snake_head.jpg')
    cell2 = vis.get_cell_of(head2[0], head2[1], game_cells, 10)
    print(cell2)
    print(cell2[2])
    distTravelledX = cell2[2] - start[0]
    disTravelledY = cell2[3] - start[1]
    print(f"Distance X: {distTravelledX} , Distance Y: {disTravelledY}")

    movespeed = 1 / distTravelledX
    print (f"Movespeed: {movespeed}")


