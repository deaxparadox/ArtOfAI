# Linear discriminant analysis

Linear dicriminant analysis (LDA) is another commonly used feature extraction technique like PCA and  SVD.

The objective of LDA is similar to the sense that it intends to transform a dataset into a lower dimensional feature space. LDA focuses on class separability, i.e. separating the features based on class separability so as to avoid over-fitting of the machine learning model.

LDA calcuate eigenvalues and eigenvectors within a class and inter-class scatter matrics. Step to follow:

1. Calculate the mean vectors for the individual classes.
2. Calculate the intra-class and inter-class scatter matrices.
3. Calculate eigenvalues and eigenvectors of S<sub>W</sub><sup>-1</sup> and S<sub>B</sub>, where S<sub>W</sub> is the intra-class scatter matrix and S<sub>B</sub> is the inter-class scatter matrix.

![Eigenvalue and eigenvector for intra-class and inter-class matrix](/assets/images/linear-discriminant-analysis-1.png)

where, *m*<sub>i</sub> is the mean vector ofthe *i*-th class.

![Mean vector of i-th class](/assets/images/linear-discriminant-analysis-2.png)

where, *m*<sub>i</sub> is the sample mean for each class, *m* is the overall mean ofthe dataset, *N*<sub>i</sub> is the sample size of each class.

4. Identify the top '*k*' eigenvectors having top '*k*' eigenvalues.