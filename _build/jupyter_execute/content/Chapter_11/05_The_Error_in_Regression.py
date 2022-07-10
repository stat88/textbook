#!/usr/bin/env python
# coding: utf-8

# ## The Error in Regression ##

# To assess the accuracy of the regression estimate, we must quantify the amount of error in the estimate. The error in the regression estimate is called the *residual* and is defined as
# 
# $$
# D = Y - \hat{Y}
# $$
# 
# where $\hat{Y} = \hat{a}(X-\mu_X) + \mu_Y$ is the regression estimate of $Y$ based on $X$.
# 
# Calculations become much easier if we express the residual $D$ in terms of the deviations $D_X$ and $D_Y$.
# 
# $$
# \begin{align*} 
# D ~ &= ~ Y - \big{(} \hat{a}(X - \mu_X) + \mu_Y \big{)} \\
# &= ~ (Y - \mu_Y) - \hat{a}(X - \mu_X) \\
# &= ~ D_Y - \hat{a}D_X
# \end{align*}
# $$
# 
# Since $E(D_X) = 0 = E(D_Y)$, we have $E(D) = 0$. 
# 
# This is consistent with what you learned in [Data 8](https://www.inferentialthinking.com/chapters/15/6/Numerical_Diagnostics.html#Average-of-Residuals): No matter what the shape of the scatter diagram, the average of the residuals is $0$.
# 
# In our probability world, "no matter what the shape of the scatter diagram" translates to "no matter what the joint distribution of $X$ and $Y$". Remember that we have made no assumptions about that joint distribution.

# ### Mean Squared Error of Regression ###
# 
# The mean squared error of regression is $E\left( (Y - \hat{Y})^2 \right)$. That is just $E(D^2)$, the expected squared residual.
# 
# Since $E(D) = 0$, $E(D^2) = Var(D)$. So the mean squared error of regression is the variance of the residual. 
# 
# Let $r(X,Y) = r$ for short. To calculate the mean squared error of regression, recall that $\hat{a} = r\frac{\sigma_Y}{\sigma_X}$ and $E(D_XD_Y) = r\sigma_X\sigma_Y$. 
# 
# The mean squared error of regression is
# 
# $$
# \begin{align*}
# Var(D) ~ &= ~ E(D^2) \\
# &= ~ E(D_Y^2) - 2\hat{a}E(D_XD_Y) + \hat{a}^2E(D_X^2) \\
# &= ~ \sigma_Y^2 - 2r\frac{\sigma_Y}{\sigma_X}r\sigma_X\sigma_Y + r^2\frac{\sigma_Y^2}{\sigma_X^2}\sigma_X^2 \\
# &= ~ \sigma_Y^2 - 2r^2\sigma_Y^2 + r^2\sigma_Y^2 \\
# &= ~ \sigma_Y^2 - r^2\sigma_Y^2 \\
# &= ~ (1-r^2)\sigma_Y^2
# \end{align*}
# $$

# ### SD of the Residual ###
# The SD of the residual is therefore
# 
# $$
# SD(D) ~ = ~ \sqrt{1 - r^2}\sigma_Y
# $$
# 
# which is consistent with the [Data 8 formula](https://www.inferentialthinking.com/chapters/15/6/Numerical_Diagnostics.html#SD-of-the-Residuals).

# ### $r$ As a Measure of Linear Association ###
# 
# The expectation of the residual is always $0$. So if $SD(D) \approx 0$ then $D$ is pretty close to $0$ with high probability, that is, $Y$ is pretty close to $\hat{Y}$. In other words, if the SD of the residual is small, then $Y$ is pretty close to being a linear function of $X$. 
# 
# The SD of the residual is small if $r$ is close to $1$ or $-1$. The closer $r$ is to those extremes, the closer $Y$ is to being a linear function of $X$. If $r = \pm 1$ then $Y$ is a perfectly linear function of $X$.
# 
# A way to visualize this is that if $r$ is close to $1$ or $-1$, and you repeatedly simulate points $(X, Y)$, the points will lie very close to a straight line. In that sense $r$ is a measure of how closely the scatter diagram is clustered around a straight line.
# 
# The case $r=0$ is worth examining. In that case we say that $X$ and $Y$ are "uncorrelated". Because $\hat{a} = 0$, the equation of the regression line is simply $\hat{Y} = \mu_Y$. That's the horizontal line at $\mu_Y$; your prediction for $Y$ is $\mu_Y$ no matter what the value of $X$ is. The mean squared error is therefore $E\big{(}(Y-\mu_Y)^2\big{)} = \sigma_Y^2$, which is exactly what you get by plugging $r=0$ into the expression $(1 - r^2)\sigma_Y^2$.
# 
# This shows that when $X$ and $Y$ are uncorrelated there is no benefit in using linear regression to estimate $Y$ based on $X$. In this sense too, $r$ quantifies the amount of linear association between $X$ and $Y$. 
# 
# In exercises you will see that it is possible for $X$ and $Y$ to be uncorrelated and have a very strong *non-linear* association. So it is important to keep in mind that $r$ measures only linear association.

# ### The Residual is Uncorrelated with $X$ ###
# 
# In Data 8 you learned to perform some [visual diagnostics](https://www.inferentialthinking.com/chapters/15/5/Visual_Diagnostics.html#Visual-Diagnostics) on regression by drawing a *residual plot* which was defined as a scatter diagram of the residuals and the observed values of $X$. We said that residual plots are always flat: "the plot shows no upward or downward trend."
# 
# We will now make this precise by showing that the correlation between $X$ and the residual $D$ is 0.
# 
# By the definition of correlation, 
# 
# $$
# \begin{align*}
# r(D, X) ~ &= ~ E\Bigg( \left(\frac{D - \mu_D}{\sigma_D}\right)\left(\frac{X - \mu_X}{\sigma_X}\right) \Bigg) \\ \\
# &= ~ \frac{1}{\sigma_D\sigma_X}E(DD_X)
# \end{align*}
# $$
# 
# because $\mu_D = 0$. Therefore to show $r(D, X) = 0$, we just have to show that $E(DD_X) = 0$. Let's do that.
# 
# $$
# \begin{align*}
# E(DD_X) ~ &= ~ E((D_Y - \hat{a}D_X)D_X) \\
# &= ~ E(D_XD_Y) - \hat{a}E(D_X^2) \\
# &= ~ r\sigma_X\sigma_Y - r\frac{\sigma_Y}{\sigma_X}\sigma_X^2 \\
# &= ~ 0
# \end{align*}
# $$

# In[ ]:




