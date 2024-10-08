# Lemmatization

Lemmatization is the task of determinig that twos words have the same root, despite their surface differences. The words *am*, *are*, and *is* have the shared lemma *be*; the words *dinner* and *dinners* both have the lemma *dinner*.

Temmatization usually refers to doing thing properly with the use of vocabulary and morhpological analysis of words normally aimming to remove inflectional ending only and to return the base or dictionary form of word, which is known as the *lemma*. If confronted with thetoken *saw*, lemmatization would attempt to return either *see* or *saw* depending on whether the use of token was as a verb or a noun.

Lemmatization only collapses the  different inflectional forms of a lemma.

### How is lemmatization done?

The most sophisticated methods for lemmatization involve complete **morphological parsing** of the word. **Morphology** is the study of the way words are built up from smaller meaning-bearing units called **morphemes** Two broad class of morphemes can be distinguished; **stems**--the central morpheme of the word, supplying the main meaning--and **affixes**--adding "additional" meanings of various kinds. So, for example, the word *fox* consists of one morpheme (the morpheme *fox*) and the word *cats* consists of two; the morpheme *cat* and the morpheme *-s*. A morphological parser takes word like *cats* and parses it into the two morphemes *cat* and *s*.