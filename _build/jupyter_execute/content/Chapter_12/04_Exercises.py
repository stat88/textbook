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
import statsmodels.api as sm
import warnings
warnings.filterwarnings("ignore")


# In[2]:


# NO CODE

pulse = Table.read_table('../../data/pulse.csv').drop(0)
m_smokers = pulse.where('Sex', 0).where('Smoke', 1)
m_data = m_smokers.to_df()
m_data
m_y = m_data[['Active']]
m_x = m_data[['Rest']]
m_x_with_int = sm.add_constant(m_x) 


# ## Exercises ##

# **1.**
# Recall that the intercept of the regression line is given by "the average of $Y$ minus the slope times the average of $x$. That is, $\hat{\beta}_0 = \bar{Y} - \hat{\beta}_1\bar{x}$. Is $\hat{\beta}_0$ an unbiased estimator of $\beta_0$?

# **2.**
# The *fitted* value of the response for the $i$th indvidual is the height of the regression line at $x_i$:
# 
# $$
# \hat{Y}_i ~ = ~ \hat{\beta}_0 + \hat{\beta}_1x_i
# $$
# 
# Show that $\hat{Y}_i$ is an unbiased estimator of $\beta_0 + \beta_1x_i$, the height of the true line at $x_i$.

# **3.** 
# Refer to the regression of active pulse rate on resting pulse rate in [Section 12.2](ch12.2). Here are the estimated values again, along with some additional data.

# In[3]:


active = pulse.column(0)
resting = pulse.column(1)

slope, intercept, r, p, se_slope = stats.linregress(x=resting, y=active)
slope, intercept, r, p, se_slope


# In[4]:


mean_active, sd_active = np.mean(active), np.std(active)
mean_active, sd_active


# In[5]:


mean_resting, sd_resting = np.mean(resting), np.std(resting)
mean_resting, sd_resting


# **a)** Use the Data 8 formulas for the slope and intercept of the regression line (proved in the previous chapter) and confirm that you get the same values as reported by `stats.linregress`.

# **b)** Find the regression estimate of the active pulse rate of a student whose resting pulse rate is 70.
# 
# **c)** Find the SD of the residuals. This is roughly the error in the estimate in Part **b**.

# **4.**
# Restrict the population of students in the previous exercise just to the male smokers.

# In[6]:


m_smokers = pulse.where('Sex', 0).where('Smoke', 1)
m_smokers.num_rows


# In[7]:


m_smokers.scatter(1, 0)


# Here is a summary of the regression of the active pulse rate on the resting pulse rate for these data. Since the population consists just of male smokers, the parameters in the model might have different values from those in the previous exercise.

# In[8]:


# NO CODE

reg4 = sm.OLS(m_y, m_x_with_int).fit()
reg4.summary()


# **a)** Find the correlation between the active and resting pulse rates for these data and compare it with the corresponding value for all students.
# 
# **b)** Show the calculation that leads to the displayed confidence interval for the true slope of `Rest`.
# 
# **c)** Use the displayed confidence interval for the true intercept to provide the conclusion of a test of hypotheses $H_0$: $\beta_0 = 0$ versus $H_A$: $\beta_0 \ne 0$ at the 5% level. Explain your reasoning.
# 
# **d)** Show the calculation that leads to the displayed value of `P>|t|` for the intercept. Is the value consistent with your answer to Part **c**?
# 
# **e)** Use the displayed results for the slope of `Rest` to provide the conclusion of a test of hypotheses $H_0$: $\beta_1 = 0$ versus $H_A$: $\beta_1 \ne 0$ at the 1% level. Explain your reasoning.
