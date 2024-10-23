# Supervised learning: Classification

### Introduction

We known, when we are try to predict a categorical or nominal variable, the problem is known as **classification problem**. *If you have'nt read about supervised learning, then [click here](README.md)*.

### What is classification problem?

A classification problem is one where the output variable is a category such as "red" or "blue" or "malignant tumour" or "benign tumour", etc.

In classification, the whole problem centres around assigning a label or category or class to a test data on the basis of the label or category or class information that is imparted by the training data. Because the target objective is to assign a class label, we call this type of problem as a classification problem.


![Image not found](/assets/images/supervised-learning-2.png)

The above image depicts the typical process of classification where a classification model is obtained from the labelled traning data by a classifier algorithm. On the basis of the model, a class label is assigned to the test data.

A critical classification problem in the context of the banking domain is identifying potentially fraudulent transactions. Because the are millions of transactions which are to be scrutinized to identify whether a particular transaction might be a fraud transaction, it is not possible for any human being to carry out this task. Machine learing leveraged efficiently to do this task, and this is a classic case of classification. On the basis of the past transaction data, especially the ones labelled as fraudulent, all new incoming transactions are marked or labelled as usual or suspicious. The suspicious transactions are subsequently segregated for a closer review.

----------

In summary, clasification is a type of supervised learning where a target feature, which is of categorial type, is predicted for test data on the basis of the information imparted by the training data. The target categorical feature is known as **class**.

----------


### Classification problem

- Image classfication
- Disease prediction
- Win-loss prediction of games
- Prediction of natural calamity such as earthquake, flood, etc.
- Handwritting recognition

### Classification learning steps

First, there is a problem which to be solved, and then, the required data (related to the problem, which is already stored in the system), is evaluated and pre-processed based on the algorithm. Algorithm selection is a critical point in supervised learning. The result after iterative training rounds is a classifier for the problem in hand.

![Image not found](/assets/images/supervised-learning-3.png)

**Problem Identification**: Identifying the problem is the first step in the supervised learning model. The problem needs to be a well-formed problem, i.e. a problem with well-defined goals and benefit, which has a long-term impact.


**Identification of required data**: On the basis of the problem identified above, the required data set that precisely represents the identified problem needs to be identified/evaluted. For example: the problem is to predict whether a tumour is malignant of benign, the corresponding patient data sets related to malignant tumour and benign tumours are to be identified.

**Data Pre-processing**: This is related to the cleaning/transforming the data set. This step ensures that all the unnecessary/irrelevant data elements are removed. Data pre-processing refers to the transformations applied to the identifieddata before feeding the same into the algorithm. Because the data is gathered from different sources, it is usually collected in raw format and is not ready for immediate analysis. This step ensures tha the data is ready to be fed into the machine learning algorithm.

**Definition of training data set**: Before starting the analysis, the user should decide what kind of data set is to be used as a training set. In the case of signature analysis, for example, the training data set might be  a single handwritten alphabet, an entire handwritten word (i.e. a group of the alphabets) or an entire line of handwriting (i.e. sentences of a group of words). Thus, a set of "input meta-objects" and corresponding "output meta-objects" are also gathered. The training set needs to be actively representative ofthe real-world use of the given scenario. Thus, a set of data input (*X*) and corresponding outputs (*Y*) is gathered either from human experts or experiments.

**Training**: The learning algorithm identified is the previous step to run on the gathered training set for further fine turning. Some supervised learning algorithms require the user to determine specific control parameters (which are given as inputs to the algorithm). These parameters (inputs given to algorithm) may also be adjusted by optimizing performance on a subset (called as validation set) of the training set.

**Evaluation with the test data set**: Training data is run on the algorithm, and its performance is measured here. If a suitable result is not obtained, further training of parameters may be required.


##### Common classifiction algorithms


- [Logistic regression](logistic-regression.md)
- [*k*-Nearest neighbor](k-nearest-neighbor.md)
- [Decision tree](decision-tree.md)
- [Random forest](random-forest.md)
- [Support Vector Machine](support-vector-machine.md)
- [Naive bayes classifiers](naive-bayes-classifiers.md)

