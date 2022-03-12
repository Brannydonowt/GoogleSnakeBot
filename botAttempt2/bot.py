import cv2 as cv
import vision as vis
import framelabeler as labels
from VideoGet import VideoGet
from VideoShow import VideoShow
from CountsPerSec import CountsPerSec
from threading import Thread

def handle_video(source=0):
    video_getter = VideoGet(source).start()
    video_shower = VideoShow(video_getter.frame).start()
    cps = CountsPerSec().start()

    while True:
        if video_getter.stopped or video_shower.stopped:
            video_shower.stop()
            video_getter.stop()
            break

        frame = video_getter.frame
        video_shower.frame = frame
        cps.increment()

handle_video('botAttempt2/resources/demo.mp4')