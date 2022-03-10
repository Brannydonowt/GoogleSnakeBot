import vision as vis

v = vis.vision()

game_boundary_x = [0, 0]
game_boundary_y = [0, 0]

def main():
   running = True
   img = v.Screen_Shot()
   game = get_game(img)
   v.show_img(game)

def get_game(img):
    global game_boundary_x
    global game_boundary_y
    bounds = v.get_board_boundary(img)
    game_boundary_x = [bounds[0], bounds[1]]
    game_boundary_y = [bounds[3], bounds[2]]
    print("[Min, Max] X", game_boundary_x)
    print("[Min, Max] Y", game_boundary_y)
    return draw_game_boundary(img)

def draw_game_boundary(img):
    global game_boundary_x
    global game_boundary_y
    start = [game_boundary_x[0], game_boundary_y[0]]
    end = [game_boundary_x[1], game_boundary_y[1]]
    return v.draw_rectangle(img, start, end, (0, 0, 255))
   # return v.draw_rectangle(img, v.get_board_start(img), v.get_board_end(img), (0, 0, 255))

main()