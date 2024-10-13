# Ridge regression

Ridge regression algorithm is one of the linear model algorithm, it uses the same concept as [linear regression](linear-regression.md), with a little tweak. It imposes a penalty on the size of the coefficients. The ridge coefficients minimize a penalized residual sum of squares.

![Ridge regression](/assets/images/ridge-regression-1.png)

The complexity parameters *α* ≥ 0 controls the amount of shrinkage; thelarge the value of *α*, the greater the amount of shrinkage and thus the coefficients become more robust to collinearity.

```py
>>> reg = linear_model.Ridge(alpha=.5)  
>>> reg.fit([[0, 0], [0, 0], [1, 1]], [0, .1, 1])
Ridge(alpha=0.5)
>>> reg.coef_
array([0.34545455, 0.34545455])
>>> reg.intercept_
0.13636363636363638
>>>
```