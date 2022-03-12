import cv2 as cv
import mss
import numpy as np
import collections


class vision:
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
        Image = cv.rectangle(img, top_left, bottom_right, col, 2)
        return Image

    def get_board_start(self, img):
        compare = lambda x, y: collections.Counter(x) == collections.Counter(y)
        col = [75, 218, 163, 255]
        img = np.array(img)
        img = cv.cvtColor(img, 0)
        for h in range(0, len(img)):
            for w in range(0, 934):
                if (compare(img[h, w], col)):
                    print("Top Left [x,y] -", [w,h])
                    return [w, h]
                else:
                    print("could not color match: ", img[h, w], "to", col)

    def get_board_end(self, img):
        compare = lambda x, y: collections.Counter(x) == collections.Counter(y)
        col = [75, 218, 163, 255]
        img = np.array(img)
        img = cv.cvtColor(img, 0)
        for h in reversed(range(0, len(img))):
            for w in reversed(range(0, 934)):
                if compare(img[h, w], col):
                    print("Bottom Right [x, y] -", [w,h])
                    return [w,h]
                else:
                    print("could not color match: ", img[h, w], "to", col)

    def get_board_boundary(self, img):
        start = self.get_board_start(img)
        end = self.get_board_end(img)
        bounds = [start[0], end[0], end[1], start[1]]
        return bounds

    def get_boundary_x(self, img):
        bounds = self.get_board_boundary(img)
        return [bounds[0], bounds[1]]

    def get_boundary_y(self, img):
        bounds = self.get_board_boundary(img)
        return [bounds[2], bounds[3]]

    def show_img(self, img):
        cv.imshow("vision", img)
        cv.waitKey(0)
