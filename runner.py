#!/usr/bin/env python

import kinect_lib.freenect as freenect
import kinect_lib.frame_convert as frame_convert
from freenect import sync_get_video as get_video
import os
import sys
import numpy as np
import signal
# import cv

## write code to get take the kinect images and then convert frames to tf records
## tf records then get fed into the tf-models object recognition pipeline

KEEP_RUNNING = True

def run():
    while KEEP_RUNNING:
        pass

    return

if __name__ == '__main__':
    run()
