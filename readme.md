# <a name="top"></a>README TELCO-CHURN PROJECT
![]()

by: David Howell

<p>
  <a href="https://github.com/David-Howell/telco-churn" target="_blank">
    <img alt="David Howell seen here addressing the Texas Supreme Court" src="https://github.com/David-Howell/telco-churn/blob/main/IMG_3682.jpg" />
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
    - Findings
    - Methodologies
    - Conclusions / Recommendations
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
    i.e. understand categorical vs. numerical data, numbers as `int` or `float`, etc.
    - Split the data into training, validation, and testing subsets (60%, 20%, 20%)
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
    - Identify regression, classification, and/or other algorithms that address the data relationships
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
- The Distributions of Gender and Churn are different.
  - FALSE
- The Distributions of Senior citizens and non-Seniors are different.
  - TRUE


### Target variable
#### - Churn

### Need to haves (Deliverables):
- A model that will predict churn with a better accuracy than baseline
  - At around 80% we are well above the Baseline of 73%
  - Additionally, (and More importantly):
    - Baseline Recall was 0.00% and our model is at around 66% for out-of-sample data!!


### Nice to haves (With more time):
- Segmentation of customers into groups with targeted strategies to reduce churn within different segments


***

## <a name="findings"></a>Key Findings:
[[Back to top](#top)]

- Fiber customers churn way more than any other Internet Service group
- E-Checks are not bringing in the $$$


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

- Get data from MySQL
- Cache that!
- Fix Nulls
- Get data into numeric formats
- Encode appropriate fields

*********************

## <a name="explore"></a>Data Exploration:
[[Back to top](#top)]
- Python files used for exploration:
    - wrangle.py 
    - explore.py
    - modeling.py


### Takeaways from exploration:

- Things that aren't related to churn...
    - gender - they churn evenly
      - Can probably drop this field and not use it as a feature
    - phone servie
      - Everyone has phone service except a portion of the DSL customers
    - multiple lines
      - Multiple lines seems to line up with the DSL customers that do have phone
  - Things that don't matter much...
    - senior citizens - don't make up a great deal of customers
    - Streaming_tv
    - Streaming_movies
  - Things that seem to have a relationship to churn...
    - partner - no partner has more churn
    - dependents - no dependents has more churn
    - Fiber - DSL - No ISP 42%/19%/8% Churn
    - online backup      - not having leads to churn
    - online security    - not having leads to churn
    - device protection  - not having leads to churn
    - tech support       - not having leads to churn
    - Electronic check seems to be the LARGEST indicator of churn
      - 45% of customers using E-checks churn

***

## <a name="stats"></a>Statistical Analysis
[[Back to top](#top)]


### Stats Tests : T-Tests: Two Sample, Two Tailed Tests

- The t-test returns the t-statistic and the p-value:
    - t-statistic: 
        - Is the ratio of the departure of the estimated value of a parameter from its hypothesized value to its standard error. It is used in hypothesis testing via Gender, and Senior vs Churn t-test. 
        - It is used in a t-test to determine if you should support or reject the null hypothesis
        - t-statistic of 0 = H<sub>0</sub>
    -  - the p-value:
        - The probability of obtaining test results at least as extreme as the results actually observed, under the assumption that the null hypothesis is correct
- We wanted to compare the individual clusters to each other. 

#### Hypothesis:
- The null hypothesis (H<sub>0</sub>) is They are the same
- The alternate hypothesis (H<sub>1</sub>) is They are different

#### Confidence level and alpha value:
- I established a 95% confidence level
- alpha = 1 - confidence, therefore alpha is 0.05


#### Results:
- Gender: They're the same
- Seniors: They're different

#### Summary:
These let us decide to drop gender, and keep seniors
***

## <a name="model"></a>Modeling:
[[Back to top](#top)]

### Model Preparation:

- As above, so below

### Baseline
    
- Baseline Results: 73% Accuracy and 0.00% Recall
    

- Selected features to input into models:
    - features = [['senior',
 'partner',
 'dependents',
 'tenure',
 'e_bill',
 'monthly_charges',
 'total_charges',
 'DSL',
 'Fiber',
 'one_year',
 'two_year',
 'bank_transfer',
 'cc',
 'e_check',
 'add_ons']]

***

### Models and R<sup>2</sup> Values:
- Will run the following regression models:
  - Decision Tree
  - Random Forest
  - K Nearest Neighbors
  - Logistic Regression
    

- Other indicators of model performance with breif defiition and why it's important:

  - Accuracy: Overall how are we doing with our predictions
  - Recall: How many misses are we getting and can we minimize that
    
#### Model 1: Linear Regression (LibLinear with L1 penalty)


- Model 1 results: Accuracy around 80% and Recall around 66%



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

