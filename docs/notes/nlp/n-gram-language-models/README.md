# N-gram language models

### Language models

**Language models** or **LMs**, models that assign a **probability** to each possible next word. Language models can also assign probability to entire sentence, telloing us that the sequence has a much higher probability of appearing in a text:

```
all of a sudden I notice three guys standing on the sidewalk
```

then does this same set of words in  a different order:

```
on guys all I of notice sidewalk three a sudden standing the
```

##### *Why would we want to predict upcoming words, or know the probabilty of a sentence?* 

One reason is for generation: choosing contextually better words. For example we can correct grammer or spelling erros like **Their are two midterms**, in which **There** was mistyped as **Their**. The phrase **There are** is more probable than **Their are**, so language models can help users select the more grammatical variant. 

Language models can also help in **augmentative and alternative communication** (**AAC**). People can use AAC systesm if they are physically unable to speak or sign but can instead can use eye gaze or other movements to select words from a menu. Word prediction can be used to suggest likely words for the menu.

### Word predictions

Words prediction is also central to NLP for another reason: **large language models** are built just by training them to predict words.

### n-gram

**n-gram**, is the simplest language model.

- An n-gram is a sequence of *n* words: 
- A 2-gram (also called **bigram**) is a two-word sequence of wrods like the **The water**, or **water of**.
- A 3-gram (also called **trigram**) is three-word sequence of wrods like **The water of**, or **water of walden**.

The word 'n-gram' is also used to mean a probabilistic model that can estimate the probability of a word given the n-1 previous words, and thereby also to assign probabilities to entire sentences.

[<<< nlp](../README.md) | [n-gram >>>](n-grams.md)
