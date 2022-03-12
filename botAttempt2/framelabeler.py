import cv2 as cv
from threading import Thread

# multithreaded frame labelling
# some caveats/problems that might arise
# 1 - accessing information from other classes might become troublesome
#       - Perhaps having a game parser that gets all relevant info and is then passed into this, would work.
#       -   The main thread would then have to look something like this:
#           - StreamVideo
#           - ParseVideo
#           - Do calculations
#           - Do actions <- Actions should be done before results are rendered to the screen? As labelling the screen might take a lot of time
#           - Label frame
#           - Show fram
def labelFrame(frame):
        frame = putIterationsPerSec(frame, 100)

        return frame

def draw_rectangle(img, top_left, bottom_right, col):
    frame = cv.rectangle(img, top_left, bottom_right, col, 2)
    return frame

def putIterationsPerSec(frame, iterations_per_sec):
    """
    Add iterations per second text to lower-left corner of a frame.
    """
    cv.putText(frame, "{:.0f} iterations/sec".format(iterations_per_sec),
        (10, 450), cv.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255))
    return frame

def draw_game_boundary(img):
    global game_boundary_x
    global game_boundary_y
    start = [game_boundary_x[0], game_boundary_y[0]]
    end = [game_boundary_x[1], game_boundary_y[1]]
    return draw_rectangle(img, start, end, (0, 0, 255))