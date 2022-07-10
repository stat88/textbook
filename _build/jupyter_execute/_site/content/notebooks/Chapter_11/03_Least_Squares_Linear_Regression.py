#!/usr/bin/env python
# coding: utf-8

# ## Least Squares Linear Regression ##

# The mean squared error is a criterion by which you can compare two estimators – the one with the smaller mean squared error is on average closer to the quantity you are trying to estimate. An important use of this criterion is to identify the best among a class of estimators.
# 
# For example, suppose you have a random pair $(X, Y)$ and you want to use a linear function of $X$ to estimate $Y$. That is, you want to estimate $Y$ by the function $aX + b$ for some slope $a$ and intercept $b$. Your goal is to find the best in the class of all linear functions. If the criterion is mean squared error, the goal is to see if there is a slope and an intercept that minimize the mean squared error.
# 
# This is the [regression](https://www.inferentialthinking.com/chapters/15/2/Regression_Line.html) problem from Data 8, expressed in random variable notation. Recall that in Data 8 you were given formulas for the [slope and intercept](https://www.inferentialthinking.com/chapters/15/2/Regression_Line.html#The-Equation-of-the-Regression-Line) of the "best" or "least squares" line, also known as the regression line. In Data 8 notation the formulas are:
# 
# $$
# \text{slope of the regression line} ~ = ~ r \frac{\text{SD of }y}{\text{SD of }x}
# $$
# 
# where $r$ is the correlation between the two variables (which we have not yet defined in this course), and
# 
# $$
# \begin{align*}
# &\text{intercept of the regression line} \\
# &= ~ \text{(average of }y\text{)} - \text{slope}\times\text{(average of }x\text{)}
# \end{align*}
# $$
# 
# Data 8 gives you two ways of confirming that the formulas work:
# 
# - By the [geometry](https://www.inferentialthinking.com/chapters/15/2/Regression_Line.html#Identifying-the-Line-in-Standard-Units) of elliptical or "football shaped" scatter diagrams
# - By [numerical minimization](https://www.inferentialthinking.com/chapters/15/3/Method_of_Least_Squares.html#Minimizing-the-Root-Mean-Squared-Error) of the mean squared error over all possible lines
# 
# We will now derive the formulas mathematically using calculus and properties of expectation and variance. 
# 
# First, some notation:
# 
# - $E(X) = \mu_X$, $SD(X) = \sigma_X$
# - $E(Y) = \mu_Y$, $SD(Y) = \sigma_Y$
# 
# Also, some terminology: statistics that we have been calling "estimators" can also be called "predictors" depending on the context. Data 8 calls the regression estimate a regression prediction, and we will do that too.

# ### Mean Squared Error ###
# For the random point $(X, Y)$, the mean squared error of a linear predictor of $Y$ based on $X$ depends on the slope $a$ and intercept $b$ of the line used. So let us define $MSE(a, b)$ to be the mean squared error when we use the line $aX + b$ to predict $Y$. That is,
# 
# $$
# MSE(a, b) ~ = ~ E\big{(} (Y - (aX+b))^2 \big{)}
# $$
# 
# We have to find the values of $a$ and $b$ that minimize this function. We will do that by calculus, in two stages.

# ### Best Intercept for a Fixed Slope ###
# First, we will fix the slope and find the best intercept for that slope. The error can be rewritten as follows:
# 
# $$
# Y - (aX+b) ~ = ~ (Y-aX) - b
# $$
# 
# For a fixed $a$, let $MSE_a(b) = MSE(a, b)$ be considered as a function of $b$ alone. Then
# 
# $$
# \begin{align*}
# MSE_a(b) ~ &= ~ E\big{(} ((Y-aX) - b)^2 \big{)} \\
# &= ~ E\big{(} (Y-aX)^2 - 2b(Y-aX) + b^2 \big{)} \\
# &= ~ E\big{(} (Y-aX)^2\big{)} -2bE(Y-aX) + b^2
# \end{align*}
# $$
# 
# Now
# 
# $$
# \frac{d}{db}MSE_a(b) ~ = ~ -2E(Y-aX) + 2b
# $$
# 
# Set this equal to $0$ and solve to see that the best intercept $\hat{b}_a$ for the fixed slope $a$ is given by
# 
# $$
# \hat{b}_a ~ = ~ E(Y-aX) ~ = ~ \mu_Y - a\mu_X
# $$
# 
# This is consistent with the formula for the intercept of the regression line in Data 8:
# 
# $$
# \begin{align*}
# &\text{intercept of the regression line} \\
# &= ~ \text{(average of }y\text{)} - \text{slope}\times\text{(average of }x\text{)}
# \end{align*}
# $$
# 
# To be very thorough, we should take the second derivative, look at its sign, and confirm that we have a minimum rather than a maximum value of the mean squared error. But we will spare ourselves that calculation. We have enough experience from Data 8 to know that this is a minimum, not a maximum.

