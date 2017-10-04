#!/usr/bin/env python

from freenect import sync_get_video as get_video, sync_get_depth as get_depth
import freenect
import os
import sys
import numpy as np
import signal
import frame_convert2
from time import time
import cv2

## write code to get take the kinect images and then convert frames to tf records
## tf records then get fed into the tf-models object recognition pipeline

cv2.namedWindow('Depth')
cv2.namedWindow('RGB')
KEEP_RUNNING = True

def get_depth():
    return frame_convert2.pretty_depth_cv(freenect.sync_get_depth()[0])


def get_video():
    return frame_convert2.video_cv(freenect.sync_get_video()[0])

def run():
    while KEEP_RUNNING:
        # cv2.imshow('Depth', get_depth())
        cv2.imshow('Video', get_video())
        if cv2.waitKey(10) == 27:
            break

    # print('Press ESC in window to stop')
    # freenect.runloop(depth=display_depth,
    #                  video=display_rgb,
    #                  body=body)
    return

if __name__ == '__main__':
    run()
