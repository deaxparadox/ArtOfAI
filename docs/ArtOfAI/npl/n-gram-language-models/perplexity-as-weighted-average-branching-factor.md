# Perplexity as Weighted Average Branching Factor

Perplexity can also be though of as the **weighted average branching factor** of a language. The branching factor of a language is the number of possible next words that can follow any words. For example consider a mini artificial language that is deterministic (no probabilities), any word can follow any word, and whose vocabulary consists of only three colors:

$$L = \{red, blue, green\}$$

The branching factor of this  language is 3.

Let's make a probabilistic version of the same LM, let's call it $A$, where each word follows each other with equal probability $\frac{1}{3}$ (it was trained on the training set with equal counts for the 3 colors), and a test set $T = "red\;red \;red \;red\;blue"$.