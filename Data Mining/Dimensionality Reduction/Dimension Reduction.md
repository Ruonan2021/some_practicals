# Dimensionality Reduction

# Part 1: Derived Variables

Feature selection is a method to select an informative set of features, while eliminating irrelevant and/or redundant ones , to achieve:

1. Higher learning accuracy.
2. Lower computational cost during modelling.
3. Better model interpretability.  
4. Enhanced generalization by reducing Overfitting



## 1.1 Single Variable Transformations

1. **Standardize numeric**
   1. Why: allows comparisons between variables in a same scale. Particular useful for clustering memory-based reasoning which depend on the concept of distance.
   2. How: values with $\mu = 0$, and $\sigma = 1$
2. **Percentiles**
   1. Why: useful when **relative** position is more important than absolute.
   2. How: For example, given a group of people, a member with height at the 80th percentile means that 80% among the other members have lower height.  
3. **Convert Counts into Rates**
   1. Why: useful for counts concerning events over time.
   2. How: counts divide by some fixed time unit
   3. Example: number of purchases, number of late deliveries  
4. **Replace Categorical Variables with Numeric Variables**  
   1. Why: useful when the numbers are meaningful for the data mining task.
   2. How: *Numeric descriptor* variables or *binary indicator variables*.  
      1. Numeric descriptor variables:
         1. Replace a categorical variable **with a handful of numerical variables** capturing important aspects of the categories based on what needs to be predicted.
         2. E.g. a city is characterized by a population, medium income, annual rainfall etc.
      2. Binary indicator variables:
         1. Create a binary variable for each category which is 1 if the category is present and 0, otherwise.
         2. Good: Works well with few categories.
         3. Bad: For a larger number of categories, the number of variables explodes, deteriorating the data mining model performance.  
   3. Example: simply replacing cities with numbers obtained by an alphabetic enumeration is meaningless and misleading, as two cities might turn out be closer than others without any reason.  
5. **Replace Numeric Variables with Categorical Variables**
   1. Why: Useful because it places outliers in one **bin**.
   2. How: Divide the range of a numeric variable into a set of subranges, the bins, and replace each numeric value with a bin number . 
   3. Ways of creating bins:
      1. Equal width binning: bins of equal width, but unequal height.
      2. Equal weight binning: divides the set of instances into subsets of equal size.
      3. Supervised binning uses information of the target variable to reshape the input variable.  



## 1.2 Combining Variables

Ratio

1. When two variables are **highly-correlated**, regression models can be harmful.
2. Combining highly correlated variables as ratios can be useful. ***This new variable should have high variance***, otherwise they do not add new information.
3. Example:
   1. In universities, the number of students and number of staff members are highly correlated.
   2. Their ratio indicates the amount of attention that a student should expect.  



## 1.3 Extracting Features from Structured Data  

Extracting features from time series data: use full year to eliminate seasonal effects

Extracting from geodata



## 1.4 Handling Sparse Data  

1. Context
   1.  Netflix Ratings Data, approximately 100 million ratings, 480 thousand users, 17.5
      thousand movies.  Narrow data set because each row contains just four fields: user id, movie id, date, rating.
2. To handle:
   1. Create  a small number of dense variables to summarize information from many sparse variables.
      1. Ratings in the first month.
      2. Ratings per month (after first month).
      3. Total number of ratings.
      4. Proportion of {love, hate} ratings.  
   2. Capture patterns across multiple variables in one variable 
      1. E.g. Action movie rating, romantic movie ratings...
   3. Bin together values from sparsely populated variables.  



# Part2: Dimensionality Reduction

## 2.1 Problems with High-Dimensional Data  

1. Risk of correlation
2. Risk of overfitting
3. Risk of sparse data



## 2.2 Variable Selection

1. Independence

   1. Numeric: use linear correlation coefficient
   2. Nominal: use average mutual information

2. Correlation

   1. ![image-20220502100628604](C:/Users/Lenovo/AppData/Roaming/Typora/typora-user-images/image-20220502100628604.png)			

3. Average Mutual Information

   1. ![image-20220502100732470](C:/Users/Lenovo/AppData/Roaming/Typora/typora-user-images/image-20220502100732470.png)

4. Heuristic methods

   For many prediction problems, there is no optimal algorithm for variable selection. However, there are many good heuristic methods.  Firstly separate data set into training, validation and test sets, use training and test set to build model, then  use validation set to select the best model.

   1. **Exhaustive Feature Selection**: $\sum_i^n C_n^i, i=1, 2, ..., n$, if the number of variables is $n$, then the number of combinations will be $2^n - 1$
   2. **Using a target variable**: e.g. decision tree. However the number of instances might be insufficient when it is relatively small compared with the  number of variable.
   3. **Sequential feature selection**: Forward selection, Backward selection(For high-dimensional data sets, backward selection is impractical) 

## 2.3 Variable Transformation

### 2.3.1 Linear Algebra and Statistics Revision  

1. A linear transformation $T: R^n \rightarrow R^k$ :  is a mapping from $R^n$ to $R^k$ such that:
   $T(x+y) = T(x) + T(y)$
   $T(cx) = cT(x)$  
2. Eigenvector and Eigenvalues
   1. An eigenvector of a square matrix $A$ is a vector $u$, associated with a  scalar l known as the eigenvalue, such that: $\boldsymbol{Au} = \lambda \boldsymbol{u}$, which means scale changed while direction remain unchanged.





### 2.3.2 Principal Component Analysis  

**What is PCA**

PCA is dimensionality reduction method, mapping original data by an orthogonal projection matrix($P$) to a smaller number of dimensions($Y = XP$). 

**Principal component characteristics**

1. Each column of $P$ is a principal component, representing the direction of the reduced subspace.
2.  each component is the **linear combination** of the original variables.
3. PCA finds directions (principal components) along which the data is spread the most from the mean, i.e. capture the most variability  
4. The greatest variance in the data comes lies on the first principal component, the second greatest variance lies on the second principal component and so on. 

**What to minimize**

1. The first principal component is the line **minimizing the sum of squared orthogonal distances from each data point to the line.**  

![image-20220502111038517](C:/Users/Lenovo/AppData/Roaming/Typora/typora-user-images/image-20220502111038517.png)



**How to compute**

PCA computes the eigenvectors $\boldsymbol{v}_1, ..., \boldsymbol{v}_k$ corresponding to the largest eigenvalues $\boldsymbol{\lambda}_1, ..., \boldsymbol{\lambda}_k$ of the covariance matrix $\sum$



**Summary**

1. Reduces the number of variables.
2. The principal components are orthogonal to each other, meaning that the model is relatively easy to interpret.
3. Derives independent variables because of orthogonality.
4. Sequentially extracts variance, so that the most information is contained in the first few components.
5. Usually considered as an unsupervised learning technique.
6. Has the disadvantage that in the resulting subspace, there are aspects of the original space which are not captured  



Unfinished...



### 2.3.3 Singular Value Decomposition 

Unfinished...

### 2.3.4 Projection Pursuit Regression  

Unfinished...





