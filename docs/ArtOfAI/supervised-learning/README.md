# Supervised Learning

### Table of content

- [What is Supervised learning](#what-is-supervised-learning)
- [How supervised learning works](#how-supervised-learning-works)
- [Supervised learning algorithm](#supervised-learning-algorithms)
    - [Neural networks](#neural-networks)
- [Algorithms in supervised learning](#algorithms-in-supervised-learning)

### What is Supervised learning

Supervised leraning, also known as supervised machine liearning, is a subcategory of machine learning and artificial intelligence. It is defined by its use of labeled data sets to train algorithms that to classify data or predict outcomes accurately.

As input data is fed into the model, it adjusts it weights until the model has been fitted appropriately, which occurs as part of the cross validation process. 

Supervised learning helps organization solve for a variety of real-world problems at scale, such as classifying spam in a seprate folder from your inbox. It can be used to build highly accurate machine learning models.

### How supervised learning works

Supervised learning uses a training set to teach models to yield the disired output. This training dataset include inputs and correct ouputs, which allow the model to learn over time. The algorithm measures it accuracy through [loss function](https://) adjusting until the error has been sufficiently minimized.

Supervised leraning can be separated into two types of problems when [data mining](https://) -- classification and regression:

1. [Classification](#classification)
2. [Regression](#regression)

##### Classification

Uses an algirhtm to accurately assign test data into specific categories. It recognizes specific entities within the dataset and attempts to draw some conclusion on how those entities should be labeled or defined.

Common classification algorithms:

- [Linear classifiers](https://)
- [Support vector machines](https://) (SVM)
- [Decision trees](https://)
- [K-nearest neighbor](https://)
- [Random forest](https://)

##### Regression

It is used to understand the relationship between dependent and independent variables. It is commonly used to make projections, such as for sales revenue for a given business.

Common regression algorithms:

- [Linear regression](https://)
- [Logistical regression](https://)
- [Polynomial regression](https://)


In supervised learning, you create a function (or model) by using labeled training data that consists of input data and a wanted output. The supervision comes in a form of the wanted output, which in turn lets you adjust the function based on the acutal output it produces. When trained, you can apply this function to new observations to produce an output (predictions or classfication) that ideally responds correctly.

A typical supervised learning algorithm

[Typical supervised learning ](/assets/images/supervised-learning-1.png)


### Supervised learning algorithms

Commonly used supervised learing algorithms:

##### Neural Networks

Primary leveraged for deep learing algorithms, [neural networks](https://) process training data by mimicking the interconnectivity of the human brain layers of nodes. Each node is made up of inputs, weights, a bias (or thresold), and an output. If that output values exceeds a given thresold, it "fires" or activates the node, passing data to the next layer in the network. Neural networks learn this mapping function through supervised learning, adjusting based on the loss function through the process of [gradient descent](https://). When the [cost function](https://) is at or the near zero, we can be confident in the model's accuracy to yield the correct answer.


##### Naive Bayes

Naive Bayes is classification approach that adopts the principle of class conditional independence from the Bayes Theorem. This means that the presence of one feature does not impact the presence of another in the probability of a given outcome, and each predictor has an equal effect on that result.

There are three types of Naive Bayes classifiers:

1. Multinomial Naive Bayes
2. Bernoulli Naive Bayes
3. Gaussian Naive Bayes

This techniques is primary used in [text classification](https://), [spam detection](https://), and [recommemdation system](https://).


##### Linear regression

Linear regression is used to identify the relationship between a dependent variable and one or more independent variables and is typically leveraged to make predictions about future outcomes. 

When there is only one independent variable and one dependent variable, it is known as **simple linear regression**.

As the number of independent variables increases, it is referred to as **multiple linear regression**.

For each type of linear regression, it seeks to plot a line of best fit, which is calulated through the method of least squares. However, unlike other regression models, hits line is straight when plotted on a graph.


##### Logistic regression

Logistics regression is selected when the dependent variable is categorical, meaning they have binary outputs, such as "true" and "false" or "yes" and "no". While both regression models seek to understand relationships between data inputs, logistic regression is mainly used to solve binary classification problems, such as spam identification.


##### Support vector machines (SVM)

A support vector machine is a popular supervised learning model developed by Vladimir Vapnik, used for both data classification and regressino. That said, it is typically leveraged for classification problems, constructing a hyperplane where the distance between two classes of data points is at its maximum. This hyperplane is known as the decision boundary, separating the classes of data points (e.g., oranges vs. apples) on either side of the plane.

##### K-nearest neighbor

K-nearest neighbor, also known as the KNN algorithm, is a non-parametric algorithm that classifies data points based on their proximity and association to other available data points. This algorithm assumes that similar data points can be found near each other. As a result, it seeks to calculate the distance between data points, usually through Euclidean distance, and then it assigns a category based on the most frequent category or average. Its ease of use and low calculation time make it a preferred algorithm by data scientists, but as the test dataset grows, the processing time lengths, making it less appealing for classification tasks. KNN is typically used for recommemdation engines and image recognition.


##### Random Forest

Random forest is another flexible supervised machine learning algorithm used for both classification and regression purposes. The "forest" refrences a collection of uncorrelated decision trees, which are then merged together to reduce [variance](https://) and create more accurate data predictions.


### Supervised learning examples

Supervised learning models can be used to build and advance a number of business applications, including the following:

- **Image and object recogintion**: Supvervised learing algorithms can be used to located, isolate and categorize objects out of videos or images, making them useful when applied to various computer vision techniques and imagery analysis.

- **Prediction analysis**: A widespread use case for supervised learinig models is in creating predictive analytics systems to provide deep insights into various business data points. This allows enterprises to anticipate certain results based on a given output variable, helping business leaders justify decisions or pivot for the benefit of the organization.

- **Customer sentiment analysis**: Using supervised machine learing algorithms, organizations can extract and classify important pieces of information from large volumes of data--including context, emotion, and intent--with very little human intervention. This can be incredibly useful when gaining a better understanding of customer interactions and can be used to improve brand engagement efforts.

- **Spam detection**: Spam detection is another example of a supervised learning model. Using supervised classification algorithms, organizations can train databases to recognize patterns or anomalies in new data to organize spam and non-sopam-related correspondences effectively.


### Challenges of supervised learning

- Supervised learing models can require certain levels of expertise to structure accurately.
- Training supervised learning models can be very time intensive.
- Datasets can have a higher likelihood of human error, resulting in algorithms learning incorrectly.
- Unlike unsupervised learning models, supervised learning cannot cluster or classify data on its own.


### Algorithms in supervised learning

In this section we are going to see all the algorithm we used in the supervised machine learning. Starting with regresion algorithms, using for prediction.

##### Regression algorithms

Regression algorithm are also known are prediction algorithms because the are used to predict numerical values based on the given dataset.


- [Linear regression](linear-regression.md)
- [Ridge regression](ridge-regression.md)

##### Classifiction algorithms

Classification algorithms are used for classification an object in category. If we have collections of movie, and we want to classify each movie according to it description. We can use classification model for this case.

- [Logistic regression](logistic-regression.md)