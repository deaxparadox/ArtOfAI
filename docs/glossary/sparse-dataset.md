# Sparse dataset

### What is sparse dataset?

The features of a  dataset can be sparse or dense. IF the data stored for a particular features contains mostly zeros, it is referred to as a **sparse** feature. It the feature is populated mostly with non-zero values, it is **dense**. Most machine learning features are developed for dense features. A dataset with a significant number of sparse features is denoted as a sparse dataset.

### Challgenges of Using Sparse Datasets

- **Overfitting**: When high cardinality categorical features are one-hot encoded, we end up with a lot of features. In this situation, the model starts overfitting on the features and models  the noise also.

- **High memory usage**: Sparse matrices occupy an enormous amount of memory, and working with them is difficult. 

- **Computational complexity**: When dealing with large sparse matrices, every operation involving them, including simple multiplication, would require heavy computational power.

- **Inaccurate results**: When we have sparse features and apply these models, they may behave unexpectedly, leading to biased results.