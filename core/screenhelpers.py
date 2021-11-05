import mss
import cv2
import numpy as np

def Screen_Shot(left=0, top=0, width=1920, height=1080):
	stc = mss.mss()
	scr = stc.grab({
		'left': left,
		'top': top,
		'width': width,
		'height': height
	})

	img = np.array(scr)
	img = cv2.cvtColor(img, cv2.IMREAD_COLOR)

	return img