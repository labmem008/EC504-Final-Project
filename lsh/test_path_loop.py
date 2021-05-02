import os
import sys
import cv2

path = r'../data/set1/'

def load_images_from_folder(folder):
    images = []
    for files in os.listdir(folder):
        image = cv2.imread(os.path.join(folder,files))
        if image is not None:
            images.append(image)
    return images

images = load_images_from_folder(path)
# print(len(images))
# cv2.imshow('Testing...', images[29])
# cv2.waitKey()
