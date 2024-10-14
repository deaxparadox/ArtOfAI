# N-grams

### Computer the probability

N-gram is a simplest language models, with sequence of *n* words. Let's calcuate *P(w|h)*,  the probability of a word *w* given some history *h*. 

Suppose the hist *h* is **"The water of Walden Pond is so beautifully"** and we want to know the porbability that the next word is **blue**:

*P*(blue|The water of Walden Pond is so beautifuly)

One way to estimate this probability is directly from relative frequency counts: take a very large corpus, count the nu ber of times we the **The water of of Walden Pond is so beautifully**, and count the number of times this is followed by **blue**. This would be answering the questio "Out of the times we say the history *h*, how many times was it followed by the word *w*, as follows:

![Probability count](/assets/images/n-gram-1.png)

If we had a large enough corpus, we could computer these two counts and estimate the probability from above equation. But event the entire we isn't bit enough to give us good esetimates for cunt of entire sentences. This is because language is **creative** new sentences are invented all the time, we can't expect to get accurate counts for such large objects as entire sentences. For this reason, we'll need more clever ways to entimate the probability of a word *w* given a history *h*, or the probability of an entire word sequence *W*.


----------

##### Notation:

We'll refer **words**, although technically **LMs** uses **tokens**.

To represent the probabilty of a particular random variable *X*<sub>i</sub> taking on the value "the", or *P*(*X*<sub>i</sub> = "the"), we will use the simplication *P*(*the*).

<p>
We'll represent  a sentence of <em>n</em> words either as <em>w<sub>i</sub></em> or <em>W<sub>1:n</sub></em>. Thus the express <em>w<sub>1:n-1</sub></em> means the string <em>w<sub>1</sub></em>, <em>w<sub>2</sub></em>, ..., <em>w<sub>n-1</sub></em>, but we'll also be using the equivalent notion <em>w<sub>&lt;n</sub></em>, which can be read as "all the elements of <em>w</em> from <em>w<sub>1</sub></em> up to and including <em>w<sub>n-1</sub></em>".
</p>

<p>
For the joint probability of each word in a sequence having a particular value <em>P(X<sub>1</sub> = w<sub>1</sub>, X<sub>2</sub> = w<sub>2</sub>, ..., X<sub>n</sub> = w<sub>n</sub>)</em>, we'll use <em>P(w<sub>1</sub>, w<sub>2</sub>, ..., w<sub>n</sub>)</em>.
</p>

----------

<p>
To computer the probabilities of entire sequences like <em>P(w<sub>1</sub>, w<sub>2</sub>, ..., w<sub>n</sub></em>?
</p>

<p>
One thing 
</p>