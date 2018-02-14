# Example of kNN implemented from Scratch in Python

import numpy as np
from sklearn import datasets
'''
Before we actually start with writing a nearest neighbor classifier, we need to think about the data, i.e. the testset. 
We will use the "iris" dataset provided by the datasets of the sklearn module.

The data set consists of 50 samples from each of three species of Iris

Iris setosa,
Iris virginica and
Iris versicolor.
Four features were measured from each sample: the length and the width of the sepals and petals, in centimetres.'''

iris = datasets.load_iris()
iris_data = iris.data
iris_labels = iris.target
print(iris_data[0], iris_data[79], iris_data[100])
print(iris_labels[0], iris_labels[79], iris_labels[100])

''' We create a trainset from the sets above. We use permutation from np.random to split the data randomly. '''
np.random.seed(42)
indices = np.random.permutation(len(iris_data))
n_training_samples = 12
trainset_data = iris_data[indices[:-n_training_samples]]
trainset_labels = iris_labels[indices[:-n_training_samples]]
testset_data = iris_data[indices[-n_training_samples:]]
testset_labels = iris_labels[indices[-n_training_samples:]]
print(trainset_data[:4], trainset_labels[:4])
print(testset_data[:4], testset_labels[:4])

'''
The following code is only necessary to visualize the data of our testset, not a part of the course. 
Our data consists of four values per iris item, so we will reduce 
the data to three values by dropping fourth value. You can change the dimensions on lines 48-50 
This way, we are capable of depicting the data in 3-dimensional space:
'''

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
colours = ("r", "b")
X = []
for iclass in range(3):
    X.append([[], [], []])
    for i in range(len(trainset_data)):
        if trainset_labels[i] == iclass:
            X[iclass][0].append(trainset_data[i][0])
            X[iclass][1].append(trainset_data[i][1])
            X[iclass][2].append((trainset_data[i][2]))
colours = ("r", "g", "y")
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
for iclass in range(3):
       ax.scatter(X[iclass][0], X[iclass][1], X[iclass][2], c=colours[iclass])
plt.show()

