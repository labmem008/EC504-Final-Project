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
path = r'../data/set1/set1-1.jpg'
img = image2vector.read_image(path)
img_resized = cv2.resize(img, dsize=(500, 500))
vector = image2vector.image_to_vector(img_resized)
d = len(vector)
vector = vector.T
# print(vector.shape)
table = ht.HashTable(5, d)
value = table.generate_hash(vector)
# print(value)
table.__setitem__(vector, "label1")

items = table.hash_table.items()
for item in items:
	print(item)
