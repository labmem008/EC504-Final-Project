# CITE
# Scikit-learn: Machine Learning in Python, Pedregosa et al., JMLR 12, pp. 2825-2830, 2011.
# API design for machine learning software: experiences from the scikit-learn project, Buitinck et al., 2013.
from helper.image2vector import read_image, image_to_vector, twoD_to_oneD, image_to_list2D
from sklearn.neighbors import KDTree
import pickle
import time
import numpy as np
import os
import pathlib


# initialize the image list, 30 is the number of test images in the database
imageList = [None] * 30
# loop through the data base and convert all images into simplified vectors


# input KD_Tree_image(k, input_image_index)
# 'k' is the number of nearest neighbor you want to find
# 'input_image_index' is the index of the image you are trying to find match/matches for
# example: KD_Tree_image(2, 21)
def KD_Tree_image(k, input_image_index):
    print('---Start image converting now---')
    for i in range(30):
        # print(str(i + 1))
        path = str(pathlib.Path(__file__).parent.absolute().parent.absolute()) + '\data\set1\set1-' + str(i + 1) + '.jpg'
        img = read_image(path)
        vector = image_to_list2D(img)
        ONED = twoD_to_oneD(vector)
        # print(ONED)
        imageList[i] = ONED.tolist()

    # KD-TREE starts here
    # start the timer now
    start_time = time.time()
    X = np.array(imageList, dtype=list)
    kdt = KDTree(X, leaf_size=30, metric='euclidean')
    kdt.query(X, k=k, return_distance=False)
    s = pickle.dumps(kdt)
    tree_copy = pickle.loads(s)
    dist, ind = tree_copy.query(X[input_image_index:input_image_index+1], k=k)
    print('distant is ' + str(dist))
    print('estimate image index is ' + str(ind))
    print("--- %s seconds ---" % (time.time() - start_time))
    # print(kdt.get_tree_stats())

# path = str(pathlib.Path(__file__).parent.absolute().parent.absolute()) + '\data\set1\set1-'
# print(path)
# KD_Tree_image(1, 21)
