#!/usr/bin/env python
# coding: utf-8

# # Random Counts #

# The number of people who will vote for a Presidential candidate, the number of treated patients who recover, the number of correct predictions made by a sports journalist – all of these are example of *counts*. Random counts occur commonly in data science. Understanding them not only helps answer questions about the situations in which they arose but also helps us understand more complicated random quantities.
# 
# In this chapter we will start out with random counts that seem unlikely. We will then develop some general terminology and notation for dealing with random quantities that have numerical values. Our main examples will be random counts when sampling with and without replacement.

# ### Arranging in a Line ###
# It will help to review some of the math involved in counting. Let $n$ be a positive integer and suppose you have a set of $n$ elements. 
# 
# Let $k$ be a fixed integer such that $1 \le k \le n$. 
# 
# By the product rule of counting, the number of ways in which you can arrange $k$ of the $n$ elements in a line is $n(n-1)(n-2) \cdots (n-k+1)$.
# 
# If $k = n$, this is the same as arranging all $n$ elements in a line. Plug $k = n$ into the expression above to see that the number of ways of arranging $n$ elements in a line is $n!$. These are called *permutations* of the $n$ elements.

# ### Choosing Subsets ###
# Suppose now that you want to select $k$ elements from among the $n$ but you are not interested in the order in which they appear. This happens for example when you deal a hand of cards: you hand is the *subset* or group of cards that you got. Subsets are not ordered.
# 
# The number of different subset of $k$ elements that you can create out of $n$ elements is the number $\binom{n}{k}$, read as "$n$ choose $k$".
# 
# For $k \ge 1$, a good way to remember this number is
# 
# $$
# \binom{n}{k} ~ = ~ \frac{n(n-1)(n-2) \ldots (n-k+1)}{k!}
# $$
# 
# Notice that $\binom{n}{n} = 1$. There is only one way to choose a set of $n$ elements out of $n$: choose them all.
# 
# The calculation says that you can start by pulling out $k$ elements and arranging them in a line; the number of ways to do that is the numerator above. But you can't just stop there. All $k!$ ways of permuting those same $k$ elements give you the same subset, but the numerator counts them all as different arrangements. In other words, the numerator counts every subset consisting of $k$ elements not once but $k!$ times. You only want to count each subset once. Dividing by $k!$ solves this problem.
# 
# There is another way to remember $\binom{n}{k}$. This way is not great for numerical computation because factorials get very large. But it's a clean formula and sometimes helpful in algebraic calculations.
# 
# $$
# \binom{n}{k} ~ = ~ \frac{n!}{k!(n-k)!}
# $$
# 
# It is easy to see by algebra that the two expressions for $\binom{n}{k}$ give the same answer. 
# 
# One nice consequence of the second representation is that it can also be used when $k=0$ and gives the natural answer $\binom{n}{0} = 1$. There is only one way to choose 0 elements out of $n$: do nothing. 
# 
# Recall that $0!$ is defined to be 1. That's to make the formula above work out.
# 
# The numbers $\binom{n}{k}$ appear in many calculations.
# 
# - They are the elements of [Pascal's Triangle](https://en.wikipedia.org/wiki/Pascal%27s_triangle).
# - They are the coefficients in the [expansion](https://en.wikipedia.org/wiki/Binomial_theorem) of $(a + b)^n$. Try it out for $n = 2$ and see!
# 
# For our purposes, the main property of $\binom{n}{k}$ is that it is the number of ways you can choose a subset of $k$ elements out of a set of $n$.

# In[ ]:




