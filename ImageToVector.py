# https://necromuralist.github.io/neural_networks/posts/image-to-vector/
import numpy
import cv2
import sys
# debug
# numpy.set_printoptions(threshold=sys.maxsize)

def read_image(path):
    img = cv2.imread(path)
    # Debug: imshow
    # cv2.imshow('Test IMSHOW', img)
    # cv2.waitKey()
    return img

def image_to_vector(image: numpy.ndarray) -> numpy.ndarray:
    # Convert a 3D array to a 1D vector
    # image: numpy array of shape (length, height, depth)
    # Retuan a vector of shape (length x height x depth, 1)
    length, height, depth = image.shape
    return image.reshape((length * height * depth, 1))

path = r'./data/profile.jpg'
img = read_image(path)
vector = image_to_vector(img)
print(vector.shape)
