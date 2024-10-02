# Exploratory Data Analysis

#### Exploratory data analysis (EDA) is used by data scientists to analyze and investigate data sets and summarize their main characteristics, often employing data visualization methods. EDA is also important for build machine learning models and pipelines.

EDA helps determine how best to manipulate data sources to get the answers you need, making it easier for data scientists to discover patterns, spot anomalies, test a hypotheses, or check assumptions.

EDA is primary used to see what data can reveal beyond the formal modeling or hypothesis testing task and provides a better understanding of data set variables nad relationships between them. It can also help determine if the statistical techniques you are considering for data analysis are appropriate. **EDA technique is widely used method in the data discovery process**.


### Why is EDA important?

The main purpose of EDA is to help look at data before making assumptions. It can ehlp identify obvious erros, as well as better understanding patterns within the data, detect outliers or anomalous events, find interesting relations among the variables.

Data scientists can use exploratory analysis to ensure the results they produce are valid and applicable to any desired business outcomes and goals. EDA also helps stakeholders by confirming they are asking the right questions. EDA can help answer questions about standard deviations, categorical variables, and confidence intervals.

### Exploratory data analysis tools

Specific statistical functions and techniques you can perform with EDA tools include:

- Clustering and dimension reduction techniques, which help create grahpical display of high-dimensional data containing many variables.
- Univariate visualization of each field in the row dataset, with summary statistics.
- Bivariate visualizations and summary statistics that allow you to assess the relationship between each variable each variable in the dataset and the target variable you're looking at.
- Multivariate visualizations, for mapping and understanding interactions between different fields in the data.
- K-means Clustering is the clustering method in unsupervised learing where data points are assigned into K groups, i.e. the number of clusters, based on the distance from each group's centroid. The data points closest to a particular centroid will be clusterd under the same category. K-means Clustering is commonly used in [market segmentation](/docs/glossary/107-market-segmentation.md), [pattern recognition](/docs/glossary/108-pattern-recognition.md), and [image compression](/docs/glossary/109-image-compression.md).
- Predictive models, such as linear regression, use statistics and data to predict outcomes.


### Types of exploratory data analysis

There are four primary types of EDA:

1. **Univariate non-graphical**: This is simplest form of data analysis, where the data being analyzed consists of just one variable. Since it's sigle variable, it doesn't deal with causes and relationships. The main purpose of univariate analysis is to describe the data and find patterns that exists with it.

2. **Univariate graphical**: Non-graphical method don't provide a full picture of the data. Graphical methods are therefore required. Common types of univariate grahpics:

    - **Stem-and-leaf plots**: Which show all data values and shape of the destribution.
    - **Histograms**: a bar plot in which each bar represents the frequency (count) or proportion (count/total_count) of cases for a range of values.
    - **Box plots**: which graphically depict the five-number summary of minimum, first quartile, median, third quartile, and maximum.

3. **Multivariate nongraphical**: Mulitvariate data arises from more than one variable. Multivariate non-grahpica EDA techniques generally show the relationship between two or more variables of the data through cross-tabulation or statistics.

4. **Multivariate graphical**: Multivariate data uses graphics to display relationships between one or more sets of data. The most used grahic is a grouped bar plot or bar chart with  each representing one level of one of the variables and each bar within a group representing the levels of the other variable.

    - **Scatter plot**: which is used to plot data points on a horizontal and a vertical axis to show how much one variable is affected by another.
    - **Multivariate chart**: which is a graphical representation of the relationships between factors and a response.
    - **Run chart**: which is a line graph of data plotted over time.
    - **Bubble chart**: which is a data visualization that displays multiple circles (bubbles) in a two-dimensional plot.
    - **Heat map**:  which is a graphical representation of data where values are depicted by color.



### The process of EDA fundamentally comprises three main tasks:

1. Data overview and descriptive statistics
    - **What am i working with?**
    - Finding: 
        - Number of observations
        - Numbers and types of features
        - Overall missing rate
        - Duplicate oberservations.

    **We need to have deep understanding of our data to handle it efficiently in future machine learning tasks**.
2. Feature assessment and visualization
    - Univariate Analysis: Depeding on data we may need to perform
        - Standardize numerical data
        - One-hot encoding
        - Shifted or skewed
    - Multivariate Analysis
3. Data quality and evaluation