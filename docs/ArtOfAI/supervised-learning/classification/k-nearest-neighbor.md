# *k*-Nearest Neighbor (*k*NN)

### Introduction

The *k*NN algorithm is a simple but extremely powerful classification algorithm. The name of the algorithm originates from the underlying philosophy of *k*NN - i.e. people having similar background or mindset tend to stay close to each other.

In others words, neighbors in a locality have a similar background. In the same way , as a part of the *k*NN algorithm, the unknown and unlabelled data which comes for a prediction problem is judged on the basis of  the training data set elements which are similar to the unknown element. So, the class label of the unknown element is assigned on the basis of the class labels of the similar training data set elements (metaphorically can be considered as neighbors of the unknown element).

### How *k*NN works

Let us consider a very simple Student data set.

| Name | Aptitude | Communication | Class |
|------|-----|------|------|
| Karuna | 2 | 5 | Speaker |
| Bhuvna | 2 | 6 | Speaker |
| Gaurav | 7 | 6 | Leader |
| Parul | 7 | 2.5 | Intel |
| Dinesh | 8 | 6 | Leader |
| Jani | 4 | 7 | Speaker |
| Bobby | 5 | 3 | Intel |
| Parimal | 3 | 5.5 | Speaker |
| Govind | 8 | 3 | Intel |
| Susant | 6 | 5.5 | Leader |
| Gouri | 6 | 4 | Intel |
| Bharat | 6 | 7 | Leader |
| Ravi | 6 | 2 | Intel |
| Pradeep | 9 | 7 | Leader |
| Josh | 5 | 4.5 | Intel |

It consists of 15 students studying in a clas. Each of the students has been assigned a score on a scale of 10 on two performance parameters -- 'Aptitude' and 'Communication'. Also, a class value is assigned to each student based on the following criteria:

1. Students having good communication skills as well as a good level of aptitude have been classified as "Leader".
2. Students having good communication skills not so good level of aptitude have been a classified as "Speaker".
3. Students having not so good communication skill but a good level of aptitude have been classified as "Intel".

----------

#### Remember:

While building a supervised learning model, a part of the labelled input data is retained as test data. The remaining portion of the input data is used to train the model--hence known as training data. The motivation to retain a part of the data as test data is to evaluate the performance ofthe model. As we have seen, the performance of the classification model is measured by the number of correct classifications made by the model when applied to an unknown data set. However, it is not possible during model testing to know the acutal label value of unknown data. Therefore, the test data, which is part of the labelled input data, is used for this purpose. If the class value predicted for most of the test data elements matches with the acutal class value that they have, then we say that  the classification model posses a good accuracy. 
 
----------


In context of the Student data set, to keep the things simple, we assume one data element of the input data set as the test data, the record of the student named Josh is assumed to be the test data. Now that we have the training data and test data identified, we can start with the modelling.

In the *k*NN, algorithm the class label of the test data elements is decided by the class label of the training data elements which are neighbouring, i.e. similar in nature. But there are two challenges:

1. What is the basis of the similarity or when can we say that two data elements are similar?
2. How many similar elements should be considered for deciding the class label of each test data element?

###### What is the basis of the similarity or when can we say that two data elements are similar?

There are many measures of similarity, the most common approach adapted by *k*NN to measure similarity between two elements are **Euclidean** distance. Considering a very simple data set having two features (say $f_1$ and $f_2$), Euclidean distance between two data elements $d_1$ and $d_2$ can be measured by

$$Euclidean{\;}distance = \sqrt{{\left(f_{11} - f_{12}\right)}^2 + {\left(f_{21} - f_{22}\right)}^2}$$

where $f_{11} =$ value of features $f_1$ for data element $d_1$.
where $f_{12} =$ value of features $f_1$ for data element $d_2$.
where $f_{21} =$ value of features $f_2$ for data element $d_1$.
where $f_{22} =$ value of features $f_2$ for data element $d_2$.

We have splitted the data into *train* set and *test* set.


- Training set 

| Name | Aptitude | Communication | Class |
|------|-----|------|------|
| Karuna | 2 | 5 | Speaker |
| `content skipped` | `content skipped` | `content skipped` | `content skipped` |
| Pradeep | 9 | 7 | Leader |


- Test set

| | | | |
|------|-----|------|------|
| Josh | 5 | 4.5 | Intel |

The training data points of the Student data set considering only the features "Aptitude" and "Communication" can be represented as dots in a two-dimensional feature space. The reason for considering two-dimensional data space is that we are considering just the two features of the Student data set, i.e. 'Aptitude' and 'Communication' for doing the classification. The feature "name" is ignored because, as we understand, it has no role to play in deciding the class value. To find out the closest or nearest neighbours of the test data point, Euclidean distance of the different dots need to be calculated. Then, the class value of closest neighbors helps in assigning the class value of the test data element.

###### How many similar elements should be considered for deciding the class label of each test data element?

To find the answer to this question, i.e. how many similar elements should be considered. The answer lies in the value of '*k*' which is a user-defined parameter given as an input to the algorithm. In the *k*NN algorithm, the value of '*k*' indicates the number of neighbors that need to be considered. For example, if the value of *k* is 3, only three nearest neighbours or three training data elements closest to the test data elements are considered. Out of the three data elements, the class which is predominant is considered as the class label to be assigned to  the test data. In case the value of *k* is 1, only the closest training data element is considered. The class label of that data element is directly assigned to the test data element.


| Name | Aptitude | Communication | Class | Distance | *k*=1 | *k*=2 | *k*=3 |
|------|-----|------|------|------|------|------|------|
| Karuna | 2 | 5 | Speaker | 3.041 | | | |
| Bhuvna | 2 | 6 | Speaker | 3.354 | | | |
| Parimal | 3 | 5.5 | Speaker | 2.236 | | | |
| Jani | 4 | 7 | Speaker | 2.693 | | | |
| Bobby | 5 | 3 | Intel | 1.500 | | | 1.500 |
| Ravi | 6 | 2 | Intel | 2.693 | | | |
| Gouri | 6 | 4 | Intel | 1.118 | 1.118 | 1.118 | 1.118 |
| Parul | 7 | 2.5 | Intel | 2.828 | | | |
| Govind | 8 | 3 | Intel | 3.354 | | | |
| Susant | 6 | 5.5 | Leader | 1.1414 | | | |
| Bharat | 6 | 7 | Leader | 2.693 | | | |
| Gaurav | 7 | 6 | Leader | 2.500 | | | |
| Dinesh | 8 | 6 | Leader | 3.354 | | | |
| Pradeep | 9 | 7 | Leader | 4.717 | | | |
| Josh | 5 | 4.5 | ??? | | | | |

Let us now try to find out the outcome of the algorithm for the Student data set we have. *We will see what class value KNN will assign for the test data for student Josh*. As shown in above table, when the value of *k* is taken as 1, only one trainig data point needs to be considered. The training record for student Gouri comes as the closest one to to test record of Josh, with a distance value of 1.118. Gauri has class value "Intel". When the value of *k* is assumed as 3, the closest neighbors of Josh in the training data set are Gouri, Susant, and Bobby with distances being 1.118, 1.414, and 1.5, respectively. Gouri and Bobby have class value "Intel", while Susant has class value "Leader".  In this case, the class value of "Intel" is formed by majority **voting**. Because the class value of "Intel" is formed by the majority of the neighbors, the class value of Josh is assigned as "Intel". This same process can be extended for any value of k.

### The value of *k*

It is often tricky decision to decide the value of *k*. The reasons are as follow:

- If the value of *k* is very large (in the extreme case equal to the total number of records in the training data), the data label of the majority class of the training data set will be assigned to the test data regardless of the class labels of the neighbours nearests to the test data.
- If the value of *k* is very small (in the extreme case equal to 1), the class value of a noisy data or outlier in the training data set which is the nearest neighbour to the test data will be assigned to the test data.

The best *k* value is somwhere between these two extermes.

Few strategies, highlighted below are adapted by machine learning practiciners to arrive at a value for *k*.

- One common practice is to set *k* equal to the square root of the number of training records.
- An alternative approach is to test several *k* values on a variety of test data sets and choose the one that delivers the best performance.
- Another interesting approach is to choose a large value of *k*, but apply a weighted voting process in which the vote of close neighbours is considered more influential than the vote of distant neighbours.

### *k*NN algorithm

**Input**: The training data set, test data set (or data points) value of *'k'*, (i.e. number of nearest neighbours to be considered)

**Steps**:

```
Do for all, test data points

    Calculate the distance (usually euclidean distance) of the test data points from the different training data points.
    Find the closes 'k' training data points, i.e. training data points whose distances are least from the test data point.

If, k = 1

    Then, assign class label of the training data point to the test data point

Else,

    Whichever class label is predominantly present in the training data points, assign that class label to the test data point.

End do,

```


### Why the *k*NN algorithm is called lazy learner?

The eager learners follow the general steps of machine learning, i.e. perform an abstraction of  the information obtained from the input data and then follow it through by a generalization step.

However, the *k*NN algorithm these steps are completely skipped. It stores the training data and reictly applies the philosophy of nearest neighbourhood finding to arrive at the classification. So, for *k*NN these is no learning happening in real sense. Therefore, *k*NN falls under the category of lazy learner.


### Strengths of the *k*NN algorithm

- Extermely simple algorithm - easy to understand
- Very effective in certain situations, e.g. for recommender system design
- Very fast or almost no time required for the training phase.

### Weaknesses of the *k*NN algorithm

- Does not learn anything in the real sense. Classification is done completely on the basis of the training data. So, it has a heavy reliance on the training data. If the training data does not represent the problem domain comprehensively, the algorithm fails to make an effective classification.
- Because there is no model trained in real sense and the classification is done completely on the basis of the training data, the classification process is very slow.
- Also, a large amount of computational space is required to load the training data for classfication.

### Application of *k*NN algorithm

One of the most popular areas in machine learning where the *k*NN algorithm is widely adapted is recommender systems. Recommender system recommend users different items which are similar to a particular item that the user seems to like. The liking pattern may be revealed from past purchases or browsing history and the similar items are identified using the *k*NN algorithm.

Another area where there is widespread adoption of kNN is searching documents/ contents similar to a given document/content. This is a core area under information retrieval and is known as concept search.

### Code

- [KNN code](/code/ipynb/simple-knn.ipynb)

### Reference

- [Machine Leanring, by Saikat Dutt](https://https://www.amazon.in/Machine-Learning-Saikat-Dutt/dp/9353066697/ref=sr_1_1?crid=LUO9GQVWS7AK&dib=eyJ2IjoiMSJ9.Z6dFIzdCraM14LF92a0KLfpv-YbXKK_tn5ZIPAZkgzPGjHj071QN20LucGBJIEps.MXciqU1-jZAO6U-Q_afECWl-QR89g9lBKqj1ltDItvA&dib_tag=se&keywords=machine+learning+saikat+dutt&qid=1729954376&sprefix=machine+learing+saikat%2Caps%2C208&sr=8-1)