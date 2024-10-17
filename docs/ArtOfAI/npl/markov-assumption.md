
# Markov assumption

### Using bigram

Lets recall the **bigram** model for the understanding of Markov chain. In bigram model, we approximates the probability of a word given all the previous words *P(w <sub>n</sub> | w <sub>1:n-1</sub>)* by using only the conditional probability of the preceeding words *P(w <sub>n</sub> | w <sub>n-1</sub>)*. In other words, instead of computing the probability

*P(blue|The water of Walden Pong is so beautifully)*

we approximate it with the probability

*P(blue|beautifully)*.

When we use a bigram model to predict the conditonal probability of the next word, we are thus making the following approximation:

*P(w <sub>n</sub> | w <sub>1:n-1</sub>)* ≈ *P(w <sub>n</sub> | w <sub>n-1</sub>)* 

The assumption that the probability of a word depends only on the previous word in called a **Markov assumption**.