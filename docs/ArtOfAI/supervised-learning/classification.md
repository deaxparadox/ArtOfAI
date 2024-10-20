# Supervised learning: Classification

### Introduction

We already known, When we are trying to predict a categorical or nominal variable, the problem is known as **classification problem**. *If you have'nt read about supervised learning, then [click here](README.md)*.

### What is classification problem?

A classification problem is one where the output variable is a category such as "red" or "blue" or "malignant tumour" or "benign tumour", etc.

In classification, the whole problem centres around assigning a label or category or class to a test data on the basis of the label or category or class information that is imparted by the training data. Because the target objective is to assign a class label, we call this type of problem as a classification problem.


![Image not found](/assets/images/supervised-learning-2.png)

The above image depicts the typical process of classification where a classification model is obtained from the labelled traning data by a classifier algorithm. On the basis of the model, a class label is assigned to the test data.

A critical classification problem in the context of the banking domain is identifying potentially fraudulent transactions. Because the are millions of transactions which are to be scrutinized to identify whether a particular transaction might be a fraud transaction, it is not possible for any human being to carry out this task. Machine learing leveraged efficiently to do this task, and this is a classic case of classification. On the basis of the past transaction data, especially the ones labelled as fraudulent, all new incoming transactions are marked or labelled as usual or suspicious. The suspicious transactions are subsequently segregated for a closer review.



##### Classifiction algorithms

Classification algorithms are used for classification an object in category. If we have collections of movie, and we want to classify each movie according to it description. We can use classification model for this case.

- [Logistic regression](logistic-regression.md)

