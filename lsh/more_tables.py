import os
import sys
import cv2
import numpy
import hash_table as ht
import lsh
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
num_tables = 3
hash_size = 10
inp_dimensions = 187500
project = lsh.LSH(num_tables, hash_size, inp_dimensions)
for index, val in enumerate(vectors):
	project.__setitem__(val, str(index))
# for table in project.hash_tables:
# 	print("Generating Hash Table...")
# 	items = table.hash_table.items()
# 	for item in items:
# 		print(item)
print("Query result:")
result = project.__getitem__(vectors[31])
print(result)
