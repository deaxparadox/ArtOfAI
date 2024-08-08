# Overfitting

Overfitting refers to a model that models that training data too well.

Overfitting happens when a models learns the details and noise in the training data to the extend that it negatively impacts the performance of the model on new data. This means that the noise or random fluctuations in the training is picked up and learned as concepts by the model. The problem is that these concepts do not apply to new data and negatively impact that models ability to generalize.


Overfitting is more likely with nonparametric and nonlinear models that have more flexibility when learning a target function. As such, many nonparametric machine learning algorithms also include parameters of techniques to limit and constrain how much detail the model learns.

For example, decision trees are nonparametric machine learning algorith that is very flexible and is subject to overfitting training data. This problem can be addresses by pruning a tree after it has learned in order to remove some the detail it has picked up.


### How To Limit Overfitting

There are two important techniques that you can  use when evaluating machine learning algorithms to limit overfitting:

1. Use a resampling techniques to estimate model accuracy.
2. Hold back a validation dataset.

The most popular resampling technique is k-fold cross validation. It allows you to train and test your model k-times on different subsets of training data and build up an estimate of the performance of a machine learning model on unseen data.

A validation dataset is simply a subset of your training data that you hold back from your machine learning algorithms until the very end of your project. After you have selected and tuned your machine learning algorithms on your training dataset you can evaluate the learned models on the validation dataset to get a final objective idea of how the models might perform on unseen data.

Using cross validation is a gold standard in applied machine learning for estimating model accuracy on unseen data. If you have the data, using a validation dataset is also an excellent practice.