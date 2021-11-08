import cv2
import vision as vis
import input
import snake
import time

s = snake.SnakeMove()
v = vis.vision()
i = input.Input()

moveDelay = 0.135

def setup_game():
    i.focus_game()
    v.setup()
    s.display_game_state()

def main():
    playing = True
    while (playing):
        apple, dir = s.move_to_apple()
        print(dir)
        i.move_dir(dir)
        if (apple):
            # THE GAME GETS OUT OF SYNC BECAUSE WE SLEEP 
            # TO ALLOW TIME TO FIND THE NEW APPLE IMG!!!
            # SOLVE THAT ONE, SMART ASS
            time.sleep(0.3)
            v.get_game()
            na = v.get_apple_loc()
            s.move_apple(na)
            s.display_game_state()

        time.sleep(moveDelay)

setup_game()
main()

# if we get an apple
# we should enter "sync head" mode
# this tracks the snake head so we don't get lost
# until we have an apple again...
# then we make our new path based on the last snake head pos and the new apple

# problem is, a snake head can be between two grid cells...