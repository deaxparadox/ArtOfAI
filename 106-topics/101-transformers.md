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

This method defines a custom transformer by inheriting `BaseEstimator` and `TransformerMixin` classes of Scikit-Learn. 

`BaseEstimator` class of Scikit-Learn enables hyperparameter tuning by adding the `set_params` and `get_params` methods.

While, `TransformerMixin` class adds the `fit_transform` method without explicitly defining it.

```py
import pandas as pd
import numpy as np
from sklearn.base import BaseEstimator,TransformerMixin
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import FunctionTransformer
from sklearn.datasets import load_iris
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression

#Data Import
data = pd.DataFrame(load_iris()['data'],columns=['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm'])
data.head()


```
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>SepalLengthCm</th>
      <th>SepalWidthCm</th>
      <th>PetalLengthCm</th>
      <th>PetalWidthCm</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>5.1</td>
      <td>3.5</td>
      <td>1.4</td>
      <td>0.2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4.9</td>
      <td>3.0</td>
      <td>1.4</td>
      <td>0.2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4.7</td>
      <td>3.2</td>
      <td>1.3</td>
      <td>0.2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4.6</td>
      <td>3.1</td>
      <td>1.5</td>
      <td>0.2</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5.0</td>
      <td>3.6</td>
      <td>1.4</td>
      <td>0.2</td>
    </tr>
  </tbody>
</table>
</div>
```

```py
class OutlierRemover(BaseEstimator,TransformerMixin):
    def __init__(self,factor=1.5):
        self.factor = factor
        
    def outlier_detector(self,X,y=None):
        X = pd.Series(X).copy()
        q1 = X.quantile(0.25)
        q3 = X.quantile(0.75)
        iqr = q3 - q1
        self.lower_bound.append(q1 - (self.factor * iqr))
        self.upper_bound.append(q3 + (self.factor * iqr))

    def fit(self,X,y=None):
        self.lower_bound = []
        self.upper_bound = []
        X.apply(self.outlier_detector)
        return self
    
    def transform(self,X,y=None):
        X = pd.DataFrame(X).copy()
        for i in range(X.shape[1]):
            x = X.iloc[:, i].copy()
            x[(x < self.lower_bound[i]) | (x > self.upper_bound[i])] = np.nan
            X.iloc[:, i] = x
        return X
    
outlier_remover = OutlierRemover()
```

We've defined a class `OutlierRemover` which is our custom transformer to remove outliers i.e. replace outliers with `NaN`. The class has an attribute named `factor` which is a hyperparameter to control the outlier removal process. Higher the `factor`, extreme would the outliers removed. By default, `factor` is intialized to 1.5. The class has three metods, namely, `outlier_removal`, `fit`, and `transform`. Inheriting `BaseEstimator` and `TransformerMixin` classes adds three more methods, namely, `fit_transform`, `get_params` and `set_params`. We've also created an instance named `outlier_remover` of the `OutlierRemover` class.

`__init__` is the first method that's called upon creating an instance/object of the class. This is used to initialize the class attributes. We'll initialize the factor of the IQR method with 1.5 (default value). The `outlier_removal` method replaces the outliers in a Series with `NaN`