# Feature subset selection


Also called **Feature selection**, is this case no new feature is generated. The object of feature selection is to derive a subset of features from the full feature set which is most meaningful in the context of a specific machine learning problem. So, essentially the job of feature selection is to derive a subset *F<sub>j</sub>(F<sub>1</sub>, F<sub>2</sub>, ..., F<sub>m</sub>) of F<sub>i</sub>(F<sub>1</sub>, F<sub>2</sub>, ..., F<sub>n</sub>)*, where  *m* < *n*, such that F<sub>j</sub> is more meaningful and gets the best result for a machine learning problem.


Feature selection is arguably the most critical pre-processing activity in any machin learing project. It intends to select a subset of system attributes or features which makes a most meaningfull contribution in a machine learing activity.

Lets understand the important of feature selection with the help of example. Say we are trying to predict the weight of students based on past information about similar students, which is captured in a "student weight" data set. The student weight data set has features such as "Roll Number", "Age", "Height" and "Weight". The features "Roll number" have no bearing, whatsoever, in prediction student weight. So we can eliminate the feature roll number and build a feature subset to be considered in this machine learning problem.

The original data:

| Roll Number | Age | Height | Weight |
|-----|-----|-----|-----|
| 12 | 12 | 1.1 | 23 |
| 14 | 11 | 1.05 | 21.6 |
| 19 | 13 | 1.2 | 24.7 |
| 32 | 11 | 1.07 | 21.3 |
| 38 | 14 | 1.24 | 25.2 |
| 45 | 12 | 1.12 | 23.4 |

Selected features dataset:

| Age | Height | Weight |
|-----|-----|-----|
| 12 | 1.1 | 23 |
| 11 | 1.05 | 21.6 |
| 13 | 1.2 | 24.7 |
| 11 | 1.07 | 21.3 |
| 14 | 1.24 | 25.2 |
| 12 | 1.12 | 23.4 |



### Issues in high-dimensional data

The text data generated from different sources have exteremly high dimensions (or consider any with thousands of features). In a large document corpus having few thousand documents embedded, the number of unique word tokens which represent the feature of the text data set, can also be in the range of a few tens of thousands. To get insight from such high-dimensional data may be a big challenge for a machine learning algorithm.

On one hand, very high quantity of computational resources and high amount of time will be required. On the other hand the performance of the model both foor supervised and unsupervised machine learning task, also degrades sharply due to unnecessary noise in the data. Also, a model built on an extremently hight number of features may be very difficult to understand. For this reason, it is necessary to take a subset of the features instead of the full set.

The objective of feature selection is three-fold:

- Having faster and more cost-effective (i.e. less need for computational resources) learning model.
- Improving the efficiency of the learning model.
- Having a better understanding of the underlying model that generated the data.

### Key drivers of feature selection -- feature relevance and redundancy

##### Feature relevance

In supervised learning, the input data set which is the training data set, has a class label attached. A models is inducted based on the training data set -- so that the inducted model can assign class labels to new, unlabelled data. Each of the predictor variables, is expected to contribute information to decide the value of the class label. In case a variable is not contributing any information, it said to be irrelevant. In case the information contribution for prediction is very little, the variable is said to be weakly relevant. Remaining variables, which make a signigicant contribution to the prediciton task are said to be strongly relevant variables.

In unsupervised learning, there is no training data set or labelled data. Grouping of similar data instances are done and similarity of data instances are evaluated based on the value of different variables. Certain variables do not contribute any usefull information for deiding the similarity of dissimilarity of data instances. Hence, those variables make not significant information contribution in the grouping process. These variables are marked as irrelevant variables in the context of the unsupervised machine learning task.

Any feature which is irrelevant in the context of a machine learning task is a condidate for rejection when we are selecting a subset of features.

##### Feature redundancy

A feature may contribute information which is similar to the information contributed by one or more other features.

For example, above we took an example of "Age", "Height", and "Weight". Both the features "Age", and "Height" contribute similar information. This is because with an increase in "Age", "Weight" is expected to increase. Similarly, with the increase of "Height" also "Weight" is expect to increase. Also, "Age" and "Height" increases with each other. So, in context of this problem, "Age", "Height" contribute similar information. In other words, irrespective of whether the feature height is present as a part of feature subset, the learning model will give almost same results. In the same way, without age being part of predictor variables, the outcome of the learning model will be more or less same. In this kind of situation when one feature is similar to another feature, the feature is said to be potentially redundant in the context of the learning problem.

All features having potential redundancy are candidates for rejection in the final features subset. Only a small number of represetative features out of a set of potentially redundant features are condiered for being a part of the final feature subset.

So, **the main object of feature selection** is to remove all features which are irrelevant and take a representative subset of the features which are potentially redundant. This leads to a meaningful feature subset in context of a specific learning task.


### Measures of features relevance and redundancy.

##### Measures of feature relevance.