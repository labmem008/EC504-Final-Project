import sys
sys.path.append('../../EC504-Final-Project/helper/')
import image2vector
import hash_table as ht
'''
A module is a file containing Python code. 
A package, however, is like a directory that holds sub-packages and modules.
'''
path = r'../data/set1/set1-1.jpg'
img = image2vector.read_image(path)
vector = image2vector.image_to_vector(img)
d = len(vector)
# print(d)
# print(vector.shape)

table = ht.HashTable(5, d)
value = table.generate_hash(vector)
print(value)
