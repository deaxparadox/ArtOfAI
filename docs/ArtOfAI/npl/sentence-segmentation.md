# Sentence segmentation

Sentence segmentation is part of text pre-processing. The most important cues for segmenting a text into sentences are punctuation, like periods, question marks exclamation points.

Question marks and exclamation points are relatively unambiguous markers of sentences boundaries. Periods, on the other hand, are more ambigous. The period characters "." is ambiguous between a sentence boundary marker and a marker of abbreviations like *Mr.* or *Inc*. The previous sentence, shows even more complex case of this ambiguity, in which th final period of *Inc.* marked both an abbreviation and and the sentence boundary marker. For this reason, sentence tokenization and word tokenization may be adresses jointly.


### Sentence tokenization

Sentence tokenization works by first deciding (based on rules or machine learning) whether a period is part of the word or is a sentence-boundary marker. An abbreviation dictionary can help you determine whether the period is part of a commonly used abbreviation; the dictionaries can be hand-built or machine learned, as can the final sentence splitter.