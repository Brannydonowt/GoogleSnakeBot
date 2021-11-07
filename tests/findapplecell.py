import mss
import numpy as np
import cv2 as cv
from PIL import Image
import collections
import time
import sys
# desired rgba = 170, 215, 81
# we want to look in every column of every row
# so row 1: check each colomn, etc...
# until we find the right rgba
# then we return the row and column, this is the top left corner of the game
# game board is 17x15 by default

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

def draw_rectangle(img, top_left, bottom_right, col):
    cv.rectangle(img, top_left, bottom_right, col, 2)

def get_board_start(img):
    compare = lambda x, y: collections.Counter(x) == collections.Counter(y)
    col = [170, 215, 81, 255]
    for h in range(0, len(img)):
        for w in range(0, 600):
            if (compare(img[h, w], col)):
                return [w,h]

def get_board_end(img):
    compare = lambda x, y: collections.Counter(x) == collections.Counter(y)
    col = [170, 215, 81, 255]
    for h in reversed(range(0, len(img))):
        for w in reversed(range(0, 600)):
            if (compare(img[h, w], col)):
                return [w,h]

def divide_game_board(start, end, divisions = 17):
    width = end[0] - start[0]
    height = end[1] - start[1]
    cells = create_cell_list(start, width, height, 17, 15)
    print(f"Width: {width}, Height: {height}")
    return cells

# start, width, height, divisionsx, divisionsy
def create_cell_list(s, w, h, dx, dy):
    cells = []
    cellw = w / dx
    cellh = h / dy
    for divX in range(0, dx):
        for divY in range(0, dy):
            tlx = s[0] + (cellw * divX)
            tly = s[1] + (cellh * divY)
            brx = tlx + cellw
            bry = tly + cellh
            cell = [[tlx, tly], [brx, bry]]
            cells.append(cell)
    
    return cells

def main():
    game = Screen_Shot()
    start = get_board_start(game)
    end = get_board_end(game)
    draw_rectangle(game, start, end, (0, 0, 255))
    game_cells = divide_game_board(start, end, 17)
    for cell in game_cells:
        tl = [int(cell[0][0]), int(cell[0][1])]
        br = [int(cell[1][0]), int(cell[1][1])]
        draw_rectangle(game, tl, br, (0, 255, 0))
    running = True
    while running:
        cv.imshow('res', game)

        if cv.waitKey(1) & 0xFF == ord("q"):
		        cv.destroyAllWindows()
		        cv.waitKey(1)
		        flag = False
		        sys.exit


main()