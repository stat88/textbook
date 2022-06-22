#!/usr/bin/env python
# coding: utf-8

# In[1]:


# NO CODE

from datascience import *
from prob140 import *
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
import numpy as np
from scipy import stats

import warnings
warnings.filterwarnings('ignore')


# ## A/B Testing: Fisher's Exact Test ##

# *A/B testing* is a term used to describe tests of hypotheses that involve comparing the distributions of two random samples. Although the term is relatively new, the ideas and methods have been used by statisticians for a very long time.
# 
# In this section we revisit a test of hypotheses performed in Data 8 using random permutations. We will show how the test can be performed using a method devised by Sir Ronald Fisher early in the 20th century.
# 
# Recall a [randomized controlled experiment](https://www.inferentialthinking.com/chapters/12/3/Causality.html) to study a potential treatment for chronic back pain. The treatment was the botulinum toxin A, a very potent toxin that can be used as medication in tiny doses.
# 
# A total of 31 patients participated in the study. Of these, a simple random sample of 15 were assigned to the treatment group and the remaining 16 to the control group. Eight weeks after treatment, 9 of the 15 in the treatment group had pain relief compared to 2 out of 16 in the control group.
# 
# In other words, of the 11 patients who had pain relief, 9 were in the treatment group and 2 in the control group. What does this tell us about the treatment?
# 
# We can answer this question by performing a test of hypotheses. In scientific experiments, the hypotheses must be posed before the experiment is run, so that they are not biased by the observed data. Therefore the hypotheses are:
# 
# - $H_0$: The treatment does nothing; any difference between the two groups is due to the random assignment of patients to treatment and control.
# 
# - $H_A$: The treatment does something. Note that the "something" could be good or bad; we are not specifying the nature of the effect.
# 
# These are the same hypotheses we tested in Data 8, and also the same as in the paper.
# 
# We now have to come up with a test statistic. It is natural to start by considering the number of treated patients who have pain relief. Let's call this number $X$. We might have to adjust it to get our test statistic, but let's see what we can say about it first.
# 
# We will start by finding the distribution of $X$ under $H_0$.
# 
# Under $H_0$, the treatment does nothing different from the control. So among the 31 patients in the study, 11 would have had pain relief anyway, regardless of the group to which they were assigned. Among those 11, $X$ would end up in the treatment group due to the random assignment of patients to groups.
# 
# The treatment group consists of a simple random sample of 15 of the 31 patients. Therefore under $H_0$, the distribution of $X$ is hypergeometric with the following parameters:
# 
# - N = 31, the population size
# - G = 11, the total number of "pain relief" patients
# - n = 15, the size of the treatment group
# 
# Therefore
# 
# $$
# E_{H_0}(X) ~ = ~ 15 \times \frac{11}{31} ~ \approx ~ 5.32
# $$
# 
# If the null hypothesis were true we would expect to get 5.32 "pain relief" patients in the treatment group. To distinguish between the null and alternative hypotheses, a good statistic to use is
# 
# $$
# T ~ = ~ \vert X - 5.32 \vert
# $$
# 
# This statistic $T$ is the distance between the observed count and the expected count under the null hypothesis. Large values of $T$ favor the alternative hypothesis.
# 
# The observed value of the test statistic is
# 
# $$
# \vert 9 - 5.32 \vert ~ = ~ 3.68
# $$
# 
# Therefore the $p$-value is
# 
# $$
# \begin{align*}
# P_{H_0}(T \ge 3.68) ~ &= ~ P(\vert X - 5.32 \vert \ge 3.68) \\
# &= ~ P(X \le 5.32 - 3.68) + P(X \ge 5.32 + 3.68) \\
# &= ~ P(X \le 1.64) + P(X \ge 9) \\
# &= ~ P(X \le 1) + P(X \ge 9) \\ \\
# &= ~ \sum_{g=0}^1 \frac{\binom{11}{g}\binom{20}{15-g}}{\binom{31}{15}} ~ + ~ \sum_{g=9}^{11} \frac{\binom{11}{g}\binom{20}{15-g}}{\binom{31}{15}} \\ \\
# &\approx ~ 0.00915
# \end{align*}
# $$

# In[2]:


sum(stats.hypergeom.pmf(make_array(0, 1, 9, 10, 11), 31, 11, 15))


# That's a very small $p$-value, which implies that the data support the alternative hypothesis more than they support the null. The conclusion is that treatment did something – it wasn't just the same as the control. 
# 
# This is consistent with the conclusion of the researchers and also with our own analysis in Data 8. But the approach to getting the $p$-value is different in the three analyses.
# 
# - The calculations in the research paper involve some approximations. The reported $p$-value is $0.009$.
# - In Data 8 we simulated the difference between the two group proportions under the null hypothesis, by pooling the two groups and randomly permuting the pooled sample. Our conclusion was based on an empirical, approximate $p$-value of $0.0085$.
# - Our calculation in this section requires neither simulation nor approximation and produces the exact $p$-value.
# 
# The method we have used is called *Fisher's exact test*. That's the same Sir Ronald Fisher who formalized tests of hypotheses, suggested cutoffs for $p$-values, and so on. The method can be used for any sample size and any randomized controlled experiment with a binary response.

# In[ ]:




