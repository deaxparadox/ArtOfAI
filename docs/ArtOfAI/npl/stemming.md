# Stemming

The naive version of morphological analysis is called **stemming**.

Stemming usualling refers to a crud heuristic process that chops of the end of words in the hope of achieving the goal correctly most of the time, and often include the removal of derivational affixes. If confrontend with the token *saw*, stemming might just return *s*. 

Stemming most commonly collapses derivationally related words.

### PortStemmer

PortStemmer is the most common algorithm

[Code](/code/ipynb/portstemmer.ipynb)