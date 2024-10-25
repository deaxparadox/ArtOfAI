# Evaluating language models: Training and Test sets

### Extrinsic evaluation

The best way to evaluate the performance of language models is to embed it in an application and measure how much the application improves. Such end-to-end evaluation is called **Extrinsic evaluation**. Extrinsic evaluation is the only way to know to know if a particular improvement in the language model (or any component) is really going to help that task at hand.

For evaluating n-gram language models that are a component of some task like speech recognition or machine translation, we can compare the performance of the two candidate language models by running the speech recognition or machine translation, we can compare the performance of two candidate language models by running the speech recognizer or machine translator twice, once with each language model, and see which one gives the more accurate transcription.

**Running big NLP systems end-to-end is often very expensive**.

### Intrinsic evaluation

An **intrinsive evaluation** an metric which measures the quality of a model independent of any application. For example: **perplexity**, which is the standard intrinsic metrix for measuring language models performance, both for simple n-gram language models and for the more sophisticated neural large language models.


### Data set

In order to evaluate any machine learning models, we need to have atleast three distinct data sets; the **training set**, the **development set** and the **test set**.

##### Training set

The training set the data we use to lean the parameters of our model: for simple n-gram language models it's the corpus from which we get the counts that we normalize into the probabilities of the n-gram language model.

##### Test set

The test set is a different, hold out set of data, not overlapping the training set, that we use to evaluate the model. 

A machine learning models that perfectly captured the training data, but performed terribly on the  any other data, wouldn't be much use when it comes time to apply it to any new data or problem!

##### Development test
