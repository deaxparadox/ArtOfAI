# Feature subset selection


Also called **Feature selection**, is this case no new feature is generated. The object of feature selection is to derive a subset of features from the full feature set which is most meaningful in the context of a specific machine learning problem. So, essentially the job of feature selection is to derive a subset *F<sub>j</sub>(F<sub>1</sub>, F<sub>2</sub>, ..., F<sub>m</sub>) of F<sub>i</sub>(F<sub>1</sub>, F<sub>2</sub>, ..., F<sub>n</sub>)*, where  *m* < *n*, such that F<sub>j</sub> is more meaningful and gets the best result for a machine learning problem.


Feature selection is arguably the most critical pre-processing activity in any machin learing project. It intends to select a subset of system attributes or features which makes a most meaningfull contribution in a machine learing activity.


### Issues in high-dimensional data

The text data generated from different sources have exteremly high dimensions (or consider any with thousands of features). In a large document corpus having few thousand documents embedded, the number of unique word tokens which represent the feature of the text data set, can also be in the range of a few tens of thousands. To get insight from such high-dimensional data may be a big challenge for a machine learning algorithm.