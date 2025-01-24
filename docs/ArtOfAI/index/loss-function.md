# Loss Function in Modeling

A **loss function** is a mathematical function that quantifies how far the predicted output of a model is from the acutal (true) vaue. It acts as a guide to help the model improve during traning by adjusting weights and biases.

### Why is a Loss Function important?

- Helps the model learn by providing feedback on erros.
- The lower the loss, the better the models predictions.
Guides the optimization algorithm (like Gradients Descent) to minimize errors.

### Types of Loss Functions

Loss functions vary based on the type of machine learning problem:

#### 1. Regression Loss Functions (Used for continous outputs, e.g., price prediction)

**Mean Squared Error (MSE)**

$$\text{MSE} = \frac{1}{n}\sum\left({y}_{true} - \text{y}_{pred}\right)^2$$

- Penalizes larger errors more than smaller ones.
- Common in linear regression and dep learning models.

**Mean Absolute Error (MAE)**

$$\text{MSE} = \frac{1}{n}\sum\vert\text{y}_{true} - \text{y}_{pred}\vert$$

- Gives equal weight to all erros.
- Less sensitive to outliers than MSE.

**Huber Loss (Combination of MSE and MAE)**

- Used when data has outliers to balance robustness and performance.

#### 2. Classification Loss Functions (Used for categorical outputs, e.g., spam detection)

**Binary Cross-Entropy (Log Loss) - For Binary Classification**