# ### Best Slope ###
# We now have to find the best among all slopes. For each fixed slope $a$ we must first plug in the best intercept we just found. Then the error in the prediction can be written as
# 
# $$
# \begin{align*}
# Y - (aX+\hat{b}_a) ~ &= Y - (aX + \mu_Y - a\mu_X) \\
# &= ~ (Y-\mu_Y) - a(X-\mu_X) \\
# &= D_Y - aD_X
# \end{align*}
# $$
# 
# where $D_X$ and $D_Y$ are the deviations of $X$ and $Y$ from their respective means.
# 
# We have to minimize
# 
# $$
# \begin{align*}
# MSE(a) ~ &= ~ E\big{(} (D_Y - aD_X)^2 \big{)} \\
# &= ~ E(D_Y^2) -2aE(D_XD_Y) + a^2E(D_X^2) \\
# &= ~ \sigma_Y^2 -2aE(D_XD_Y) + a^2\sigma_X^2
# \end{align*}
# $$
# 
# by the definition of variance. Now
# 
# $$
# \frac{d}{da}MSE(a) ~ = ~ -2E(D_XD_Y) + 2a\sigma_X^2
# $$
# 
# Set this equal to $0$ and solve to see that the best slope is
# 
# $$
# \hat{a} ~ = ~ \frac{E(D_XD_Y)}{\sigma_X^2} ~ = ~ \frac{E\big{(}(X-\mu_X)(Y-\mu_Y)\big{)}}{\sigma_X^2}
# $$
# 
# This doesn't look like the Data 8 formula for the slope of the regression line, but it is the way the slope of the regression line is often written. Let's see if we can make it resemble the Data 8 formula.

# ### Correlation ###
# The expected product $E(D_XD_Y)$ is called the *covariance* of $X$ and $Y$. Covariance is difficult to interpret because it has strange units. For example, if we were using educational level to predict income, then the covariance could be measured in units of years$\times$dollars, which is hard to understand. 
# 
# One way to deal with this problem is to first divide each deviation by the corresponding SD, to get a pure number. This converts each variable to standard units. The expected product of standard units is called the *correlation coefficient* of $X$ and $Y$, or just correlation for short. We will denote it by $r(X, Y)$ or just $r$.
# 
# $$
# r ~ = ~ r(X, Y) ~ = ~ E\Big{(} \big{(}\frac{X - \mu_X}{\sigma_X}\big{)}\big{(}\frac{Y - \mu_Y}{\sigma_Y}\big{)} \Big{)}
# $$
# 
# This agrees with the [Data 8 definition](https://www.inferentialthinking.com/chapters/15/1/Correlation.html#Calculating-$r$) of correlation, which says, "$r$ is the average of the products of the two variables, when both variables are measured in standard units."
# 
# We now have
# 
# $$
# E(D_XD_Y) ~ = ~ E\big{(}(X-\mu_X)(Y-\mu_Y)\big{)} ~ = ~ r\sigma_X\sigma_Y
# $$

# ### A Familiar Formula for the Best Slope ###
# The best slope can be written as
# 
# $$
# \hat{a} ~ = ~ \frac{E(D_XD_Y)}{\sigma_X^2} ~ = ~ \frac{r\sigma_X\sigma_Y}{\sigma_X^2} ~ = ~ r\frac{\sigma_Y}{\sigma_X}
# $$
# 
# which is the same as the Data 8 formula for the slope of the regression line.

# ### Equation of the Regression Line ###
# We have shown that no matter what the joint distribution of the pair $(X, Y)$, there is a unique straight line that minimizes the mean squared error of prediction among all straight lines. This line is called the *regression line*, for reasons that you know from Data 8.
# 
# The equation of the regression line is
# 
# $$
# \hat{Y} ~ = ~ \hat{a}X + \hat{b}
# $$
# 
# where:
# 
# - $\hat{Y}$ is the regression prediction of $Y$ based on $X$, also known as the *fitted value* of $Y$
# - the slope of the regression line is $\hat{a} = r\frac{\sigma_Y}{\sigma_X}$
# - the intercept of the regression line is $\hat{b} = \mu_Y - \hat{a}\mu_X$
# 
# Sometimes it is useful to write the regression equation in a different form:
# 
# $$
# \hat{Y} ~ = ~ \hat{a}X + \mu_Y - \hat{a}\mu_X
# ~ = ~ \hat{a}(X - \mu_X) + \mu_Y
# $$
# 
# This form can reduce calculation because $E(X - \mu_X) = 0$ and $Var(X - \mu_X) = Var(X) = \sigma_X^2$. We will use it in later sections to study the error in the regression prediction.
