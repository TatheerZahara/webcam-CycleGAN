import os
from natsort import natsorted
path = r"D:\Kaspar\images\monet\rocky_vangogh"
directory  = os.listdir(path)
directory = natsorted(directory)
print(directory)
for count, filename in enumerate(directory):
    src = path + "/" + filename
    dst = path + "/" + str(count) + ".jpg"
    os.rename(src, dst) 