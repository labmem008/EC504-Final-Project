import numpy
import cv2
import sys
sys.path.append('../../EC504-Final-Project/helper/')
import image2vector

path1 = r'../data/set1/set1-1.jpg'
img1 = image2vector.read_image(path1)
path2 = r'../data/set1/set1-2.jpg'
img2 = image2vector.read_image(path2)

img1_resized = cv2.resize(img1, dsize=(1000, 1000))
img2_resized = cv2.resize(img2, dsize=(1000, 1000))
# cv2.imshow('Test: Resize', img2_resized)
# cv2.waitKey()
vector1 = image2vector.image_to_vector(img1_resized)
vector2 = image2vector.image_to_vector(img2_resized)
