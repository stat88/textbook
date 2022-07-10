#!/usr/bin/env python
# coding: utf-8

# In[1]:


# NO CODE

from datascience import *
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
import numpy as np
from scipy import stats
import warnings
warnings.filterwarnings("ignore")


# ## Towards Multiple Regression ##

# This section is an extended example of applications of the methods we have derived for regression. We will start with simple regression, which we understand well, and will then indicate how some of the results can be extended when there is more than one predictor variable.
# 
# The data are from a study on the treatment of Hodgkin's disease, a type of cancer that can affect young people. The good news is that treatments for this cancer have [high success rates](https://en.wikipedia.org/wiki/Hodgkin_lymphoma#Prognosis). The bad news is that the treatments can be rather strong combinations of chemotherapy and radiation, and thus have serious side effects. A goal of the study was to identify combinations of treatments with reduced side effects.
# 
# The table `hodgkins` contains data on a random sample of patients. Each row corresponds to a patient. The columns contain the patient's height in centimeters, the amount of radiation, the amount of medication used in chemotherapy, and measurements on the health of the patient's lungs.

# In[2]:


# NO CODE

hodgkins = Table.read_table('../../data/hodgkins.csv')
diffs = hodgkins.column(4) - hodgkins.column(3)
hodgkins = hodgkins.with_columns('difference', diffs)


# In[3]:


hodgkins


# In[4]:


n = hodgkins.num_rows
n


# The radiation was directed towards each patient's chest area or "mantle", to destroy cancer cells in the lymph nodes near that area. Since this could adversely affect the patients' lungs, the researchers measured the health of the patients' lungs both before and after treatment. Each patient received a score, with larger scores corresponding to more healthy lungs. 
# 
# The table records the baseline scores and also the scores 15 months after treatment. The change in score (15 month score minus baseline score) is in the final column. Notice the negative differences: 15 months after treatment, many patients' lungs weren't doing as well as before the treatment. 
# 
# Perhaps not surprisingly, patients with larger baseline scores had bigger drops in score. 

# In[5]:


hodgkins.scatter('base', 'difference')


# We will regress the difference on the baseline score, this time using the Python module `statsmodels` that allows us to easily perform multiple regression as well. You don't have to learn the code below (though it's not hard). Just focus on understanding an interpreting the output.
# 
# As a first step, we must import the module.

# In[6]:


import statsmodels.api as sm


# The `Table` method `to_df` allows us to convert the table `hodgkins` to a structure called a data frame that works more smoothly with `statsmodels`.

# In[7]:


h_data = hodgkins.to_df()
h_data


# There are several variables we could use to predict the difference. The only one we wouldn't use is the 15 month measurement, as that's precisely what we won't have for a new patient before the treatment is adminstered. 
# 
# But which of the rest should we use? One way to choose is to look at the *correlation matrix* of all the variables.

# In[8]:


h_data.corr()


# Each entry in this table is the correlation between the variable specified by the row label and the variable specified by the column label. That's why all the diagonal entries are $1$.
# 
# Look at the last column (or last row). This contains the correlation between `difference` and each of the other variables. The baseline measurement has the largest correlation. To run the regression of `difference` on `base` we must first extract the columns of data that we need and then use the appropriate `statsmodels` methods.
# 
# First, we create data frames corresponding to the response and the predictor variable. The methods are not the same as for `Tables`, but you will get a general sense of what they are doing.

# In[9]:


y = h_data[['difference']]  # response
x = h_data[['base']]        # predictor

# specify that the model includes an intercept
x_with_int = sm.add_constant(x) 


# The name of the `OLS` method stands for Ordinary Least Squares, which is the kind of least squares that we have discussed. There are other more complicated kinds that you might encounter in more advanced classes.
# 
# There is a lot of output, some of which we will discuss and the rest of which we will leave to another class. For some reason the output includes the date and time of running the regression, right in the middle of the summary statistics.

# In[10]:


simple_regression = sm.OLS(y, x_with_int).fit()
simple_regression.summary()


