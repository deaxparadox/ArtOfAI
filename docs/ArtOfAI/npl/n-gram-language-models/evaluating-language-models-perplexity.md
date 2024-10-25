
### Perplexity

Perplexity is a funciton of probability. It is one of the most important metrics in NLP, used for evaluating large language models as well as n-gram models. The perplexity (sometimes abbreviated as PP or PPL) or a language model on a test set is the inverse probability of the test set (one over the probability of the test set), normalized by the number of words (or tokens). For this reason it's sometimes called the per-word or per-token perplexity. We normalize by the number of words N by taking the Nth root. For a test set $W = w_1 w_2 ... w_N$:

$$ Perplexity \left(W\right) = P\left(w_1 w_2 ... w_N\right) ^{-\frac{1}{N}}$$
$$ = \sqrt[N]{\frac{1}{P\left(w_1 w_2 ... w_N\right)}}$$

Or we can use the chain rule to expand the probability of $W$:

$$perplexity\left(W\right) = \sqrt[N]{\prod_{i=1}^N\frac{1}{P\left(w_i|w_1 ... w_{i-1}\right)}}$$
###### Eq 3.15

By looking at above equation, we can say,

- The higher the probablity of the word sequence, the lower the perplexity.
- Thus the the lower the perplexity of a model on the data, the better the model.

----------

The details of computing the perplexity of a test set $W$ depends on which language model we use. Here's the perplexity of $W$  with a unigram language model (just the geometric mean of the inverse of the unigram probabilities):

$$perplexity\left(W\right) = \sqrt[N]{\prod_{i=1}^N\frac{1}{P\left(w_i\right)}}$$

The perplexity of $W$ computed with a bigram language model is still a geometric mean, but now of the inverse of the bigram probablities:

$$perplexity\left(W\right) = \sqrt[N]{\prod_{i=1}^N\frac{1}{P\left(w_i|w_{i-1}\right)}}$$


----------


Let's first convince ourselves that it we compute the perplexity of this artificial digit language on this testt set (or any such test set) we inded get 3. By using equation [3.15](#eq-315), the perpelxity of $A$ on $T$ is:

$$perplexity_A\left(T\right) = P_A\left(red\;red\;red\;red\;blue\right)^{{-}{\frac{1}{5}}}$$
$$=\;\left(\left(\frac{1}{3}\right)^5\right)^{{-}{\frac{1}{5}}}$$
$$=\;\left(\frac{1}{3}\right)^{-1} = 3$$

###### Eq 3.19

But nor suppose $red$ was very likely in the training set a different LM $B$, and so $B$ has the following probabilities:

$$P\left(red\right) = 0.8{\qquad}P\left(green\right) = 0.1{\qquad}P\left(blue\right) = 0.1$$

###### Eq 3.20

We should expect the  perplexity of the same test set $red\;red\;red\;red\;blue$ for language model $B$ to be lower since most of the time the next color well be red, which is revery predictable, i.e. has a high probability. So the probability of the test set will be higher, and since perplexity is inversely related to probablity, the perplexity will be lower. Thus, although the branching factor is still 3, the perplexity or *weighted** branching factor is smaller:

$$perplexity_B\left(T\right) = P_B\left(red\;red\;red\;red\;blue\right)^{{-}{\frac{1}{5}}}$$
$$ = 0.04096^{{-}{\frac{1}{5}}}$$
$$ = 0.527^{-1} = 1.89$$