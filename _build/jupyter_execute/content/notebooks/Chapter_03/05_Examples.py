#!/usr/bin/env python
# coding: utf-8

# In[1]:


# NO CODE

from prob140 import *
from datascience import *
import numpy as np
from scipy import stats

import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib
matplotlib.style.use('fivethirtyeight')


# ## Examples ##
# This section consists of an assortment of examples of the use of the binomial and hypergeometric distributions. In each example you will see some of the main problem solving techniques we have developed:
# 
# - Breaking the problem down into smaller pieces
# - Examining the assumptions and hence deciding which distributions can be used
# - Organizing the information to identify the parameters of the distributions
# - Partitioning events into component pieces
# - Using the addition and multiplication rules carefully

# ### Advisor Meetings ###
# An advisor at a university provides guidance to 10 students. Each student has to meet with her once a month during the school year which consists of nine months.
# 
# So each month the advisor schedules one day of meetings. Each student has to sign up for one meeting that day. Students have the choice of meeting her in the morning or in the afternoon.
# 
# Assume that every month each student, independently of other students and other months, chooses to meet in the afternoon with probability 0.75.
# 
# What is the chance that  she has both morning and afternoon meetings in all of the months except one?
# 
# **Answer:** First, let's just examine one particular month in the school year, say October. 
# 
# For the advisor to have both morning and afternoon afternoon meetings in October, some of the 10 students would have to choose the morning and others would have to choose the afternoon. This can happen in many ways, so let's see if the complement is easier.
# 
# The complement of "both morning and afternoon meetings" is "meetings only in the morning or only in the afternoon." The only ways that can happen is if all 10 students choose the morning or all 10 choose the afternoon. So, by the independence of the students' choices that month,
# 
# $$
# P(\text{both morning and afternoon meetings in October}) ~ = ~ 1 - \big{(} 0.25^{10} + 0.75^{10}) ~ \approx 94.37\%
# $$
# 
# Now let $X$ be the number of months in which this happens. Let the nine months be the trials. The students' choices are independent across months; success is having meetings both morning and afternoon; for each month, the chance of success is the answer above, which we will call $p$ for short.
# 
# Then $X$ has the binomial $(9, p)$ distribution and we want $P(X = 8)$. The answer is
# 
# $$
# P(X = 8) ~ = ~ \binom{9}{8} p^8 (1-p)^1 ~ \approx ~ 31.88\%
# $$

# In[2]:


p = 1 - (0.25**10 + 0.75**10)
p


# In[3]:


stats.binom.pmf(8, 9, p)


# ### Randomized Controlled Experiments ###
# Two randomized controlled experiments are being run independently of each other. In each experiment, a simple random sample of half the participants will be assigned to the treatment group and the other half to control.
# 
# Experiment 1 has 100 participants of whom 20 are men.
# 
# Experiment 2 has 90 participants of whom 30 are men.
# 
# **Question 1.** What is the chance that the treatment and control groups in Experiment 1 contain the same number of men?
# 
# **Answer:** Let $T_1$ be the number of men in the treatment group of Experiment 1.
# 
# The treatment group is a simple random sample of 50 participants drawn from all 100. For the two groups to have the same number of men, there must be 10 men in the treatment group. If we label men as the "good" elements, the distribution of $T_1$ is hypergeometric with parameters $N = 100$, $G = 20$, and $n = 50$.
# 
# The chance that the treatment group contains 10 men is therefore
# 
# $$
# P(T_1 = 10) ~ = ~ \frac{\binom{20}{10}\binom{80}{40}}{\binom{100}{50}} ~ \approx ~ 19.7\%
# $$

# In[4]:


stats.hypergeom.pmf(10, 100, 20, 50)


