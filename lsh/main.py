import os
import sys
import cv2
import numpy
import hash_table as ht
import lsh
image_size = 50
image_dimension = image_size * image_size * 3
def image_to_vector(image: numpy.ndarray) -> numpy.ndarray:
    length, height, depth = image.shape
    return image.reshape((length * height * depth, 1))
def load_images_from_folder(folder):
    vectors = []
    for files in os.listdir(folder):
        image = cv2.imread(os.path.join(folder,files))
        if image is not None:
        	image_resized = cv2.resize(image, dsize=(image_size, image_size))
        	vector = image_to_vector(image_resized)
        	vectors.append(vector.T)
    return vectors
path = r'../data/set1/'
vectors = load_images_from_folder(path)
num_tables = 4
hash_size = 10
inp_dimensions = image_dimension
project = lsh.LSH(num_tables, hash_size, inp_dimensions)
for index, val in enumerate(vectors):
	project.__setitem__(val, str(index))
# for table in project.hash_tables:
# 	print("Generating Hash Table...")
# 	items = table.hash_table.items()
# 	for item in items:
# 		print(item)
s = "Number of hash tables: " + str(num_tables)
print(s)
s = "Size of hash values: " + str(hash_size)
print(s)

query_numer = 0
s = "../data/query/query-" + str(query_numer) + ".jpg"
path = s
query_image = cv2.imread(s)
query_image_resized = cv2.resize(query_image, dsize=(image_size, image_size))
# cv2.imshow('Testing...', query_image_resized)
# cv2.waitKey()
query_vector = image_to_vector(query_image_resized).T

s = "The image ID that we want to search is query image " + str(query_numer)
print(s)
result = project.__getitem__(query_vector)
print("The image IDs that are similar to the query image are:")
print(result)

min_dist = int(sys.maxsize)
min_index = -1

for index in result:
    dist = numpy.linalg.norm(query_vector - vectors[int(index)])
    dist = round(dist, 2)
    if dist < min_dist:
        min_dist = dist
        min_index = int(index)
    # temp = "The distance between query and image " + str(index) + " is " + str(dist)
    # print(temp)

s = "The ID of the nearest neighbor of the query image is " + str(min_index) + " of distance "\
+ str(min_dist)
print(s)
