import cv2
import numpy as np
import os
from natsort import natsorted
#path = r"D:\Kaspar\images\monet\rocky"
path = r"/home/ben/gans_git/pytorch-CycleGAN-and-pix2pix/results/style_vangogh_pretrained/test_latest/images"
directory  = os.listdir(path)
directory = natsorted(directory)
img_array = []
print(directory)
for filename in directory:
    print(path + '/' + filename)
    img = cv2.imread(path + '/' + filename)
    height, width, layers = img.shape
    size = (width,height)
    img_array.append(img)


out = cv2.VideoWriter('project.avi',cv2.VideoWriter_fourcc(*'DIVX'), 30, size)
 
for i in range(len(img_array)):
    out.write(img_array[i])
out.release()