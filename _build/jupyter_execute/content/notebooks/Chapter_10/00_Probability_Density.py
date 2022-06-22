#!/usr/bin/env python
# coding: utf-8

# # Probability Density #

# We have used the normal curve as a mathematical function that approximates many discrete probability histograms. In the process, we have treated it very much like a discrete probability histogram, with areas under the curve representing probabilities. 
# 
# In fact, we can view the normal curve as a probability distribution in its own right, not just as an approximation to discrete distributions. This chapter formalizes what that means.
# 
# Discrete random variables have a finite number of possible values, or an infinite sequence of values indexed by $1, 2, 3, \ldots $. The probabilities in a discrete distribution are like masses attached to each possible value, which is why a discrete distribution is sometimes called a probability mass function (pmf) as you have seen in the `stats` module of `SciPy`.
# 
# Other random variables have an interval of possible values, such as the unit interval $(0, 1)$ or the whole number line, and probabilities that are smeared over the entire interval instead of being distributed in discrete lumps. For example, a random variable $Z$ has the *standard normal* distribution if its possible values are the entire number line and its probabilities are distributed according to the standard normal curve $\phi$.
# 
# This chapter makes this idea precise and shows how to work with such random variables. They are widely used for modeling variables such as time, distance, "noise" or errors, and so on, and are thus of great importance in data science.
# 
# The probability distribution of such a random variable can be represented by a curve instead of a discrete histogram with bars. The curve is called a *probability density function*. We will start the chapter by examining what density means in this context, and then develop ways of calculating the expectation and variance of a random variable that has a density function. The calculations are parallel to those in the discrete case, except that we will use integrals instead of sums.
