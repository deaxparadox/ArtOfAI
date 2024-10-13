# Exploratory Data Analysis

#### Exploratory Data Analysis refers to the critical process of performing initial investigations on data so as to discover patterns,to spot anomalies,to test hypothesis and to check assumptions with the help of summary statistics and graphical representations.


EDA is primary used to see what data can reveal beyond the formal modeling or hypothesis testing task and provides a better understanding of data set variables and relationships between them. It can also help determine if the statistical techniques you are considering for data analysis are appropriate. **EDA technique is widely used method in the data discovery process**.


### Why is EDA important?

The main purpose of EDA is to help look at data before making assumptions. It can ehlp identify obvious erros, as well as better understanding patterns within the data, detect outliers or anomalous events, find interesting relations among the variables.

Data scientists can use exploratory analysis to ensure the results they produce are valid and applicable to any desired business outcomes and goals. EDA also helps stakeholders by confirming they are asking the right questions. EDA can help answer questions about standard deviations, categorical variables, and confidence intervals.

### Key aspects of EDA 

- **Distribution of data**: Examing the distribution of data points to understand their range, central trendencies (men, median), and dispersion (variance, standard deviation).
- **Grpahical Representation**: Utilizing charts such as histograms, box plots, scatter plots, and bar charts to visualize relationships within the data and distributions of variables.
- **Outlier detection**: Identifying unusual values that deviate from other data points. Outliers can influence statistical analyses and might indicate data entry erros or unique cases.
- **Correlation Analysis**: Checking the relationship between variables to understand how they might affect each other. This include computing correlation coefficients and creating correlation matrices.
- **Handling missing values**: Detecting and deciding how to address missing data points, whether by imputation or removal, depending on their impect and the amount of missing data.
- **Summary statistics**: Calculating key statistics that provide insight into data trends and nuances.
- **Testing assumptions**: Many statistical tests and models assume the data meet certain conditions (like normality or homoscedasticity). EDA helps verify these assumptions.

### Why eda is important?

EDA is important for several reasons, especially in the context of data science and statistical modeling.

1. **Understanding data**: EDA helps in gettting familiar with the dataset, understanding the number of features, the type of data in each features, and the distribution of data points. This understanding is crucial for selecting appropriate analysis or prediction techniques.
2. **Identifying patterns and relationship**: Through visualizations and statistical summaries, EDA can reveal hidden patterns and intrinsic relationships between variables. These insights can guide further analysis and enable more effective feeature engineering and model building.
3. **Detecting Anomalies and Outliers**: EDA is essential for identify erros or unusual data points that may adversely affect the resutls of your analysis. Detecting these early can prevent costly mistakes in predictive modeling and analysis.
4. **Testing assumptions**: Many statistical models assume that data follow a certain distribution or that variables are independent.

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
3. Data quality evaluation