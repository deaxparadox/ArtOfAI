# Supervised Learning

### Table of content

- [What is Supervised learning](#what-is-supervised-learning)
- [How supervised learning works](#how-supervised-learning-works)
- [Supervised learning algorithm](#supervised-learning-algorithms)
    - [Neural networks](#neural-networks)

### What is Supervised learning

Supervised leraning, also known as supervised machine liearning, is a subcategory of machine learning and artificial intelligence. It is defined by its use of labeled data sets to train algorithms that to classify data or predict outcomes accurately.

As input data is fed into the model, it adjusts it weights until the model has been fitted appropriately, hwihc occurs as part of the cross validation process. 

Supervised learning helps organization solve for a variety of real-world problems at scale, such as classifying spam in a seprate folder from your inbox. It can be used to build highly accurate machine learning models.

### How supervised learning works

Supervised learning uses a training set to teach models to yield the disired output. This training dataset include inputs and correct ouputs, which allow the model to learn over time. The algorithm measures it accuracy through [loss function](https://) adjusting until the error has been sufficiently minimized.

Supervised leraning can be separated into two types of problems when [data mining](https://) -- classification and regression:

1. Classification

Uses an algirhtmto accurately assign test data into specific categories. it recognizes specific entities within the dataset and attempts to draw some conclusion on how those entities should be labeled or defined.

Common classification algorithms:

- [Linear classifiers](https://)
- [Support vector machines](https://) (SVM)
- [Decision trees](https://)
- [K-nearest neighbor](https://)
- [Random forest](https://)

2. Regression

It is used to understand the relationship between dependent and independent variables. It is commonly used to make projections, such as for sales revenue for a given business.

Common regression algorithms:

- [Linear regression](https://)
- [Logistical regression](https://)
- [Polynomial regression](https://)

### Supervised learning algorithms

Commonly used supervised learing algorithms:

##### Neural Networks

Primary leveraged for deep learing algorithms, [neural networks](https://) process training data by mimicking the interconnectivity of the human brain layers of nodes. Each node is made up of inputs, weights, a bias (or thresold), and an output. If that output values exceeds a given thresold, it "fires" or activates the node, passing data to the next layer in the network. Neural networks learn this mapping function through supervised learning, adjusting based on the loss function through the process of [gradient descent](https://). When the [cost function](https://) is at or the near zero, we can be confident in the model's accuracy to yield the correct answer.


