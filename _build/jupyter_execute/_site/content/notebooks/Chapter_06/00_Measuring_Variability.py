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


# # Measuring Variability #

# Expectation is the center of gravity of a probability histogram, and is thus a measure of where the histogram is located on the number line. But histograms of very different distributions can have the same expectation.
# 
# In the example below, both Distribution 1 and Distribution 2 balance at 3.5.

# In[2]:


# NO CODE

k = np.arange(1, 7)
unif = (1/6)*np.ones(6)
binom = stats.binom.pmf(np.arange(6), 5, 0.5)
ushaped = np.array([0.3, 0.1, 0.1, 0.1, 0.1, 0.3])

unif_dist = Table().values(k).probabilities(unif)
binom_dist = Table().values(k).probabilities(binom)
#ushaped_dist = Table().values(k).probabilities(ushaped)

Plots('Distribution 1', unif_dist, 'Distribution 2', binom_dist)


# The probabilities in Distribution 2 are more concentrated around the center of the distribution. So it seems *less spread out* than Distribution 1.
# 
# In this chapter we will quantify the spread or variability in a distribution. Once we have defined a measure of spread and examined how to calculate it, we will see what it tells us about the *tails* of the distribution, that is, probabilities of values that are far away from the expectation.
