# Brief of probability

### Table of content

- [Introduction](#introduction)
- [Importance of statistical tools in machine learning](#importance-of-statistical-tools-in-machine-learning)
- [Concept of probability - frequentist and bayesian interpretation](#concept-of-probability---frequentist-and-bayesian-interpretation)

----------


### Introduction

ML provides us a set of methods that can automatically detect patterns in data, and then can be used to uncover patterns to predict future data, or to perform other kinds of decision making under uncertainty. The best way to perform such activites on top of huge dataset known as **big data** is to use the tools of probability theory because probability theory can be applied to any situation involving uncertainty.

In machine learning there may be uncertainties in differrent forms like arriving at the best prediction of future given the past data, arriving at the best model based on certain data, arriving at the confidence level while predicting the future outcome based on past data, etc.

### Importance of statistical tools in machine learning

In machine learning, we train the system by using a limited data set called "training data" and based on the confidence level of the training data we expect the machine learning algorithm to depict the behaviour of the larger set of acutal data. If we have observation on a subset of events, called 'sample', then t here will be some uncertainty in attributing the sample results to the whole set or population. So, the question was how a limited knowledge of a sample set can be used to predict the behaviour of a real set with some confidence. It was realized by mathematicians that even if some knowledge is based on  sample, if we know the amount of uncertainty related to it, then ti can be used in an optimum way without causing loss of knowledge.

![alt](/assets/images/probability-1.png)

Probability theory provides a mathematical foundation for quantifying this uncertainty of the knowledge. As the knowledge about the training data comes in the form of **interdependent** feature sets, the conditional probability theories, form the basis for deriving required confidence level of the training data.

Different distribution principles create the view of how data set that we deal with in mahcine can behave, in terms of their features destributions. It is important to understand the mathematical function behind each of these distributions so that we can understand how the data is spread out from its average value--denoted by the mean and the variance. While choosing the samples from these distribution sets we should be able to calculate to what wextent the sample is representing the acutal behaviour of the full dataset. These along with the test of hypothesis principles build  the basis for finding out the uncertainty in the training dataset to represetn the acutal data set which is the fundamental principles of ML.


### Concept of probability - frequentist and bayesian interpretation

Example, while tossing a coin we talk about probability of gettings the heads and the tails when a coint is flipped are equal, we acutally intend to say that if a coint is flipped many times, the coint will land heads a same number of times as it lands tails. This is the **frequentist** interpretation of probability. This interpretation represents the long run frequencies of events. Another inmportant interpretaion of probabilty tries to quantify the uncertainty of some vent and thus focuses on informatino rather than repeated trails. This is called the **Bayesian** interpretation of probablity. Taking the same example of coin flipping is interpreted as -- the coint is equally like to land heads or tails when we flip the coint next.

The reason the Bayesian interpretaion can be used to model the uncertainty of events is that it does not expect the long run frequencies of the events to happen. For example, if we have to compute the porbability of Brazil winning 2018 football world cup final, that event can happend only once and can't be repeated over and over again to calculate its probablity. But sill, we should be able to quantify the uncertainty about the event and which is noly possible if we interpret probabilty the Bayesian way. Another example, we are starting a new software implementation probject for a large customer and want to compute the probablity of this project getting into customer escalation based on data from similar projects in the past, or we want to compute the probablity of a tumor to be maliganat or not based on the probabilty distribtion of such cases among the patients of similar profile. In all these cases it is not possible to do a repeated trail of the event and the Bayesian concept is valid for computing the uncertainty.

[<<< Features subset approaches](https://) | [Brief review of probablity theory >>>](brief-review-of-probability-theory.md)