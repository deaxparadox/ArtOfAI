# Dealing with scale in large n-gram models

### Log probabilities

Language models probabilities are always stored and computed on log space as **log probabilities**. This is because probabilities are (by definition) less than or equal to 1, and so the more probabitlies we multiply together, the smaller the product becomes. Mulitplying enough n-grams together would result in numerical underflow. Adding in log space is equivalent to mulitipying in linear space, so we combine log probabilities by adding them. By addint log probabitlies instead of multiplying probabilities, we get results that are not as small. We do all computation and storage in log space, and just convert back into probabilities if we need to report probablities at the end by taking the exp of the logprob:

$$p_1 \times p_2 \times p_3 \times p_4 = \exp_{}(\log{p_1} + \log{p_2} + \log{p_3} + \log{p_4})$$

### Longer context

When there is sufficient training data we use **trigram** moels, which condition on the previous two words, or **4-grams** or **5-grams** models. For these large n-grams, we'll need to assume extra contexts to the left and right of the sentence end. For example, to compute trigram probabitlies at the very begining of the sentence, we use two pseudo-words for the first trigram (i.e., $P \left(I | \lt{s}\gt \lt{s}\gt \right)$).

It's even possible to use extremely long-range n-gram context. The infini-gram ($\infty$-gram) project allows n-gram of any length. Their idea is to avoid the expensive (in space and time) pre-computation of huge n-gram count tables. Instead, n-gram probabilities with arbitrary n are computed quickly at ingerence time by using an efficient representtaion called suffix arrays. This allows computing of 5 trillion tokens.


Efficiency considerations are important when building large n-gram language models. It is standard to quantize the probabilities using 4-8 bits (instead of 8-bytes floats), store the word strings on disk and represent them in memory only as a 64-bit hash, and represents n-grams in special data structures like "reverse tries". It is also common to prune n-gram language models, for example by only keeping n-grams with counts greater than some thresold or using entropy to prune less important n-grams.

[⏮️ How to estimate probabilities](how-to-estimate-probabilities.md) | [⏸️ N-gram models](README.md) |
 [Evaluating language models ⏭️](evaluating-language-models.md)