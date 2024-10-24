# The markov assumption

The intuition of the n-gram models is that instead of commputing the probability of a word given its entire history, we can **approximate** the history by just the last few words.

### bigram

The **bigram** models, for example approximates the probability of a word given all the previous words *P(w<sub>n</sub>|w <sub>1:n-1</sub>)* by using only the coditional probability of the preceding word *P(w<sub>n</sub>|w<sub>n-1</sub>)*. In other words, instead of computing the probability

*P(blue|The water of Walden Pong is so beautifully)*

we approximate it with the probability

*P(blue|beautifully)*.

### Markov assumption

*Read [bigram](#bigram) above this*.

When we use a bigram model to predict the conditonal probability of the next word, we are thus making the following approximation:

*P(w <sub>n</sub> | w <sub>1:n-1</sub>)* ≈ *P(w <sub>n</sub> | w <sub>n-1</sub>)* 

The assumption that the probability of a word depends only on the previous word in called a **Markov assumption.


Markov models are the class of probabilistic models that assume we can predict the probability of some future unit without looking to far into the past. We can generalize the bigram (which looks one word into the past) to the trigram (which looks two wrods into the past) and thus to the **n-gram** (which looks n-1 words into the past).

Let's see a general equation for this n-gram approximation to the conditional probability of the next word in a sequence. We'll use *N* here to mean the n-gram size, so *N* = 2 means bigrams and *N* = 3 means trigrams. Then we approximate the probability of a word given its entire context as follows:

*P(w<sub>n</sub>|w<sub>1:n-1</sub>)* ≈ *P(w<sub>n</sub>|w<sub>n-N+1:n-1</sub>)*

Given the bigram assumption for the probability of an individual word, we can compute the probabilty of a complete word sequence by substituting the follwing 

*P(w <sub>n</sub> | w <sub>1:n-1</sub>)* ≈ *P(w <sub>n</sub> | w <sub>n-1</sub>)* 

into

![Image not found](/assets/images/n-gram-3.png)

gives:

![Image not found](/assets/images/n-gram-4.png)

[<<< N-grams](n-grams.md) | [How to estimate probabilities >>>](how-to-estimate-probabilities.md)