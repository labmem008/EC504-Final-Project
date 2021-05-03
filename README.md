# EC504-Final-Project Report



## Team information:
Hanming Wang (hita@bu.edu) U29135433 scc-username: hita

Yaopu Wang (yaopuw@bu.edu) U60843045 scc-username: yaopuw



## Abstract
Locality-sensitive hashing and KD-Tree

It is prohibitive to apply any brute-force algorithm to searching problems these days. In this project, we plan to research two classical types of algorithms. Locality-sensitive hashing is a technique that hashes similar input items into the same "buckets" with high probability. The K-dimensional tree is a space-partitioning data structure for organizing points in a k-dimensional space.

We plan to take advantage of the various third-party libraries of Python to implement the algorithms. We will implement LSH and KD-Tree. We will analyze their speed and accuracy and test them with an online database.



## Installation & Run Instructions
1. `cd` to root directory:

`cd hita`

`cd EC504-Final-Project`

. Run this:

`pip3 install -r requirements.txt`

2. Run this:

`python main.py`

   

### How to run each function Individually

###### LSH

1. Inside lsh/lsh_final.py, add the following line

2. ```python
   lsh_final_function(query_numer)
   # query_number is the image index you want to search in the data base
   ```

3. python lsh/lsh_final.py

###### KD-TREE

1. Inside kdtree/KD_Tree_function.py, add the following line

2. ```python
   KD_Tree_image(1, 21)
   # input KD_Tree_image(k, input_image_index)
   # 'k' is the number of nearest neighbor you want to find
   # 'input_image_index' is the index of the image you are trying to find match/matches for
   ```

3. python kdtree/KD_Tree_function



## File Distribution

- ##### LSH

  folder 'lsh' contains all the functions

- ##### KD-TREE

  folder 'kdtree' contains all the functions

- ##### helper functions

  folder 'helper' contains all the helper functions



## Sample Results

The first run is on LSH function. The run time illustrated for LSH is around 0.0248 seconds, with a correct output. The second run is on KD-tree function. The run time for KD-tree is around 0.02593 seconds. After testing for several times, we found the run time for LSH is slightly faster than that of KD-tree, given 30 datasets.

```command
---starting LSH now ---


Number of hash tables: 4
Size of hash values: 10
The image ID that we want to search is query image 22
The image IDs that are similar to the query image are:
['18', '11', '22', '17']
The ID of the nearest neighbor of the query image is 22 of distance 0.0
Time spent: 0.02482891082763672
---LSH ENDING ---


---starting kd_tree now ---


---Start image converting now---
distant is [[0.]]
estimate image index is [[22]]
--- 0.025930166244506836 seconds ---
---kd_tree ENDING ---



Process finished with exit code 0


```



## Introduction to Locality Sensitive Hashing: Random Projection Method
### Idea behind this method

Consider a image dataset matrix `D` with `n` vectors of size `d`. This database `D` can be projected onto a lower dimensional space with `n` vectors of size `k` using a random projection matrix.
### Algorithm
We construct a table of all possible bins where each bin is made up of similar items. Each bin can be represented by a bitwise hash value so that two images with same bitwise hash values are more likely to be similar than those with different hashes.

Steps to generate a bitwise hash table (this is our `hash_table.py`):

1. Create `k` random vectors of length `d` each, where `k` is the size of bitwise hash value and `d` is the dimension of the feature vector (in our case, this is the dimension of the image).
2. For each random vector, compute the dot product of the random vector and the image. If the result of the dot product is positive, assign the bit value as 1, else 0.
3. Concatenate all the bit values computed for `k` dot products.
4. Repeat the above two steps for all images to compute hash values for all images.
5. Group images with same hash values together to create a LSH table.


In addition, because of the randomness, it is not likely that all similar items are grouped correctly. To overcome this limitation, a common practice is to create multiple hash tables and consider an image `a` to be similar to image `b`, if they are in same bin in at least one of the tables. It is also worth noting that multiple tables generalize the high dimensional space better and amortize the contribution of bad random vectors.

In practice, the number of hash tables and size of the hash value `k` are tuned to adjust the trade-off between recall and precision.

`lsh.py` contains construction of multiple hash tables.





## KD-Trees

#### Ideas behind KD-Trees

In computer science, a k-d tree (short for k-dimensional tree) is a space-partitioning data structure for organizing points in a k-dimensional space. k-d trees are a useful data structure for several applications, such as searches involving a multidimensional search key (e.g. range searches and nearest neighbor searches) and creating point clouds. k-d trees are a special case of binary space partitioning trees.

The algorithm is as such:

- pick random dimension (X, Y...), find median, split data, repeat
- find NNs for a point
  - find region contain the point
  - compare to all points in that region





![k-d tree - Wikipedia](https://upload.wikimedia.org/wikipedia/commons/thumb/2/25/Tree_0001.svg/370px-Tree_0001.svg.png)

#### Library we used

[`sklearn.neighbors`](https://scikit-learn.org/stable/modules/classes.html#module-sklearn.neighbors) provides functionality for unsupervised and supervised neighbors-based learning methods. Unsupervised nearest neighbors is the foundation of many other learning methods, notably manifold learning and spectral clustering. In the function we loop over all the data images and convert them into small vectors. The list of image vectors are passed into provided KD-TREE library to run. The final output contains the run time, closest distance and neighbor index. 



## Resources
1. https://santhoshhari.github.io/Locality-Sensitive-Hashing/ *lsh*
2. https://necromuralist.github.io/neural_networks/posts/image-to-vector/ *image2vector*
3. https://docs.python.org/3/tutorial/venv.html *venv*
4. https://storage.googleapis.com/openimages/web/index.html *image database*
5. https://www.iloveimg.com/resize-image *this is not used*
6. http://unsample.net/ *image database*
7. https://caesium.app/ *compress images*
8. https://stackoverflow.com/questions/48121916/numpy-resize-rescale-image *cv2 resize*
9. https://imagecyborg.com/ *download images*
10. https://scikit-learn.org/stable/modules/neighbors.html KD-tree library
11. [Scikit-learn: Machine Learning in Python](http://jmlr.csail.mit.edu/papers/v12/pedregosa11a.html), Pedregosa *et al.*, JMLR 12, pp. 2825-2830, 2011.
12. [API design for machine learning software: experiences from the scikit-learn project](https://arxiv.org/abs/1309.0238), Buitinck *et al.*, 2013.