# There are three blocks of output. We will focus only on the the middle block.
# 
# - `const` and `base` refer to the intercept and baseline measurement.
# - `coef` stands for the estimated coefficients, which in our notation are $\hat{\beta_0}$ and $\hat{\beta_1}$.
# - `t` is the $t$-statistic for testing whether or not the coefficient is 0. Based on our model, its degrees of freedom are $n-2 = 20$; you'll find this under `Df Residuals` in the top block.
# - `P > |t|` is the total area in the two tails of the $t$ distribution with $n-2$ degrees of freedom.
# - `[0.025 0.975]` are the ends of a 95% confidence interval for the parameter.
# 
# For the test of whether or not the true slope of the baseline measurement is $0$, the observed test statistic is
# 
# $$
# \frac{-0.5447 - 0}{0.150} ~ = ~ -3.63
# $$
# 
# The area in one tail is the chance that the $t$ distribution with $20$ degrees of freedom is less than $-3.63$. That's the cdf of the distribution evaluated at $-3.63$:

# In[11]:


one_tail = stats.t.cdf(-3.63, 20)
one_tail


# Our test is two-sided (large values of $\vert t \vert$ favor the alternative), so the $p$-value of the test is the total area of two tails, which is the displayed value $0.002$ after rounding.

# In[12]:


p = 2*one_tail
p


# To find a 95% confidence interval for the true slope, we have to replace $2$ in the expression $\hat{\beta}_1 \pm 2SE(\hat{\beta}_1)$ by the corresponding value from the $t$ distribution with 20 degrees of freedom. That's not very far from $2$:

# In[13]:


t_95 = stats.t.ppf(0.975, 20)
t_95


# A 95% confidence interval for the true slope is given by $\hat{\beta}_1 \pm t_{95}SE(\hat{\beta}_1)$. The observed interval is therefore given by the calculation below, which results in the same values as in the output of `sm.OLS` above.

# In[14]:


# 95% confidence interval for the true slope

-0.5447 - t_95*0.150, -0.5447 + t_95*0.150


# ### Multiple Regression ###
# What if we wanted to regress `difference` on both `base` and `chemo`? The first thing to do would be to check the correlation matrix again:

# In[15]:


h_data.corr()


# What you are looking for is not just that `chemo` is the next most highly correlated with `difference` after `base`. More importantly, you are looking to see how strongly the two predictor variables `base` and `chemo` are linearly related *to each other*. That is, you are trying to figure out whether the two variables pick up genuinely different dimensions of the data.
# 
# The correlation matrix shows that the correlation between `base` and `chemo` is only about $0.06$. The two predictors are not close to being linear functions of each other. So let's run the regression.
# 
# The code is exactly the same as before, except that we have included a second predictor variable.

# In[16]:


y = h_data[['difference']]      # response
x2 = h_data[['base', 'chemo']]  # predictors

# specify that the model includes an intercept
x2_with_int = sm.add_constant(x2) 

multiple_regression = sm.OLS(y, x2_with_int).fit()
multiple_regression.summary()


# Ignore the scary warning above. There isn't strong multicollinearity (predictor variables being highly correlated with each other) nor other serious issues.
# 
# Just focus on the middle block of the output. It's just like the middle block of the simple regression output, with one more line corresponding to `chemo`.
# 
# All of the values in the block are interpreted in the same way as before. The only change is in the degrees of freedom: because you are estimating one more parameter, the degrees of freedom have dropped by $1$, and are thus $19$ instead of $20$.
# 
# For example, the 95% confidence interval for the slope of `chemo` is calculated as follows.

# In[17]:


t_95_df19 = stats.t.ppf(0.975, 19)

0.1898 - t_95_df19*0.076, 0.1898 + t_95_df19*0.076


# Finally, take a look at the value of `R-squared` in the very top line. It is $0.546$ compared to $0.397$ for the simple regression. It's a math fact that the more predictor variables you use, the higher the `R-squared` value will be. This tempts people into using lots of predictors, whether or not the resulting model is comprehensible.
# 
# With an "everything as well as the kitchen sink" approach to selecting predictor variables, a researcher might be inclined to use all the possible predictors.

# In[18]:


y = h_data[['difference']]      # response
x3 = h_data[['base', 'chemo', 'rad', 'height']]  # predictors

# specify that the model includes an intercept
x3_with_int = sm.add_constant(x3) 

bad_regression = sm.OLS(y, x3_with_int).fit()
bad_regression.summary()


# This is not a good idea. We end up with a far more complicated model for no appreciable gain in `R-squared`. The "adjusted $R^2$" penalizes us for using more predictor variables: notice that the value of `Adj. R-squared` is smaller for the regression with all the predictors than for the regression with just `base` and `chemo`.

# Curious about how to select predictors, or about what makes a good regression? Then take some more statistics classes! This one is complete.

# In[ ]:




