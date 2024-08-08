# Bias Variance Trade Off

In supervised learning, the class value assigned by the learning model built based on the training data may differ from the acutal class value. This error in learning can be of two types--errors due to 'bias' and error due to 'variance'.


### Errors due to 'Bias'

It is due to underfitting of the model.

Parameteric models generally have high bias making them easier to understand/interpret and faster to learn. These algorithms have poor performance on datasets, which are complex in nature and do not align with the  simplifying assumptions made by the algorithm. Underfitting results in high bias.


### Errors due to 'Variance'

Erros due to variance occur from difference in training data sets used to train the model. Different training data sets are used to train the model.



----------

- Increaing the bias will decrease the variance, and
- Increasing the variance will decrease the bias

----------

- Parametric algorithms are generally seem to demonstrate high bias but low variance.
- Non-parametric algorithms demonstrate low bias and high variance.