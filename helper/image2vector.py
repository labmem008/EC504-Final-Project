# https://necromuralist.github.io/neural_networks/posts/image-to-vector/
import numpy
from PIL import Image
import numpy as np
import cv2
import sys
# debug
# numpy.set_printoptions(threshold=sys.maxsize)

def read_image(path):
    img = cv2.imread(path)
    img = cv2.resize(img, dsize=(50, 50))
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

def image_to_list2D(image: numpy.ndarray) -> numpy.ndarray:
    # Convert a 3D array to a 2D vector
    length, height, depth = image.shape
    return image.reshape(1, (length * height * depth))


def twoD_to_oneD(vector):
    ini_array1 = np.array(vector)
    # printing initial arrays
    # print("initial array", str(ini_array1))

    # Multiplying arrays
    result = ini_array1.flatten()
    return result
    # printing result
    # print("New resulting array: ", result)

# def pillowMethod():
#     temp = asarray(Image.open('test.jpg'))
#     for j in temp:
#         new_temp = asarray([[i[0], i[1]] for i in j])  # new_temp gets the two first pixel values

# X = []
#
# imageList = np.zeros(shape=(1,30912))
# path = 'D:\Desktop\BUclass\EC504 Algo&DataStruct\EC504-Final-Project\data/att-database-of-faces\s1/1.pgm'
# img = read_image(path)
# vector = image_to_vector(img)
# # A = twoD_to_oneD(vector)
# print(vector.flatten())
# print(A)
# np.put(imageList, , vector)
# print(imageList)
# ONED = twoD_to_oneD(vector)
# print(ONED)
# X.append(ONED.tolist())
#
# path = 'D:\Desktop\BUclass\EC504 Algo&DataStruct\EC504-Final-Project\data/att-database-of-faces\s1/2.pgm'
# img = read_image(path)
# vector = image_to_vector(img)
# print(vector)
# ONED = twoD_to_oneD(vector)
# # print(ONED.tolist())
#
#
# X.append(ONED.tolist())
# print(X)
