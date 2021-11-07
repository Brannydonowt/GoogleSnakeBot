# test program for image tracking using oop approach
# currently tracks apples and snake head
# updates every frame when running
# can be canceled by pressing q
import sys
import cv2 as cv
import numpy as np
import mss

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

def main():
    running = True
    while running:
        img = Screen_Shot()
        tlA, brA = get_target_rect(img, 'img/apple.jpg')
        draw_rectangle(img, tlA, brA, (0, 0, 255))
        tlS, brS = get_target_rect(img, 'img/snake_head.jpg')
        draw_rectangle(img, tlS, brS, (0, 255, 0))
        cv.imshow('res', img)

        if cv.waitKey(1) & 0xFF == ord("q"):
		        cv.destroyAllWindows()
		        cv.waitKey(1)
		        flag = False
		        sys.exit()

def get_target_rect(img, templatepath):
    img2 = img.copy()
    template = cv.imread(templatepath, 1)
    #template = cv.cvtColor(template, cv.COLOR_BGR2GRAY)
    w, h = template.shape[:-1]

    method=cv.TM_CCOEFF_NORMED
    gray = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)
    res = cv.matchTemplate(img2, template, method)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
    # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
    if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)

    return top_left, bottom_right

def draw_rectangle(img, top_left, bottom_right, col):
    cv.rectangle(img, top_left, bottom_right, col, 2)
   

main()