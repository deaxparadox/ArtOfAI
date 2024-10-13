# Objective function

#### Evaluate the quality or optimality of a solution.

----------


### Table of content

- [What is objective function?](#what-is-objective-function)

----------


### What is objective function?

Machine learning is an optimization problem. We try to define a model and tunethe parameters to findt he most suitable solution to a problem. However, we want to have a way to evaluate the quality of optimality of a solution. This is done using **objective function**. Objective means goal.

Objective function takes in data and model (along with parameters) as input and returns a value. Target is to find values of model parameter to maximize the return value. When the objective isto minimize the value, it becomes synonymous to cost function. Examples: maximize the reward function in reinforcement learning, maximize the posterior probability in Naive Bayes, minimize squared error in regression.