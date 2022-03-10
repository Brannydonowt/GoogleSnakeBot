import cv2
import vision as vis
import input
import calibrate as cal
import snake
import time
import webbrowser
import pathing as path

s = snake.SnakeMove()
v = vis.vision()
i = input.Input()

#moveDelay = 0.14285714285714285
moveDelay = 0.135

def calibrate():
    i.focus_game()
    v.setup()

    time.sleep(2)

    cal.get_move_speed(v.game_cells)

def setup_game():
    # webbrowser.open('https://www.google.com/fbx?fbx=snake_arcade')
    time.sleep(5)
    i.focus_game()
    s.display_game_state()

def main():
    playing = True
    path.set_last_dir([0, 1])
    s.snakehead = s.snake[len(s.snake) - 1]
    while (playing):
        dir = path.get_next_Dir(s.snakehead)
        i.move_dir(dir)
        s.move_snake(dir)
        s.display_game_state()
        time.sleep(moveDelay)

setup_game()
main()

# if we get an apple
# we should enter "sync head" mode
# this tracks the snake head so we don't get lost
# until we have an apple again...
# then we make our new path based on the last snake head pos and the new apple

# Add a way to wait until apple found is true or something...

# problem is, a snake head can be between two grid cells...