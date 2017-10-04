#!/usr/bin/env python

import kinect_lib.freenect as freenect
import kinect_lib.frame_convert as frame_convert
from freenect import sync_get_video as get_video
import os
import sys
import numpy as np
import signal
import cv2
from time import time

## write code to get take the kinect images and then convert frames to tf records
## tf records then get fed into the tf-models object recognition pipeline

KEEP_RUNNING = True


def run():
    start = time()
    while KEEP_RUNNING:
        rgb, _ = get_video()
        d3 = np.dstack((r,g,depth/20)).astype(np.uint8)
        da = np.hstack((d3,rgb[::2, ::2]))
        ## downsample image and then
        cv2.imshow('image', da)
        cv2.waitKey(0)
    return

if __name__ == '__main__':
    run()
