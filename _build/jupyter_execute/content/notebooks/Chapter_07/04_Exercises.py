#!/usr/bin/env python
# coding: utf-8

# ## Exercises ##

# **1.**
# Let $X$ and $Y$ be independent random variables such that
# 
# - $E(X) = 10$, $SD(X) = 3$
# - $E(Y) = -8$, $SD(Y) = 4$
# 
# Let $V = 5X - 2Y + 9$. Find $E(V)$, $Var(V)$, and $SD(V)$.

# **2.** A multiple choice test has 60 questions. Each question has three possible answers, one of which is correct. Let $R$ be the number of correct answers a student gets by guessing all the answers independently at random. Find $E(R)$ and $SD(R)$.

# **3.** In roulette, a bet on a "split" pays 17 to 1 and there are two chances in 38 to win. This means:
# 
# - Each time you bet on a split, your chance of winning is $2/38$ independently of all other times.
# - If you bet a dollar on a "split", then if you win the bet your net gain is $\$17$ and if you lose the bet your net gain is $-\$1$.
# 
# Suppose you bet on a split on each of 100 spins of the roulette wheel. Let $X$ be your total net gain on all 100 bets. 
# 
# **a)** Find $E(X)$ and $SD(X)$.
# 
# **b)** Find the chance that you come out ahead, that is, your total net gain is positive.

# **4.** 
# This exercise is about draws made at random with replacement from the integers $1, 2, \ldots, N$. It is the model we used for estimation in the [German tanks problem](http://stat88.org/textbook/notebooks/Chapter_05/04_Unbiased_Estimators.html).
# 
# **a)** In the special case $N = 6$, our model represents rolling a die. Let $X_1$ be the number of spots on one roll of a die. Find $E(X_1)$ and $Var(X_1)$.
# 
# **b)** The calculations in Part **a** can be generalized for $X_1$ uniformly distributed on $1, 2, \ldots, N$, to get $E(X_1) = (N+1)/2$ as you know, and $Var(X_1) = (N^2 - 1)/12$. The formula for variance follows by algebra that you don't have to do; you can just use the formula.
# 
# Now let $X_1, X_2, \ldots, X_n$ be draws at random with replacement from $1, 2, \ldots, N$, as in the German tanks problem. Denote the sample average by $\bar{X} = \frac{1}{n}\sum_{i=1}^n X_i$. Find $SD(\bar{X})$.
# 
# **c)** In the German tanks problem, we constructed $\hat{N} = 2\bar{X} - 1$ as an unbiased estimator of $N$. (Statisticians often use "hat" notation to represent estimators.) You know that $E(\hat{N}) = N$. Find $SD(\hat{N})$.
# 
# **d)** Explain how $\hat{N}$ becomes a better estimator of the population size $N$ as the sample size $n$ gets large.

# **5.** 
# The number of typos on the cover page of an exam has a distribution given by
# 
# |value|$0$|$1$|
# |----:|:---:|:---:|
# |**probability**|$0.8$|$0.2$|
# 
# The number of misprints in the rest of the exam has the Poisson $(3)$ distribution, independently of the cover page.
# 
# Find the expectation and SD of the total number of misprints on the exam.

# **6**. Let $X$ have the Poisson $(\mu)$ distribution. Let $Y$ have the Poisson $(\lambda)$ distribution and suppose $X$ and $Y$ are independent.
# 
# **a)** Use properties of expectation and variance to find $E(X+Y)$ and $SD(X+Y)$.
# 
# **b)** What is the distribution of $X+Y$? Check that your answer is consistent with your answer to Part **a**.

# **7.**
# A coin is tossed repeatedly. Find the expectation and SD of the number of tosses required to get a total of three heads.

# **8.**
# A randomized controlled experiment has 50 participants of whom 30 are men. A simple random sample of 25 participants is assigned to the treatment group and the rest to control.
# 
# Let $M_T$ be the number of men in the treatment group and let $M_C$ be the number of men in the control group.
# 
# **a)** Find $E(M_T)$ and $SD(M_T)$.
# 
# **b)** Find $E(M_C)$ and $SD(M_C)$.
# 
# **c)** True or false: $Var(M_T + M_C) = Var(M_T) + Var(M_C)$.

# **9.**
# In a country, State A has 40 million people and State B has 10 million people. The two states have the same proportion of college graduates.
# 
# In each of part below, pick one of the three options without calculation and explain your choice.
# 
# **a)** In each state, a simple random sample of 500 people is taken. The SD of the number of college graduates in the sample from State A is
# 
# **(i)** quite a bit less than
# 
# **(ii)** about the same as
# 
# **(iii)** quite a bit more than
# 
# the SD of the number of college graduates in the sample from State B.
# 
# **b)** In each state, a simple random sample of 0.01% of the population is taken. The SD of the number of college graduates in the sample from State A is
# 
# **(i)** quite a bit less than
# 
# **(ii)** about the same as
# 
# **(iii)** quite a bit more than
# 
# the SD of the number of college graduates in the sample from State B.

# **10.**
# A non-negative integer valued random variable has expectation 50 and SD 10. Could the random variable have a binomial distribution?

# **11.** 
# Each Data 8 student is asked to draw a random sample and estimate a parameter using a method that has chance 95% of resulting in a good estimate. 
# 
# Suppose there are 1300 students in Data 8. Let $X$ be the number of students who get a good estimate. Assume that all the students' samples are independent of each other. 
# 
# **a)** Find the distribution of $X$.
# 
# **b)** Find $E(X)$ and $SD(X)$.
# 
# **c)** Find the chance that more than 1250 students get a good estimate.

# **12.**
# In a population of size 100 there are 50 women, 20 unemployed people, and 80 college graduates. 
# 
# A simple random sample of 30 people is taken. In the sample, let $W$ be the number of women, $U$ the number unemployed, and $C$ the number of college graduates.
# 
# **a)** Without calculation (other than obvious conversions to percents or proportions), rank $E(W)$, $E(U)$, and $E(C)$ in increasing order. If you think two of the values are equal, put an $=$ sign between them.
# 
# **b)** Without calculation (other than obvious conversions to percents or proportions), rank $SD(W)$, $SD(U)$, and $SD(C)$ in increasing order. If you think two of the values are equal, put an $=$ sign between them.

# In[ ]:




