# <a name="top"></a>README TELCO-CHURN PROJECT
![]()

by: David Howell

<p>
  <a href="https://github.com/David-Howell/telco-churn" target="_blank">
    <img alt="David" src="https://github.com/David-Howell/telco-churn/blob/main/IMG_3682.jpg" />
  </a>
</p>


***
[[Project Description](#project_description)]
[[Project Planning](#planning)]
[[Key Findings](#findings)]
[[Data Dictionary](#dictionary)]
[[Data Acquire and Prep](#wrangle)]
[[Data Exploration](#explore)]
[[Statistical Analysis](#stats)]
[[Modeling](#model)]
[[Conclusion](#conclusion)]
___

<img src="https://github.com/David-Howell/telco-churn/blob/main/telcoco.png">

## <a name="project_description"></a>Project Description:
[[Back to top](#top)]
#### We will explore the Telco Dataset for a greater understanding of the attributes and drivers of customer churn.
- We will ask questions of the data to further our understanding
- The resulting charts and statistical tests will help answer our questions
- We will split our data to avoid overfitting in modeling and avoid data poisoning
- Machine Learning models will be constructed and fit, statistically validated, and tested
- A report will be generated for a 5-minute presentation to management, to include:
    - The work done
    - Why certain lines were followed
    - The Goals of the exploration and experiements
    - Fingings
    - Methodologies
    - Conclusions / Recomendations
***
## <a name="planning"></a>Project Planning: 
[[Back to top](#top)]

### Project Outline:
- Acquire the data:
    - The original data is kept in a MySQL RDBMS managed by the codeup DS department
    - An `env.py` file is needed to provide credentials to access the RDBMS
    - An `acquire.py` file will be created to reproduce gathering the of the data
        - This repository will include a .csv caching of the acquired data
    - The Python library `pandas` will be utilized to acquire the data and manipulate as a DataFrame
    
- Preparation:
    - Initial understanding of the form and format of the data fields, and find the target variable
    - Clean fields for ease of data manipulation and exploration, 
    i.e. understand categorical vs. numerical data, numbers as int or float, etc.
    - Split the data into training, validation, and testing subsets (60%,20%,20%)
    - A `prepare.py` file will be created with functions to recreate this process
    - Python tools will include:
        - `pandas` will be used to handle nulls, outliers, normalizing text, changing data types
        - `matplotlib`, (Sam Norman)`seaborn`, and `lux` help visualize info included in fields
        - `scikit-learn` is used to split the data into train, validate, and test subsets
        
- Exploratory Analysis, Visualization, Feature Engineering, and Feature Selection:
    - Discover which features have the greatest impact on the target, and drive the outcome
    - An `explore.py` file will be created to recreate the visualization and prepocessing of the data
    - Visualizations will show the relationship between attributes, each other, and the target
    - New features will be created from transformation and/or combination of data attributes
    - Features (or subsets) that are overly noisy, extraneous, or confounding will be removed
    - Final Features will be scaled and/or encoded for modeling
    
- Modeling:
    - Identify regression, classification, and/or other algorithms that adress the data relationships
    - Create, explore, and evaluate Machine Learning models that predict the target
        - Build the thing
        - Fit(train) the thing
        - Use the thing
        - Evaluate the best performing models on out of sample validation information
        - Tune the features for best performance on validation data
        - Open the Test envelope: only on final models will we evaluate performance on the out of sample test data
        
- Delivery:
    - A final analysis notebook will be prepared for presentation to the team and the team lead
    - A 5 minute presentation of the final notebook will be given
    - This will include the most relevant insights, visualizations, and statistical examinations
    - A conclusion will be derived and a recomendation(s) will be suggested
        
### Hypothesis



### Target variable
#### - Churn

### Need to haves (Deliverables):
- A model that will predict churn with a better accuracy than baseline


### Nice to haves (With more time):
- Segmentation of customers into groups with targeted strategies to reduce churn within different segments


***

## <a name="findings"></a>Key Findings:
[[Back to top](#top)]




***

## <a name="dictionary"></a>Data Dictionary  
[[Back to top](#top)]

### Data Used
---
| Attribute | Definition | Data Type |
| ----- | ----- | ----- |
| | | |
| | | |
| | | |
| | | |
| | | |
| | | |

***

## <a name="wrangle"></a>Data Acquisition and Preparation
[[Back to top](#top)]

![]()


### Wrangle steps: 


*********************

## <a name="explore"></a>Data Exploration:
[[Back to top](#top)]
- Python files used for exploration:
    - wrangle.py 
    - explore.py
    - modeling.py


### Takeaways from exploration:


***

## <a name="stats"></a>Statistical Analysis
[[Back to top](#top)]

### Stats Test 1: ANOVA Test: One Way

Analysis of variance, or ANOVA, is a statistical method that separates observed variance data into different components to use for additional tests. 

A one-way ANOVA is used for three or more groups of data, to gain information about the relationship between the dependent and independent variables: in this case our clusters vs. the log_error, respectively.

To run the ANOVA test in Python use the following import: \
<span style="color:green">from</span> scipy.stats <span style="color:green">import</span> f_oneway

- f_oneway, in this case, takes in the individual clusters and returns the f-statistic, f, and the p_value, p:
    - the f-statistic is simply a ratio of two variances. 
    - The p_vlaue is the probability of obtaining test results at least as extreme as the results actually observed, under the assumption that the null hypothesis is correct

#### Hypothesis:
- The null hypothesis (H<sub>0</sub>) is
- The alternate hypothesis (H<sub>1</sub>) is 

#### Confidence level and alpha value:
- I established a 95% confidence level
- alpha = 1 - confidence, therefore alpha is 0.05

#### Results:


#### Summary:


### Stats Test 2: T-Test: One Sample, Two Tailed
- A T-test allows me to compare a categorical and a continuous variable by comparing the mean of the continuous variable by subgroups based on the categorical variable
- The t-test returns the t-statistic and the p-value:
    - t-statistic: 
        - Is the ratio of the departure of the estimated value of a parameter from its hypothesized value to its standard error. It is used in hypothesis testing via Student's t-test. 
        - It is used in a t-test to determine if you should support or reject the null hypothesis
        - t-statistic of 0 = H<sub>0</sub>
    -  - the p-value:
        - The probability of obtaining test results at least as extreme as the results actually observed, under the assumption that the null hypothesis is correct
- We wanted to compare the individual clusters to the total population. 
    - Cluster1 to the mean of ALL clusters
    - Cluster2 to the mean of ALL clusters, etc.

#### Hypothesis:
- The null hypothesis (H<sub>0</sub>) is 
- The alternate hypothesis (H<sub>1</sub>) is 

#### Confidence level and alpha value:
- I established a 95% confidence level
- alpha = 1 - confidence, therefore alpha is 0.05


#### Results:


#### Summary:

***

## <a name="model"></a>Modeling:
[[Back to top](#top)]

### Model Preparation:

### Baseline
    
- Baseline Results: 
    

- Selected features to input into models:
    - features = []

***

### Models and R<sup>2</sup> Values:
- Will run the following regression models:

    

- Other indicators of model performance with breif defiition and why it's important:

    
    
#### Model 1: Linear Regression (OLS)


- Model 1 results:



### Model 2 : Lasso Lars Model


- Model 2 results:


### Model 3 : Tweedie Regressor (GLM)

- Model 3 results:


### Model 4: Quadratic Regression Model

- Model 4 results:


## Selecting the Best Model:

### Use Table below as a template for all Modeling results for easy comparison:

| Model | Validation/Out of Sample RMSE | R<sup>2</sup> Value |
| ---- | ----| ---- |
| Baseline | 0.167366 | 2.2204 x 10<sup>-16</sup> |
| Linear Regression (OLS) | 0.166731 | 2.1433 x 10<sup>-3</sup> |  
| Tweedie Regressor (GLM) | 0.155186 | 9.4673 x 10<sup>-4</sup>|  
| Lasso Lars | 0.166731 | 2.2204 x 10<sup>-16</sup> |  
| Quadratic Regression | 0.027786 | 2.4659 x 10<sup>-3</sup> |  


- {} model performed the best


## Testing the Model

- Model Testing Results

***

## <a name="conclusion"></a>Conclusion:
[[Back to top](#top)]

