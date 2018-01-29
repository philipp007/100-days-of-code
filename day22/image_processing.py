from scipy.misc import imresize
import numpy as np


def get_gray_scale(screen_buffer, width=None, height=None):
    gray_scale = screen_buffer.astype(np.float32).mean(axis=0)

    if width is not None and height is not None:
        return imresize(gray_scale, (width, height))
    return gray_scale


def scale(screen_buffer, width=80, height=80):
    return imresize(screen_buffer, (width, height))