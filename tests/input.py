from pynput.mouse import Button, Controller
from pynput.mouse import Listener
import cv2 as cv
import numpy as np
import mss
import time

mouse = Controller()

waitingInput = False
gameTL = [0, 0]
gameBR = [0, 0]
lastClick = [0, 0]

def Screen_Shot(left=0, top=0, width=600, height=668):
	stc = mss.mss()
	scr = stc.grab({
		'left': left,
		'top': top,
		'width': width,
		'height': height
	})

	img = np.array(scr)
	img = cv.cvtColor(img, 1)

	return img


def on_click(x, y, button, pressed):
    global waitingInput
    waitingInput = False
    print("input.")
    if not waitingInput:
        return False

    if not pressed:
        return False
    
    return [x, y]

# ask the user to point in the top left and bottom right corners of the game
def get_user_screen_point(msg):
    global waitingInput
    print(msg)
    waitingInput = True
    while (waitingInput):
        time.sleep(0.5)
        print("...")

def draw_rectangle(img, top_left, bottom_right, col):
    cv.rectangle(img, top_left, bottom_right, col, 2)

def main():
    global gameTL, gameBR
    gameTL = get_user_screen_point("Please press in the top left corner of the game grid.")
    gameBR = get_user_screen_point("Please press in the bottom right corner of the game grid.")
    width = gameBR[0] - gameTL[0]
    height = gameBR[1] - gameTL[1]
    print(f"Width: {width}, Height: {height}")
    img = Screen_Shot(gameTL[0], gameTL[1], width, height)
    draw_rectangle(img, gameTL, gameBR)
    cv.imshow("game", img)

main()
    

