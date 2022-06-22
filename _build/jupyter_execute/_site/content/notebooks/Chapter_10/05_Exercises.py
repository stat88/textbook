#!/usr/bin/env python
# coding: utf-8

# ## Exercises ##

# **1.**
# Let $X_1, X_2, X_3, \ldots $ be i.i.d. with density given by
# 
# $$
# f(x) ~ = ~
# \begin{cases}
# 0 ~~~~~~~ x \le 50 \\
# \frac{c}{x^4} ~~~~~~ x > 50
# \end{cases}
# $$
# 
# This is one of the *Pareto* densities, sometimes used in economics to represent distributions of wealth in populations where a small percent of the population owns a large percent of the wealth.
# 
# **a)** Find $c$.
# 
# **b)** Find the cdf of $X_1$ and sketch its graph.
# 
# **c)** Find $E(X_1)$.
# 
# **d)** Find $Var(X_1)$.
# 
# **e)** Let $\bar{X}_{(n)} = \frac{1}{n}\sum_{i=1}^n X_i$. Find or approximate $P(\bar{X}_{(100)} > 70)$.

# **2.**
# A class starts at 3:10 p.m. Seven students in the class arrive at random times $T_1, T_2, \ldots, T_7$ that are i.i.d. with the uniform distribution on the interval 3:07 to 3:12.
# 
# **a)** Find $E(T_1)$.
# 
# **b)** What is the chance that all seven students arrive before 3:10?
# 
# **c)** Let $X = \max(T_1, T_2, \ldots, T_7)$ be the time when the last of the seven students arrives. Find the cdf of $X$.

# **3.**
# Let $X$ have the exponential distribution with mean 24 hours. Assume that $X$ is measured in hours.
# 
# **a)** Find $P(X > 72)$.
# 
# **b)** Find $P(X > 72 \mid X > 24)$.

# **4.** 
# Strontium 90 has a half-life of 28.8 years. Assuming exponential decay, about how many years will it take for $2/3$ of a lump of Strontium 90 to decay?

# **5.**
# The weights of five randomly sampled people are i.i.d. normally distributed random variables with mean 150 pounds and SD 20 pounds. Let $W$ be the total weight of the five people, measured in pounds. If possible, find $w$ such that $P(W > w) = 0.05$. If this is not possible, explain why not.
# 

# **6.** 
# A random variable $X$ is normally distributed. The 25th percentile of the distribution is 120 and the 75th percentile is 147. Find the 90th percentile. [Use any method, but it's worth seeing if you can solve the problem without using the mean.]

# **7.** A simple random sample of 200 students is taken at University A. Independently, a simple random sample of 300 students is taken at University B.
# 
# - The number of football games watched by students in Sample A has an average of 1.5 and an SD of 2. The number of football games watched by students in Sample B has an average of 4 and and SD of 1.5.
# - 20% of the students in Sample A are football fans, whereas 50% of the students in Sample B are football fans.
# 
# In what follows, define "difference" to be "Quantity in B minus Quantity in A". Note that this not an absolute difference; it is allowed to be negative.
# 
# **a)** Construct an approximate 95% confidence interval for the difference between the average number of football games watched by students in the two universities.
# 
# **b)** Construct an approximate 95% confidence interval for the difference between the proportions of football fans in the two universities.
# 

# **8.**
# A simple random sample of 500 students is taken at University A. Independently, a simple random sample of 700 students is taken at University B.
# 
# In the sample from University A, 20% of the students are Economics majors. In the sample from University B, 16% of the students are Economics majors.
# 
# Is this difference due to chance? Or does University A have a higher percent of Economics majors?
# 
# Answer this by performing a test of hypotheses at the 5% level. Your answer should include a null hypothesis in terms of random variables, an appropriate alternative hypothesis, a test statistic, a $p$-value, and a conclusion, along with justifications of all of these.

# **9.**
# The heights of two men drawn at random from a population are i.i.d. normal with mean 68 inches and SD 3 inches. Find the chance that one of the men is more than four inches taller than the other.

# **10.**
# Let $U$ have the uniform distribution on the interval $(0, 1)$. Let $V = -\frac{1}{5}\log(U)$.
# 
# **a)** What are the possible values of $V$?
# 
# **b)** Find the cdf of $V$. Be careful about minus signs and directions of inequalities. [Section 10.2](http://stat88.org/textbook/notebooks/Chapter_10/02_Expectation_and_Variance.html) has the cdf of $U$.
# 
# **c)** Use Part **b** to identify the distribution of $V$.

# **11.**
# Scores on a test are normally distributed. The 80th percentile is 15 points higher than the 70th percentile.
# 
# True or false (explain):
# 
# The 90th percentile is 15 points higher than the 80th percentile.

# **12.** 
# In a simple random sample of 100 students taken in School A, the average GPA is 3.2 and the SD is 0.5. In a simple random sample of 150 students taken at School B, the average GPA is 3.4 and the SD is 0.3. You can assume that the samples from the two schools are independent of each other.
# 
# Is this just chance variation? Or are the average GPAs different in the two schools?
# 
# Answer this by performing a test of hypotheses at the 5% level. Your answer should include a null hypothesis in terms of random variables, an appropriate alternative hypothesis, a test statistic, a $p$-value, and a conclusion, along with justifications of all of these.

# In[ ]:




