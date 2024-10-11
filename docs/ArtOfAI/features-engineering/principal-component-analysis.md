# Principal component analysis (PCA)

##### PCA is the most popular feature extraction algorithms using in machine learning.


### Table of Contents

- [Introduction](#introduction)
- [Concept of orthogonality](#concept-of-orthogonality)
    - [Principal component](#principal-component)
- [Objective of PCA](#objective-of-pca)

### Introduction

Any machine learning algorithm performs better as the number of related attributes or features reduced. In other words, a key to the success of the machine learning lies in the fact that the features are less in number as well as the similarity between each other is very less. This is the main guiding philosophy of principal component analysis (PCA) technique of feature extraction.

In PCA, a new set of features are extracted from the original features which are quite dissimilar in nature. So an *n*-dimensional feature space gets transformed to an *m*-dimensional feature space, where the dimensions are orthogonal to each other, i.e. completely independent of each other.


### Concept of Orthogonality

A vector is quantity that has both magnitude and direction and hence can determine the position of a point relative to another point in Euclidean space (i.e. a two or three or 'n' dimensional space). **A vector space is a set of vector**. Vectors spaces have a property that they can be represented as a linear combination of a smaller set of vectors, called **basis vectors**. So, any vector "v" is a vector space can be represented as;

![vector space equation](/assets/images/vector-space.png)

where a<sub>i</sub> represents "n" scalars and *u*<sub>i</sub> represents the basis vectors. **Basis vectors are orthogonal to each other.

*Orthogonality of a vectors* in *n*-dimensional vector space can be thought of an extension of the vectors being perpendicular in a two-dimensional vector space. Two orthogonal vectors are completely unrelated or independent of each other. So, the transformation of a set of vectos to corresponding set of basis vectors such that each vector in the original set can be expressed as a linear combination of basis vectors helps in decomposing the vectors to a number of independent components.


##### Principal component.

The feature vector can be transformed to a vector space of the basis vectors which are termed as **principal components**. These principal components, just like the basis vectors, are orthogonal to each other. So, a set of feature vectors which may have similarity with each other is transformed to a set of principal components which are completely unrelated. However, the principal components capture the variability of the original feature space. Also, the number of principal component derived, much like the basis vectors, is much smaller than the original set of features.


### Objective of PCA

To make the transformation in such a way that:

1. The new features are distinct, i.e. the covariance between the new features, i.e. the principal components is 0.
2. The principal components are generated in order of the variabitlity in the data that it captures. Hence, the first principal component should capture the maximum variability, the second principal component should capture the next highest variability etc.
3. The sum of variance of the new features or the principal components should be equal to the sum of variance of the original features.


PCA works based on a proces called eigenvalue decomposition of a covariance matrix of a data set. Below are the steps to be followed:

1. First, calculate the covariance matrix of a data set.
2. Then, calculate the eigenvalues of the covariance matrix.
3. The eigenvector having highest eigenvalue represents the direction in which there is the highest variance. So this will help in identifying the first principal component.
4. The eigenvector having the next highest eigenvalue represents the driection in which data has the highest remainning variance and also orthogonal to the first direction. So this helps in idetifying the second principal component.
5. Like this, identify the top '*k*' eigenvectors having top '*k*' eigenvalues so as to get the '*k*' principal components.