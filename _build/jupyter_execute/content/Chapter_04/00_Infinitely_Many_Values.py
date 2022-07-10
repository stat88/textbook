#!/usr/bin/env python
# coding: utf-8

# # Infinitely Many Values #

# The random variables we have studied thus far have had a finite number of possible values. For example, a random variable that has the binomial $(100, 0.5)$ distribution can be no bigger than 100.
# 
# Much of data science involves large random samples. If you think of $n$ as a sample size, then natural questions arise about the properties of the sample when $n$ is large. To answer these questions, it helps to think about the sample size $n$ tending to infinity. That usually involves imagining an arbitrarily large set of possible values.
# 
# This leads naturally to thinking about random variables that have infinitely many values. Many such random variables arise in practice. For example, if you toss a coin repeatedly and note down how many times you have to toss till you see heads for the first time, the number that you note down can be arbitrarily large because you can get any finite number of tails in a row.
# 
# This chapter introduces some random variables that have infinitely many possible values. To study them, it helps to have a new way of specifying distributions. We introduce this first, and then look at examples of some random variables that have infinitely many values and are used frequently in applications.

# <h3> IID Trials </h3>
# The primary setting that we will use in the chapter is that of a sequence of independent repeated trials. The outcome of each trial has the same distribution as the outcome of every other trial, so we say that the trials are identically distributed.
# 
# "Independent and identically distributed" has too many syllables for comfort, so it is abbreviated to *i.i.d.* which is one of the most heavily used acronyms in probability theory.
# 
# Sequences of coin tosse are i.i.d. trials, as are sequences of rolls of a die, or samples drawn with replacement.

# In[ ]:




