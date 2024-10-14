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