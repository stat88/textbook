#!/usr/bin/env python
# coding: utf-8

# ## Bounds on Correlation ##

# For a random pair $(X, Y)$, the correlation $r(X, Y)$ is defined as
# 
# $$
# r(X, Y) ~ = ~ E\Bigg( \left(\frac{X-\mu_X}{\sigma_X}\right)\left(\frac{Y-\mu_Y}{\sigma_Y}\right) \Bigg) ~ = ~ E(X^*Y^*)
# $$
# 
# where $X^*$ and $Y^*$ are respectively $X$ and $Y$ measured in standard units.
# 
# Thus by definition, correlation is a pure number and has no units.
# 
# You have seen several properties of correlation in Data 8. Some are obvious, such as $r(X, Y) = r(Y, X)$. Some require proof.
# 
# In this brief section we will prove one principal property, which is that correlation is a number between $-1$ and $1$. You will prove a few other properties in exercises. In the next section we will specify the sense in which correlation measures clustering about a straight line.

# ### Lower Bound ###
# As a preliminary, recall that
# 
# $$
# E(X^*) = 0, ~~~ Var(X^*) = 1 = E\left({X^*}^2\right)
# $$
# 
# So also $E(Y^*) = 0$ and $E\left({Y^*}^2\right) = 1$. 
# 
# We know the expected squares, and what we need is a bound on the expected product $E(X^*Y^*)$. A result that connects the squares and the product of two numbers is $(a+b)^2 = a^2 + 2ab + b^2$.
# 
# So let's find $E\left((X^* + Y^*)^2\right)$ and see what that gives us.
# 
# $$
# \begin{align*}
# E\left((X^* + Y^*)^2\right) ~ &= ~ E\left({X^*}^2\right) + 2E(X^*Y^*) + E\left({Y^*}^2\right) \\
# &= ~ 2 + 2E(X^*Y^*)
# \end{align*}
# $$
# 
# Since $E\big{(}(X^* + Y^*)^2\big{)} \ge 0$, we have
# 
# $$
# 2 + 2E(X^*Y^*) \ge 0
# $$
# 
# which is the same as
# 
# $$
# E(X^*Y^*) \ge -1
# $$

# ### Upper Bound ###
# Play the same game with $E\big{(}(X^* - Y^*)^2\big{)}$ to see that
# 
# 
# $$
# 2 - 2E(X^*Y^*) \ge 0
# $$
# 
# which is the same as
# 
# $$
# E(X^*Y^*) \le 1
# $$
# 
# because division by $-2$ flips the direction of the inequality.

# ### Other Properties ###
# 
# As you know from Data 8, correlation measures linear association. In exercises you will show that if $Y$ is a linear function of $X$ then $r(X, Y)$ is either $1$ or $-1$.
# 
# You will also find the relation between $r(X, Y)$ and $r(X, W)$ where $W$ is a linear function of $Y$.
# 
# In the next section we will return to regression and formalize the idea that correlation measures clustering about a straight line. Our result will imply that if $r(X, Y)$ is either $1$ or $-1$, then the relation between $X$ and $Y$ must be perfectly linear.

# In[ ]:




