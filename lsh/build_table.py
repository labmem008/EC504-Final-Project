import os
import sys
import cv2
import numpy
import hash_table as ht

def image_to_vector(image: numpy.ndarray) -> numpy.ndarray:
    length, height, depth = image.shape
    return image.reshape((length * height * depth, 1))

def load_images_from_folder(folder):
    vectors = []
    for files in os.listdir(folder):
        image = cv2.imread(os.path.join(folder,files))
        if image is not None:
        	image_resized = cv2.resize(image, dsize=(250, 250))
        	vector = image_to_vector(image_resized)
        	vectors.append(vector.T)
    return vectors

path = r'../data/set1/'
vectors = load_images_from_folder(path)
# print(len(vectors))
# print(vectors[0].shape)
# print(len(vectors[0]))

table = ht.HashTable(5, 187500)
for index, val in enumerate(vectors):
	table.__setitem__(val, str(index))

items = table.hash_table.items()
for item in items:
	print(item)
