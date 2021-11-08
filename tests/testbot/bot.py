import findapplecell as vis
import snake

s = snake.SnakeMove()
v = vis.vision()

def setup_game():
    v.setup()
    s.main()

setup_game()