# Feature transformation

Engineering a good feature space is crucial prerequisite for the success of any machine learning model. Feature transformation is used as an effective tool for dimensionality reduction and hence for boosting learning model performance. Broadly, there are two distinct goals of feature transformation:

- Achieving best construction of the original featuers in the dataset.
- Achieving highest effciency in the learning task.


Feature transformation transforms the data -- structure or unstructured, into a new set of features which can represent the underlying problem which machine learning is trying to solve.

There are two variants of feature transformation:

1. Feature construction
2. Feature extraction
 

Both are sometimes known as **feature discovery**.

### Feature construction

**Feature contruction** process discovers missing information about the relationships between features and augments the feature space by creating additional features. Hence, if there are *'n'* features or dimensions in a data set, after feature construction *'m'* more features or dimensions may get added. So at the end, the data set will become *'n + m'* dimensional.

Feature construction involves transformaing a given set of input features to generate a new set of more powerful featuers. 

Lets take a example to understand feature transformation, suppose a data set has three features -- apartment length, apartment breadth, and price of the apartment. If it is  used as an input to a regression problem, such data can be training for the regression model. So given the training data, the model should be able to predict the price of an apartment whose price is not known or which has just come up for sale.  However, instead of using length and breadth of the apartment as a predictor, it is much more convenient and makes more sense to use the area of the apartment, which is not an existing feature of the data set. So such a feature, namely apartment area, can be added to the dataset. In other words, we transform the three-dimensional data set to a four-dimensional data set, with the newly 'discovered' feature apartment area being added to the original data set.

There are certain situations where feature constuction is an essential activity before we can start with the machine learning task. These situations are

- when features have categorical value and machine learning needs numeric value inputs.
- when features having numeric (continuous) values and need to be converted to ordinal values.
- when text-specific feature construction needs to be done.

### Encoding categorical (nominal variables)

**Nominal: the data can only be categorized.**

Lets understand it with an example. We have a dataset on atheletes, say the data set have feature "age", "City of origin", and "Parent athelete" (i.e. indicate whether any one of the parents was an athelete), and *Chain of win*. The feature "Chance of win" is an class variable while the others are predictor variables.

| Age (Years) | City of origin | Parents athelete | Chance of win |
|-------------|----------------|------------------|---------------|
| 18 | City A | Yes | Y |
| 20 | City B | No | Y |
| 23 | City B | Yes | Y |
| 19 | City A | No | N | 
| 18 | City C | Yes | N |
| 22 | City B | Yes | Y |


We know any machine learning algorithm, requires numerical figures to learn from. So, the three features "City of origin", "Parent athelete" and "Change of win", which are categorical in nature and cannot be used by any machine learning task.

----------


In this case, feature construction can be used to create new dummy features which are usable by machine learning algorithms. Since the feature "City of origin" has three unique values namely "City A", "City B", "City C", three features namely "origin_city_A", "origin_city_B", and "origin_city_C" is created. In the same way, dummy features "parents_athelete_Y",  and "parents_athelete_N" are created for features "Parents athelete", and "win_chance_Y" and "win_chance_N" are created for feature "Chance of win". 

| Age (Years) | origin_city_A | origin_city_B | origin_city_C | parents_athelete_Y | parents_athelete_N | win_chance_Y | win_chance_N |
|-----|-----|------|-----|-----|-----|-----|-----|
| 18 | 1 | 0 | 0 | 1 | 0 | 1 | 0 |
| 20 | 0 | 1 | 0 | 0 | 1 | 1 | 0 |
| 23 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| 19 | 1 | 0 | 0 | 0 | 1 | 0 | 1 |
| 18 | 0 | 0 | 1 | 1 | 0 | 0 | 1 |
| 22 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |

The dummy features have value 0 or 1 based on the categorical value for the original feature in that row. For example, the second row had a categorical value "City B" for the featue "City of origin". So, the newly created features in place of "City of origin", i.e. "origin_city_A", "origin_city_B", and "origin_city_C" will have values 0, 1, and O respectively. In the same way, "parent_athelete_Y" and "parent_athelete_N" will have values 0 and 1, respectively.

----------


However, examinig closely, we see the featues "Parent_atheletes" and "Chance of win" in the original data set can have two values only. So createing two features from them is kind of duplication, since the value of one feature can be decided from the valeu of the other. To avoid this duplication, we can just leave one feature and eliminate the other.

| Age (Years) | origin_city_A | origin_city_B | origin_city_C | parents_athelete_Y | win_chance_Y |
|------|-----|-----|-----|-----|-----|
| 18 | 1 | 0 | 0 | 1 | 1 |
| 20 | 0 | 1 | 0 | 0 | 1 |
| 23 | 0 | 1 | 0 | 1 | 1 |
| 19 | 1 | 0 | 0 | 0 | 0 |
| 18 | 0 | 0 | 1 | 1 | 0 |
| 22 | 0 | 1 | 0 | 1 | 1 |


### Encoding categorical (ordinal) variables

**Ordinal: the data can be categorized and ranked**.

Let's take an example of student data set. Let's assume that there are three variables "science marks", "maths marks" and "grade".

| marks_science | marks_maths | grade |
|-----|-----|-----|
| 78 | 75 | B |
| 56 | 62 | C |
| 87 | 90 | A |
| 91 | 95 | A |
| 45 | 42 | D |
| 62 | 57 | B |

The "grade" is an ordinal variable with values A, B, C and D. To transform this variable to a numeric variable, we can create a feature *num_grade* mapping a numeric value against each ordinal value. In the context of the current example, grades A, B, C, and D is mapped to values 1, 2, 3, and 4 in the transformed variable.

| marks_science | marks_maths | num_grade |
|-----|-----|-----|
| 78 | 75 | 2 |
| 56 | 62 | 3 |
| 87 | 90 | 1 |
| 91 | 95 | 1 |
| 45 | 42 | 4 |
| 62 | 57 | 2 |


### Transforming numeric (continous) features to categorical features

Sometimes there is a need of transforming a continuous numerical variable into a categorical variable. For example, we may want to treat the real estate price predition problem which is regression problem, as a real estate price category prediction, which is a classficiation problem. In that case, we can "bin" the numerical data into multiple categories based on the data range. In the context of the rela estate price prediction example, the original data set has a numerical feature "apartment_price":

| apartment_area | apartment_price |
|-----|-----|
| 4,720 | 23,60,000 |
| 2,430 | 12,15,000 |
| 4,368 | 21,84,000 |
| 3,969 | 19,84,500 |
| 6,142 | 30,71,000 |
| 7,912 | 39,56,000 |

If can be transformated to a categorical variable "price_grade" as:

| apartment_area | apartment_grade |
|-----|-----|
| 4,720 | Medium |
| 2,430 | Low |
| 4,368 | Medium |
| 3,969 | Low |
| 6,142 | High |
| 7,912 | High |

or as this:


| apartment_area | apartment_grade |
|-----|-----|
| 4,720 | 2 |
| 2,430 | 1 |
| 4,368 | 2 |
| 3,969 | 1 |
| 6,142 | 3 |
| 7,912 | 3 |

### Text-specific feature contruction

Text is arguably the most predominant medium of communication. Whether we think about social networks like Facebook or micro-blogging channels like Twitter or emails or short messaging services such as Whatsapp, text plays a major role in the flow of information. Hence [text-mining](#) is an important area of research.

Howevery, making sense of text data, due to the inherent unstructured nature of the data, is not so straightforward. In the first place, the text data chunks that we can think about do not have readily available features, like structured data sets, on which machine learning tasks can be executed. All the machine learning models need numerical data as input. So the text data in the data sets need to be transformed into numerical features.

Text data, or corpus which is the more popular keyword, is converted to a numerical representation following is process is known as **vectorization**. In this process, word occurences in all documents belonging to the corpus are consolidated in the form of **bag-of-words**. There are three major steps that are followed:

1. Tokenize
2. Count
3. Normalize

In order to tokenize a corpus, the blank spaces and punctuations are used as delimiters to separate out the words, or tokens. Then the number of occurences of each token is counted, for each document. Lastly, tokens are weighted with reducing importance when they occur in the majority of the documents. A matrix is then formed with each token representing a column and a specific document of the corpus representing each row. Each cell contains the count of occurrence of the token in a specific document. This matrix is known as a document-term matrix (also known as a term-document matrix).

