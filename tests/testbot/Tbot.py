import vision as vis
import input
import snake
import time

s = snake.SnakeMove()
v = vis.vision()
i = input.Input()

moveDelay = 0.13

def setup_game():
    i.focus_game()
    v.setup()
    v.get_game()
    s.display_game_state()

def main():
    playing = True
    while (playing):
        apple, dir = s.move_to_apple()
        i.move_dir(dir)
        if (apple):
            v.get_game()
            na = v.get_apple_loc()
            s.move_apple(na)
            s.display_game_state()

        time.sleep(moveDelay)

setup_game()
main()
