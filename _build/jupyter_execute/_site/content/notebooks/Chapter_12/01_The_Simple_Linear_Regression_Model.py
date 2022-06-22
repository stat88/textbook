#!/usr/bin/env python
# coding: utf-8

# ## The Simple Linear Regression Model ##

# The model involves a variable called the *response* and another called a *predictor variable* or *feature*. The assumptions are that the response is a linear function of the predictor variable, called a *signal*, plus random error, called *noise*:
# 
# $$
# \text{response} ~ = ~ \text{signal} ~ + ~ \text{noise}
# $$
# 
# Our job is to extract the signal. The data are observations on the predictor variable and the response of $n$ individuals. We assume that we can measure the predictor variable perfectly accurately, and that it is therefore not random. The only random component of the response is the noise.
# 
# Formally, for individuals $i = 1, 2, 3, \ldots, n$, the response is assumed to be
# 
# $$
# Y_i ~ = ~ \beta_0 + \beta_1x_i + \epsilon_i
# $$
# 
# where:
# 
# - $\beta_0$ and $\beta_1$ are unobservable constant parameters.
# - $x_i$ is the value of the predictor variable for individual $i$ and is assumed to be constant (that is, not random).
# - The errors $\epsilon_1, \epsilon_2, \ldots, \epsilon_n$ are i.i.d. normal $(0, \sigma^2)$ random variables.
# - The error variance $\sigma^2$ is an unobservable constant parameter, and is assumed to be the same for all individuals $i$.
# 
# For each individual $i$, we would like to get as close as we can to the signal $\beta_0 + \beta_1x_i$. We can't see the true line $y = \beta_0 + \beta_1x$, but we can estimate it by the regression line. Thus our estimator of the $i$th signal $\beta_0 + \beta_1x_i$ is
# 
# $$
# \hat{Y}_i ~ = ~ \hat{\beta}_0 + \hat{\beta}_1x_i
# $$
# 
# where $\hat{\beta}_0$ and $\hat{\beta}_1$ are the interecept and slope of the regression line.
# 
# To estimate the true slope $\beta_1$, it is a good idea to examine the properties of the estimated slope $\hat{\beta}_1$. Before that, let's examine the response.
# 
# It is important to keep in mind that all the subsequent calculations in this chapter will be performed under the regression model. The model does not pretend to be the truth: is only a set of assumptions about reality. If the assumptions are not valid for your data, then the calculations of this chapter will not be valid either.

# ### Individual Responses ###
# 
# Fix $i$ in the range $1$ through $n$. The response $Y_i$ of individual $i$ is the sum of two pieces: the $i$th signal $\beta_0 + \beta_1x_i$ and the noise $\epsilon_i$. 
# 
# The signal is a constant, and $\epsilon_i$ has the normal $(0, \sigma^2)$ distribution.
# 
# Therefore **the response $Y_i$ of individual $i$ has the normal distribution with mean $\beta_0 + \beta_1x_i$ and variance $\sigma^2$**.
# 
# The randomness in $Y_i$ comes only from $\epsilon_i$ as the $i$th signal is a constant. Since $\epsilon_1, \epsilon_2, \ldots, \epsilon_n$ are independent, the individual responses $Y_1, Y_2, \ldots, Y_n$ are independent of each other.

# ### Average Response ###
# 
# Let $\bar{Y} = \frac{1}{n}\sum_{i=1}^n Y_i$ denote the average response of the $n$ individuals.
# 
# Then $\bar{Y}$ is a linear combination of independent normally distributed random variables. So the distribution of $\bar{Y}$ is normal.
# 
# The mean of the distribution is
# 
# $$
# \begin{align*}
# E(\bar{Y}) ~ &= ~ \frac{1}{n}\sum_{i=1}^nE(Y_i) \\
# &= ~ \frac{1}{n}\sum_{i=1}^n (\beta_0 + \beta_1 x_i) \\
# &= ~ \frac{1}{n}\sum_{i=1}^n \beta_0 ~ + ~ \frac{1}{n}\sum_{i=1}^n \beta_1x_i \\
# &= ~ \frac{1}{n} \cdot n\beta_0 ~ + ~ \beta_1\frac{1}{n}\sum_{i=1}^n x_i \\
# &= ~ \beta_0 + \beta_1 \bar{x}
# \end{align*}
# $$
# 
# Thus the expected average response is the signal at the average value of the predictor variable.
# 
# Since the individual responses are independent of each other, we have
# 
# $$
# Var(\bar{Y}) ~ = ~ \frac{1}{n^2}\sum_{i=1}^n Var(Y_i) ~ = ~ \frac{1}{n^2}\cdot n\sigma^2 ~ = ~ \frac{\sigma^2}{n}
# $$
# 
# To summarize, **the distribution of the average response $\bar{Y}$ is normal with mean $\beta_0 + \beta_1\bar{x}$ and variance $\frac{\sigma^2}{n}$**.

# In[ ]:




