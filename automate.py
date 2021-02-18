import os 
from natsort import natsorted
import cv2
models = ['style_cezanne_pretrained', 'style_monet_pretrained',  'style_ukiyoe_pretrained',  'style_vangogh_pretrained']
#run on rocky mountain dataset
for model in models:
    os.system('python test.py --dataroot ./datasets/rocky --name ' +  model + ' --model test --dataset_mode single --preprocess none --no_dropout --num_test 5')
    path = r'/home/ben/gans_git/pytorch-CycleGAN-and-pix2pix/results/' + model + '/test_latest/images'
    directory  = os.listdir(path)
    directory = natsorted(directory)
    img_array = []
    for filename in directory:
        print(path + '/' + filename)
        img = cv2.imread(path + '/' + filename)
        height, width, layers = img.shape
        size = (width,height)
        img_array.append(img)

    print("Writing video...")
    out = cv2.VideoWriter(model + '.avi',cv2.VideoWriter_fourcc(*'DIVX'), 30, size)
    
    for i in range(len(img_array)):
        out.write(img_array[i])
    out.release()
    print("Written!")