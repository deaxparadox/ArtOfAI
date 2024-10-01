# Text Normalization

Text normalization is the process of transforming text data into a standardized or  canonical form. It involves converting text data into a consistent format by applying various techniques. Text normalization is an importantt step in natural language processing (NKP) tasks such as text classification, sentiment analysis, and information extraction. It purpose it to convert text data into a consistent format through the application of various techniques, thereby enhancing the accuracy and effectiveness of these NLP tasks.

### Normalization techniques:

1. [Stemming](#stemming)
2. [Lemmatization](#lemmatization)

These techniques are used to reduce infectional forms and sometimes derivationally related forms ofwords to a common base form.

```
sentence = “It would be unfair to demand that people cease pirating files when those same people aren't paid for their participation in very lucrative network schemes. Ordinary people are relentlessly spied on, and not compensated for information taken from them. While I'd like to see everyone eventually pay for music and the like, I'd not ask for it until there's reciprocity.”

```

### Expanding Contractions

In *sentence*, we have the words "we will" contracted as "we'll", which should be managed before normalization.

**Contractions** are words or combinations for words that are shortened by droppings letters and replacing them by an apostrophe, and removing them contributes to the text standardization.

We can create a dicitionary of contractions, which hold contracted words as key and value as expanded words.

```
contractions_dict = { “ain’t”: are not”, ”’s”:” is”, ”aren’t”: “are not”, “can’t”: “cannot”, ”can’t’ve”: “cannot have”, “‘cause”: “because”, ”could’ve”: “could have”, ”couldn’t”: “could not”, “couldn’t’ve”: “could not have”, “didn’t”: “did not”, ”doesn’t”: “does not”, “don’t”: “do not”, ”hadn’t”: “had not”, ”hadn’t’ve”: “had not have”, “hasn’t”: “has not”, ”haven’t”: “have not”, ”he’d”: “he would”, “he’d’ve”: “he would have”, ”he’ll”: “he will”, “he’ll’ve”: “he will have”, “how’d”: “how did”, ”how’d’y”: “how do you”, ”how’ll”: “how will”, “I’d”: “I would”, “I’d’ve”: “I would have”, ”I’ll”: “I will”, “I’ll’ve”: “I will have”, ”I’m”: “I am”, ”I’ve”: “I have”, “isn’t”: “is not”, “it’d”: “it would”, ”it’d’ve”: “it would have”, ”it’ll”: “it will”, “it’ll’ve”: “it will have”, “let’s”: “let us”, ”ma’am”: “madam”, “mayn’t”: “may not”, ”might’ve”: “might have”, ”mightn’t”: “might not”, “mightn’t’ve”: “might not have”, ”must’ve”: “must have”, ”mustn’t”: “must not”, “mustn’t’ve”: “must not have”, “needn’t”: “need not”, “needn’t’ve”: “need not have”, ”o’clock”: “of the clock”, ”oughtn’t”: “ought not”, “oughtn’t’ve”: “ought not have”, ”shan’t”: “shall not”, ”sha’n’t”: “shall not”, “shan’t’ve”: “shall not have”, ”she’d”: “she would”, ”she’d’ve”: “she would have”, “she’ll”: “she will”, “she’ll’ve”: “she will have”, ”should’ve”: “should have”, “shouldn’t”: “should not”, “shouldn’t’ve”: “should not have”, ”so’ve”: “so have”, “that’d”: “that would”, ”that’d’ve”: “that would have”, “there’d”: “there would”, “there’d’ve”: “there would have”, “they’d”: “they would”, “they’d’ve”: “they would have”,”they’ll”: “they will”, “they’ll’ve”: “they will have”, “they’re”: “they are”, ”they’ve”: “they have”, “to’ve”: “to have”, ”wasn’t”: “was not”, ”we’d”: “we would”, “we’d’ve”: “we would have”, ”we’ll”: “we will”, ”we’ll’ve”: “we will have”, “we’re”: “we are”, ”we’ve”: “we have”, “weren’t”: “were not”,”what’ll”: “what will”, “what’ll’ve”: “what will have”, ”what’re”: “what are”, “what’ve”: “what have”, “when’ve”: “when have”, ”where’d”: “where did”, “where’ve”: “where have”, “who’ll”: “who will”, ”who’ll’ve”: “who will have”, ”who’ve”: “who have”, “why’ve”: “why have”, ”will’ve”: “will have”, ”won’t”: “will not”, “won’t’ve”: “will not have”, “would’ve”: “would have”, ”wouldn’t”: “would not”, “wouldn’t’ve”: “would not have”, ”y’all”: “you all”, “y’all’d”: “you all would”, “y’all’d’ve”: “you all would have”, ”y’all’re”: “you all are”, “y’all’ve”: “you all have”, “you’d”: “you would”, ”you’d’ve”: “you would have”, “you’ll”: “you will”, ”you’ll’ve”: “you will have”, “you’re”: “you are”, “you’ve”: “you have”}
```


Then, we can use regular expression expand the sentence.

### Tokenize

Tokenization is the process of segmenting running text into sentences and words. It essence, it's the task of cutting a text into pieces called *tokens*.

### Removing Punctuation

From the tokeinzed sentence, we have to remove punctuation.

### Stemming

Stemming is the process of reducing the words to their word stem or root form. The objective of stemming is to reduce related words to the same stem even if the stem is not a dictionary word. For example, connection, connection, connecting word reduce to a common word "connect".

**Stemming a word or sentence may result in words that are not acutal words**. Because, stemming referes to a crude heuristic process that chops off theends of words i nthe hope of achieving this goal correctly most of the time.

This happends because there are two mainly errors in stemming:

- **Over-stemming**: Where a much large part of words is chopped of then what is requried, which in turn leads to words being reduced to the same root word or stem incorrectly when they should have been reduced to more stem words. For example, the words "university" and "universe" that get reduced to "univers".

- **Under-stemming**: Occurs when two or more words could be wrongly reduced to more than one root word when they acutally should be reduced to the same root word. For example, the words "data" and "datum" that get  reduced to "dat" and "datu" respectively (instead of the same stem "dat").

The most common algorithm for stemming English, and one that has repeatedly been shown to be mpirically every effective, is **Porter's algorithm**.


**Snowball Stemmer** is an improvement to the Poter Stemmer, which stems words to a more accurate stem.

### Lemmatization

**Lemmatization reduces words to their base words**, reducing the inflected words properly and ensuring that the root word belongs to the language. It's usually more sophisticated than stemming, since stemmers words on an individual word  without knowledge of the context.

In lemmatization, a root word is called **Lemma**. A lemma is the canonical form, dictionary form, or citation form of a set of words.

- **WordNet** Lemmatizer.

To improve performance of lemmatization, by providing the context in which you want ot lemmatize,w hich you can do through **parts-of-speech (POS)** tagging.

### POS tagging

**Part-of-speech** (POS) tagging is the task of assigning each word in a sentence the part of speech that it assumes in that sentence. The primary target of POS sentence is to identify the grammatical group of given word: Whether it is a noun, pronoun, adjective, verb, adverbs, etc. based on the context.

You can use POS as a speech parameter, which in Python is **noun by default**. For example, the word '*leaves*' without a POS tag would get lemmatized to the word '*leaf*', but with a *verb* tag, its lemma would become '*leave*'.