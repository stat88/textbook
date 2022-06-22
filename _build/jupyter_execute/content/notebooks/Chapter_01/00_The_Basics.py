#!/usr/bin/env python
# coding: utf-8

# In[1]:


# HIDDEN
from datascience import *
from prob140 import *
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
import numpy as np


# # The Basics #

# This chapter sets out the rules of the game – the axioms on which the theory of probability is based. The axioms aren't laws of nature. They are minimal conditions outlined by probabilists to reflect some reasonable requirements about how probabilities should behave. It turns out that the simple set of axioms leads to a powerful theory that has an extraordinary range of application, some of which we will study in this course.
# 
# We will start out by examining our own intuition about probabilities as proportions, and then look at some ways in which proportions behave. This will help motivate the formal axioms and a few of their consequences.
# 
# Along the way we will also address a general problem that data scientists encounter frequently: What do we do if we are looking for a numerical answer to a question but don't have enough information to find it? Can we do better than just giving up and going away? 
# 
# In many situations there is indeed a better option. We will examine one of those situations and see what we can do to gain some insight even though we have incomplete information.

# In[ ]:




