# Singular value decomposition

Singular value decomposition (SVD) is a matrix factorization technique commonly used in linear algebra. SVD of a matrix A (m x n) is a factorization of the form.

![Singular value decomposition](/assets/images/singular-value-decomposition-1.png)

where, *U* and *V* are orthonormal matrices, *U* is an *m* x *m* unitary matrix, *V* is  an *n* x *n* unitary matrix and ∑ is an *m* x *n* rectangular diagonal matrix. The diagonal entries of ∑ are known as singular values of matrix A. The columns of *U* and *V* are called *left-singular* and *right-singular* vectors of matrix A, respectively.

SVD is generally used in PCA, once the mean of each variable has been removed. Since it is not always advisable to remove the mean of data attribute, espically when  the data set if [sparse](/docs/glossary/sparse-dataset.md) (as is case of text data), SVD is a good choice for dimensionality reduction in those situations.


SVD of a data matrix is expected to have the properties highlighted below:

1. Patterns in the attributes are captured by the right-singular vectors, i.e. the columns of *V*.
2. Patterns among the instances are captured by the left-singular, i.e.e the columns of *U*.
3. Larger a singular value, larger is the part of the matrix A that it accounts for its associated vectors.
4. New data matrix with '*k*' attributes is obtained using the equation.

![new data matrix with 'k' attributes](/assets/images/singular-value-decomposition-2.png)

Thus the dimensionality get reduced to *k*. SVD is often used in the context of text data.


