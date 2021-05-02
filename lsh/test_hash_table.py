import sys
sys.path.append('../../EC504-Final-Project/helper/')
import image2vector
import hash_table as ht
import numpy as np
import cv2
'''
A module is a file containing Python code. 
A package, however, is like a directory that holds sub-packages and modules.
'''
path1 = r'../data/set1/set1-1.jpg'
img1 = image2vector.read_image(path1)
img1_resized = cv2.resize(img1, dsize=(500, 500))
vector1 = image2vector.image_to_vector(img1_resized)
d = len(vector1)
vector1 = vector1.T
# print(vector.shape)
table = ht.HashTable(5, d)
# value = table.generate_hash(vector)
# print(value)
table.__setitem__(vector1, "image1")
vector2 = vector1
table.__setitem__(vector2, "image2")

items = table.hash_table.items()
for item in items:
	print(item)
