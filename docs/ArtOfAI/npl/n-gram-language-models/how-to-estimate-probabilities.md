# How to estimate probabities

*How to we estimate these b-gram or n-gram probabilties?*

An inituitive way to estimate probabilities is called **maximum likelihood estimation** or **MLE**. We get he MLE estimate for the parameters of an n-gram model by getting counts from a corpus, and **normalizing** the counts so that they lie between 0 and 1. For probablitistic models, normaling means dividing by some total count so that the resulting probabilistics fall between 0 and 1 and sum to 1.

For example, to compute a particular bigram proability of a word *w <sub>n</sub>* given a previous word *w <sub>n-1</sub>*, we'll compute the count of the bigram *C(w<sub>n-1</sub>w<sub>n</sub>)* normalize by the sum of all the bigrams that share the same first word *w<sub>n-1</sub>*:

![Image not found](/assets/images/n-gram-5.png)

We can simplify this equation, since the sum of all bigram counts that start with a given word *w<sub>n-1</sub>* must be equal to the unigram count for that word *w<sub>n-1</sub>*:

![Image not found](/assets/images/n-gram-6.png)

Let's work through an example using a mini-corpus of three sentences. We'll first need to augment each sentence with a special symbol &lt;s&gt; at the begining of the sentence, to give us the bigram context of the first word. We'll also need a special end-symbol &lt;/s&gt;

```
<s> I am Sam </s>
<s> Sam I am </s>
<s> I do not like green eggs and ham </s>
```

Here are the calculations for some of the bigram probabilities from this corpus:


*P*(I|&lt;s&gt;) = 2/3 = 0.67

*P*(Sam|&lt;s&gt;) = 1/3 = 0.33

*P*(am|I) = 2/3 = 0.67

*P*(&lt;/s&gt;|Sam) = 1/2 = 0.50

*P*(Sam|am) = 1/2 = 0.50

*P*(do|I) = 1/3 = 0.33

For the general case of MLE n-gram parameter estimation:

![Image not found](/assets/images/n-gram-7.png)

The above equation estimates the n-gram probabilty by dividing the observed frequency of a particular sequences by the observed frequency of a prefix. This ration is called **relative frequency**.

In MLE, the resulting parameter set maximizes the likehood of the training set *T* given the model *M*(i.e., *P(T|M)*). For example, supposethe word *Chinese* occurs 400 times in a corpus of a million words. What is the probability that a random word selected from some tother text of, say a million words will be the word *Chinese*? The MLE os its probability is 400/1000000 or 0.0004. Now 0.0004 is not the best possible estimate of the probablity of *Chinese* occuring in all situations; it might turns out that in some other corpus or context *Chinese* is a very likely word. But it is the probability that makes it *most like* that Chinese will occur 400 times in a million-word corpus.

[⏮️ The markov assumption](the-markov-assumption.md) | [⏸️ N-gram models](README.md) | [Dealing with scale in large n-gram models ⏭️](dealing-with-scale-in-large-n-gram-models.md)