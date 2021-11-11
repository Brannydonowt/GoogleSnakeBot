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
class vision:
    game_cells = []
    apple_cell = []
    apple_loc = []

    def Screen_Shot(self, left=0, top=0, width=600, height=668):
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

    def draw_rectangle(self, img, top_left, bottom_right, col):
        cv.rectangle(img, top_left, bottom_right, col, 2)

    def get_board_start(self, img):
        compare = lambda x, y: collections.Counter(x) == collections.Counter(y)
        col = [170, 215, 81, 255]
        for h in range(0, len(img)):
            for w in range(0, 600):
                if (compare(img[h, w], col)):
                    return [w,h]

    def get_board_end(self, img):
        compare = lambda x, y: collections.Counter(x) == collections.Counter(y)
        col = [170, 215, 81, 255]
        for h in reversed(range(0, len(img))):
            for w in reversed(range(0, 600)):
                if compare(img[h, w], col):
                    return [w,h]

    def divide_game_board(self, start, end, divisions = 17):
        width = end[0] - start[0]
        height = end[1] - start[1]
        cells = self.create_cell_list(start, width, height, 17, 15)
        #print(f"Width: {width}, Height: {height}")
        return cells

    # start, width, height, divisionsx, divisionsy
    def create_cell_list(self, s, w, h, dx, dy):
        cells = []
        cellw = w / dx
        cellh = h / dy
        for divX in range(0, dx):
            for divY in range(0, dy):
                tlx = s[0] + (cellw * divX)
                tly = s[1] + (cellh * divY)
                brx = tlx + cellw
                bry = tly + cellh
                cell = [[int(tlx), int(tly)], [int(brx), int(bry)], divX + 1, divY + 1]
                cells.append(cell)
        
        return cells

    def get_target_rect(self, img, templatepath):
        img2 = img.copy()
        template = cv.imread(templatepath, 1)
        template = cv.cvtColor(template, cv.COLOR_BGR2GRAY)
        w, h = template.shape[::-1]

        method=cv.TM_CCOEFF_NORMED
        gray = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)
        res = cv.matchTemplate(gray, template, method)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
        # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
        if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
            top_left = min_loc
        else:
            top_left = max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)

        return top_left, bottom_right

    def get_apple_cell(self, start, end, cells, t = 10):
        
        ac = self.get_center_point(start, end)
        for cell in cells:
            tl = [int(cell[0][0]), int(cell[0][1])]
            br = [int(cell[1][0]), int(cell[1][1])]
            cc = self.get_center_point(tl, br)

            xDif = cc[0] - ac[0]
            yDif = cc[1] - ac[1]

            if (xDif < t and xDif > (0 - t)):
                if (yDif < t and yDif > (0 - t)):
                    self.apple_cell = cell
                    print(f"Detected Apple Cell: {self.apple_cell}")
                    return cell

    def get_cell_of(self, start, end, cells, t = 10):
        ac = self.get_center_point(start, end)
        for cell in cells:
            tl = [int(cell[0][0]), int(cell[0][1])]
            br = [int(cell[1][0]), int(cell[1][1])]
            cc = self.get_center_point(tl, br)

            xDif = cc[0] - ac[0]
            yDif = cc[1] - ac[1]

            if (xDif < t and xDif > (0 - t)):
                if (yDif < t and yDif > (0 - t)):
                    return cell

    def get_apple_loc(self):
        self.apple_loc = [self.apple_cell[3], self.apple_cell[2]]
        print(f"Apple Loc: {self.apple_loc}")
        #print (self.game_cells.index(self.apple_cell))
        return self.apple_loc

    def get_center_point(self, start, end):
        cx = (start[0] + end[0]) / 2
        cy = (start[1] + end[1]) / 2
        return [int(cx), int(cy)]

    def setup(self):
        game = self.Screen_Shot()
        start = self.get_board_start(game)
        end = self.get_board_end(game)
        self.draw_rectangle(game, start, end, (0, 0, 255))
        self.game_cells = self.divide_game_board(start, end, 17)
        for cell in self.game_cells:
            tl = [int(cell[0][0]), int(cell[0][1])]
            br = [int(cell[1][0]), int(cell[1][1])]
            self.draw_rectangle(game, tl, br, (0, 255, 0))
        
        apple = self.get_target_rect(game, 'img/apple.jpg')
        self.draw_rectangle(game, apple[0], apple[1], (255, 0, 0))

        ac = self.get_apple_cell(apple[0], apple[1], self.game_cells, 10)
        self.draw_rectangle(game, [int(ac[0][0]), int(ac[0][1])],  [int(ac[1][0]), int(ac[1][1])], (0, 0, 255))

    def get_game(self):
        game = self.Screen_Shot()

        apple = self.get_target_rect(game, 'img/apple.jpg')
        self.draw_rectangle(game, apple[0], apple[1], (255, 0, 0))

        ac = self.get_apple_cell(apple[0], apple[1], self.game_cells, 5)
        self.draw_rectangle(game, [int(ac[0][0]), int(ac[0][1])],  [int(ac[1][0]), int(ac[1][1])], (0, 0, 255))

        return game

    def main(self):
        game = self.Screen_Shot()
        start = self.get_board_start(game)
        end = self.get_board_end(game)
        self.draw_rectangle(game, start, end, (0, 0, 255))
        for cell in self.game_cells:
            tl = [int(cell[0][0]), int(cell[0][1])]
            br = [int(cell[1][0]), int(cell[1][1])]
            self.draw_rectangle(game, tl, br, (0, 255, 0))
        
        apple = self.get_target_rect(game, 'img/apple.jpg')
        self.draw_rectangle(game, apple[0], apple[1], (255, 0, 0))

        ac = self.get_apple_cell(apple[0], apple[1], self.game_cells, 10)
        self.draw_rectangle(game, [int(ac[0][0]), int(ac[0][1])],  [int(ac[1][0]), int(ac[1][1])], (0, 0, 255))

        running = True
        while running:
            cv.imshow('res', game)

            if cv.waitKey(1) & 0xFF == ord("q"):
                    cv.destroyAllWindows()
                    cv.waitKey(1)
                    flag = False
                    sys.exit