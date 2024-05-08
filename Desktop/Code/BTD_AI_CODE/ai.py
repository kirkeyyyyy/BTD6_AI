import numpy as np
import ultralytics
import torch
import cv2
import time
from PIL import ImageGrab


def data_collector(num_ss):
    for i in range(num_ss):
        #takes screenshot every 1 second
        time.sleep(1)
        ss = ImageGrab.grab(bbox = (300, 300, 1100, 650))
        ss.save("data/data_3" + str(i) + ".png") 





if __name__ == '__main__':
    time.sleep(1)
    data_collector(2)
    
