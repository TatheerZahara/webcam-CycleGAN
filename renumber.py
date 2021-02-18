import os
from natsort import natsorted
path = r"/home/ben/gans_git/pytorch-CycleGAN-and-pix2pix/results/style_vangogh_pretrained/test_latest/images"
directory  = os.listdir(path)
directory = natsorted(directory)
print(directory)
for count, filename in enumerate(directory):
    src = path + "/" + filename
    dst = path + "/" + str(count) + ".png"
    os.rename(src, dst) 