# **Question 2.** What is the chance that the treatment groups in the two experiments have the same number of men?
# 
# **Answer:** Let $T_2$ be the number of men in the treatment group of Experiment 2. Analogously to $T_1$, we can see that $T_2$ has the hypergeometric distribution with parameters $N = 90$, $G = 30$, and $n = 45$.
# 
# We want $P(T_1 = T_2)$. Partition the event into all the ways it can happen:
# 
# - $T_1 = 0, T_2 = 0$
# - $T_1 = 1, T_2 = 1$
# - $T_1 = 2, T_2 = 2$
# - ...
# - $T_1 = 20, T_2 = 20$
# 
# By the addition rule, $P(T_1 = T_2)$ is the sum of the chances of all these events.
# 
# The two experiments are independent. So for $0 \le g \le 20$,
# 
# $$
# P(T_1 = g, T_2 = g) ~ = ~ P(T_1 = g)P(T_2 = g) ~ = ~ \frac{\binom{20}{g}\binom{80}{50-g}}{\binom{100}{50}} \cdot \frac{\binom{30}{g}\binom{60}{45-g}}{\binom{90}{45}}
# $$
# 
# Hence
# 
# $$
# P(T_1 = T_2) ~ = ~ \sum_{g=0}^{20} \frac{\binom{20}{g}\binom{80}{50-g}}{\binom{100}{50}} \cdot \frac{\binom{30}{g}\binom{60}{45-g}}{\binom{90}{45}} ~ \approx ~ 3.37\%
# $$

# In[5]:


g = np.arange(21)
t1_probs = stats.hypergeom.pmf(g, 100, 20, 50)
t2_probs = stats.hypergeom.pmf(g, 90, 30, 45)

sum(t1_probs * t2_probs)


# ### Sampling from a State ###
# A state has several million households, half of which have annual incomes over 50,000 dollars. In a simple random sample of 400 households taken from the state, what is the chance that more than 215 have incomes over 50,000 dollars?
# 
# **Answer:** Think of a population whose elements are households in this state. We are counting successes where success is defined as an annual income of over 50,000 dollars. The sample is drawn without replacement, but we don't know the exact total number of households. Without the population size, we can't use the hypergeometric formula.
# 
# Does that mean we are stuck? No, because we can see that the sample size is small relative to the population size: 400 out of several million. In such a situation, sampling without replacement is very well approximated by sampling with replacement.
# 
# Since the draws are essentially independent, the number of successes $X$ can be thought of as a binomial $(400, 0.5)$ random variable because half the elements in the elements in the population are successes. The answer is
# 
# $$
# P(X > 215) = \sum_{k=216}^{400} \binom{400}{k}0.5^k0.5^{400-k} ~ = ~ 6.05\%
# $$

# In[6]:


sum(stats.binom.pmf(np.arange(216, 401), 400, 0.5))


# ### Assessing a Treatment ###
# In a randomized controlled experiment with 100 participants, 60 participants are in the treatment group and 40 are in the control group. In the treatment group, 50 out of the 60 participants recover after the treatment. In the control group, 30 out of the 40 participants recover.
# 
# This looks like evidence in favor of the treatment, as $5/6 \approx 83\%$ of the treatment group recovered compared to 75% of the control group.
# 
# As part of the assessement of whether the treatment was effective, data scientists pose the following question. Suppose the treatment had no special effect and in fact acted just like the control. Then the 80 patients who recovered would have recovered in whichever group they were placed. What is the chance that 50 or more of these 80 people were assigned to the treatment group just by chance?
# 
# The treatment group consists of a simple random sample of 60 draws from a population of 100. Designate the 80 recovered patients as good elements and let $X$ be the number of them who were assigned to the treatment group. Then $X$ has the hypergeometric $(100, 80, 60)$ distribution, and
# 
# $$
# P(X \ge 50) ~ = ~ \sum_{g=50}^{60} \frac{\binom{80}{g}\binom{20}{60-g}}{\binom{100}{60}} ~ \approx ~ 22\%
# $$

# In[7]:


sum(stats.hypergeom.pmf(np.arange(50, 61), 100, 80, 60))


# If the treatment did nothing more than the control, then there is about 22% chance that the recovery rates would appear to favor the treatment by at least as much as was observed. That's a pretty substantial chance. This is not very convincing evidence in favor of the treatment.
# 
# This way of assessing the treatment in a randomized controlled experiment is called *Fisher's Exact Test*. It is named after [Sir Ronald Fisher](https://en.wikipedia.org/wiki/Ronald_Fisher) who introduced the way statistical hypotheses are tested. In his first paper on this topic, he performed this test using data from an experiment in which he had served [randomized cups of tea](https://en.wikipedia.org/wiki/Lady_tasting_tea) to a lady who claimed she could tell if the milk or the tea had been added first in the cup. 

# In[ ]:




