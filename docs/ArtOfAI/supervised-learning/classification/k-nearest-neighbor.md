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


In context of the Student data set, to keep the things simple, we assume one data element of the input data set as the test data, the record of the student named Josh is assumed to be the test data. Now that we have the training data nd test data identified, we can start with the modelling.