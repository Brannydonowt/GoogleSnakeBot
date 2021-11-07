import mss
import numpy as np
import cv2 as cv
from PIL import Image
import collections
import sys
# desired rgba = 170, 215, 81
# we want to look in every column of every row
# so row 1: check each colomn, etc...
# until we find the right rgba
# then we return the row and column, this is the top left corner of the game

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

def get_pixels(img):
    print("bolh")

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

def find_game_board():
    img = Screen_Shot()
    start = get_board_start(img)
    end = get_board_end(img)
    draw_rectangle(img, start, end, (0, 0, 255))
    return img

def main():
    running = True
    game = find_game_board()
    while running:
        cv.imshow('res', game)

        if cv.waitKey(1) & 0xFF == ord("q"):
		        cv.destroyAllWindows()
		        cv.waitKey(1)
		        flag = False
		        sys.exit


main()