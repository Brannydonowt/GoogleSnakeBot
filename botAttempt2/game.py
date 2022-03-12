from turtle import update
import cv2 as cv
import mss
import numpy as np
import collections
import vision


# Class responsible for all parsed game data
class game:

    def __init__(self, frame) -> None:
        self.frame = frame

    def start(self):
        self.boundsX = [0, 0]
        self.boundsY = [0, 0]
        return self.update_game(self.frame)

    def get_game(self):
        return self

    def update_game(self, frame):
        self.v = vision.vision()
        self.frame = frame
        self.boundsX = self.v.get_boundary_x(frame)
        self.boundsY = self.v.get_boundary_y(frame)
        return self


    