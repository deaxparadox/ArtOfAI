# Feature extraction

**Feature extraction** is the process of extracting or creating a new set of features from the original set of features using some functional mapping. New features are created from a combination of original features. Some of the commonly used operators for combining the original features include:

1. For Boolean features: Conjuctions, Disjunctions, Negation, etc.
2. For nominal features: Cartesian product, M of N, etc.
3. For numerical features: Min, Max, Addition, Subtraction, Multiplication, Division, Average, Equivalence, Inequality, etc.


Lets have an example and try to understand. Say, we have a data set with a feature set *F<sub>i</sub> (F<sub>1</sub>, F<sub>2</sub> , F<sub>3</sub>, ..., F<sub>n</sub>)*. After feature extraction using a mapping fucntion *f(F<sub>1</sub>, F<sub>2</sub> , F<sub>3</sub>, ..., F<sub>n</sub>)* say, we will have a set of featues *F'(F'<sub>1</sub>, F'<sub>2</sub> , F'<sub>3</sub>, ..., F'<sub>m</sub>)* such that *F' = f(F<sub>i</sub>)* and *m* < *n*. For example, *F' = k<sub>1</sub>F<sub>1</sub> + k<sub>2</sub>F<sub>2</sub>*.

| Feat<sub>A</sub> | Feat<sub>B</sub> | Feat<sub>C</sub> |  Feat<sub>D</sub>|
|-----|-----|-----|-----|
| 34 | 34.5 | 23 | 233 |
| 44 | 45.56 | 11 | 3.44 |
| 78 | 22.59 | 21 | 4.5 |
| 22 | 65.22 | 11 | 322.3 | 
| 11 | 122.32 | 63 | 23.2 |

can be transformed into:

| Feat<sub>1</sub> | Feat<sub>1</sub> |
|-----|-----|
| 41.25 | 185.80 |
| 54.20 | 53.12 |
| 43.73 | 35.79 |
| 65.30 | 264.10 |
| 37.02 | 238.42 |
| 113.39 | 167.74 |

using the formula:

Feat<sub>1</sub> = (0.3 x Feat<sub>A</sub>) + (0.9 x Feat<sub>A</sub>)
Feat<sub>2</sub> = Feat<sub>A</sub> + (0.5 x Feat<sub>B</sub>) + (0.6 x Feat<sub>C</sub>)


Techniques used for feature extraction:

1. [Principal component analysis](principal-component-analysis.md)
2. [Singular value decomposition](singular-value-decomposition.md)
3. [Linear discriminant analysis](linear-discriminant-analysis.md)