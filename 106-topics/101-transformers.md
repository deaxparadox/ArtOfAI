### Transformers

Transformers are classes that enable data transformations while preprocessing the data for machine learning. Examples of transformers in Scikit-Learn are:

1. SimpleImputer
2. MixMaxScaler
3. OrdinalEncoder
4. PowerTransformer


We may require to perform data transformers that are not predefined in popular Python packages. In such cases, custom transformers come to the rescue.


Two methods of defining custom transformers in Python using Scikit-Learn:

1. [Method 1](#method-1)
2. Method 2


### Method 1

This method defines a custom transformer by inheriting `BaseEstimator` and `TransformerMixin` classes of Scikit-Learn