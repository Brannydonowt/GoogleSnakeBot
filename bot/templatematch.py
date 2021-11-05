# script for template matching related functions

import sys
import cv2 as cv
import numpy as np
import mss

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