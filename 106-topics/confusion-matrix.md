# Confusion matrix


### Definition

A matrix containing correct and incorrect predictions in the forms of `True Positive (TPs)`, `False Positive (FPs)`, `False Negative (FNs)`, `True Negative (TNs)` is known as **confusion matrix**.

### What is a Confusion Matrix?

A **confusion matrix** is a matrix  that summarizes the performance of a machine learning model on a set of test data. It is a mean of displaying the number of accurate and inaccurate instances based on the models predictions. It is often used to measure the performance of classification models, which aim to predict a categorical label for each input instance.

The matrix displays the number of instances produced by the model on the test data.

- **True Position (TP)**: The model correctly predicted positive outcome (The actual outcome was positive).
- **True Negative (TN)**: The model correctly predicted negative outcome (the acutal outcome was negative).
- **False Positive (FP)**: The model incorrectly predicted a positive outcome (the acutal outcome as negative). Also known as a Type I error.
- **False Negative (FN)**: The model incorrectly predicted a negative outcome (the acutal outcome as positive). Also known as a Type II error.

### Why do we need a Confusion Matrix?

A confusion matrix is used to evaluate the performance of the model. It offers thorough analysis of true position, true negative, false position, false negative predictions, facilitating a more prefound comprehension of a model's **recall**, **accuracy**, **precision**, and overall effectiveness in class distinction.

When there is an uneven class distribution in a dataset, this matrix is especially helpfull in evaluating a model's performance beyound basic accuracy metric.


#### Model accuracy 

Accuracy is used to measur the performance of the model. It is the ratio of Total correct instances to the total instances.


Model accuracy = (TP + TN) / (TP + FP + FN + FN)


#### Precision

Presion is a measure of how accurate a model's positive predictions are. It is defined as the ratio of true positive predictions to the total number of positive predictions made by the model.

Precision = TP / (TP + FP)


#### Recall
 
Recall measures the effectiveness of a classification model identifying all relevant instances from a dataset. It is the ratio of the number of true position (TP) instances to the sum of true positive and false negative (FN) instances.

Recall = TP / (TP + FN)


#### F1-Score

F1-score is used to evaluate the overall performance of a classification model. It is the harmonic mean of precision and recall.

F1-Score = 2 * Precision * Recal / (Presion = Recall)

We balance precision and recall with the F1-score when a trade-off between minimizing false positives and false negatives is necessary, usch as in information retrieval systems.


#### Specificity

Specificity is another important metric in the evaluation of classification models, particularly in binary classification. It measures the ability of a model to correctly identify negative instances. Specificity is also known as the True Negative Rate.

Specificity = TN / (TN + FP)

#### Error rate

Error rate = (FP + FN) / (TP + FP + FN + TN)


#### Kappa Value (k)

k  = (P(a) - P(p<sub>r</sub>)) / (1 - P(p<sub>r</sub>))


#### Type 1 and Type 2 error

##### Type 1 error

Type 1 error occurs when the model predicts a positive instance, but it is acutally negative. Precision is affected by false positives, as it is the ratio of true positives to the sum of true positives and false positives.

Type 1 Error = FP / (TN + FP)

##### Type 2 error

Type 2 error occurs when the model fails to predict a positive instance. Recall is directly affected by false negatives, as it is the ratio of true positives to the sum of true positives and false negatives.

Type 2 Error = FN / (TP + FN)

Precision emphasizes minimizing false positives, while recall focuses on minimizing false negatives.



- [Confusion matrix for Binary classification](../1000-other/confusion-matrix-binary-classification.ipynb)