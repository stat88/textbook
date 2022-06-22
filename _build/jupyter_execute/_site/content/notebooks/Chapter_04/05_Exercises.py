#!/usr/bin/env python
# coding: utf-8

# ## Exercises ##

# **1.** At rush hour, passengers in a subway station come down an escalator to the platforms and choose either the Eastbound or the Westbound platform. Assume that each passenger chooses the Eastbound platform with chance 0.8 independently of all other passengers.
# 
# Suppose you start watching the escalator at the start of rush hour.
# 
# **a)** Find the chance that the first passenger to choose the Westbound platform is the fifth passenger that you see.
# 
# **b)** Find the chance that more than 15 passengers choose the Eastbound platform before the first one who chooses the Westbound platform.

# **2.** A random variable $W$ has the distribution shown in the table below. Sketch a graph of the cdf of $W$. 
# 
# |$~~~~~~~~~~~~~~~~~~~~~w$|$-2$ |$-1$|$0$|$1$|$3$|
# |----------------:|:---:|:---:|:---:|:---:|:---:|
# |$P(W = w)$|$0.1$|$0.3$|$0.25$|$0.2$|$0.15$|

# **3**.
# In a population, 30% of the individuals are green and the rest are blue. Suppose you draw individuals at random with replacement till both colors have appeared. Find the chance that you draw 10 times.

# **4.**
# In a "best of seven" sports series, Team A plays Team B until one team has won four games. That team wins the series. Assume that in each game Team A has chance 0.8 of winning, independently of other games.
# 
# **a)** Find the chance that there is a "sweep", that is, one team wins the first four games.
# 
# **b)** Find the chance that the series lasts more than five games.
# 
# **c)** Find the chance that the series lasts six games and Team A wins it.
# 
# **d)** Find the chance that Team A wins the series.

# **5.**
# Cards are dealt one by one at random without replacement till the fourth ace appears. Let $X$ be the number of cards dealt. 
# 
# **a)** Find $P(X = 39)$.
# 
# **b)** Find $P(X > 20)$.

# **6.**
# Each time I play the lottery, I have chance $1/2n$ of winning, independently of other times. Suppose I play $n$ times. For large $n$, find an approximate numerical value of the chance that I win at least once. Your answer should not involve $n$.

# **7.**
# A book has 20 chapters. In each chapter the number of misprints has the Poisson distribution with parameter 2, independently of the misprints in other chapters.
# 
# **a)** Find the chance that Chapter 1 has more than two misprints.
# 
# **b)** Find the chance that the book has no misprints.
# 
# **c)** Find the chance that two of the chapters have three misprints each.

# **8.** In the first hour that a bank opens, the customers who enter are of three kinds: those who only require teller service, those who only want to use the ATM, and those who only require special services (neither the tellers nor the ATM). Assume that the numbers of customers of the three kinds are independent of each other and also that:
# 
# - the number that only require teller service has the Poisson (6) distribution,
# - the number that only want to use the ATM has the Poisson (2) distribution, and
# - the number that only require special services has the Poisson (1) distribution.
# 
# Suppose you observe the bank in the first hour that it opens. In each part below, find the chance of the event described.
# 
# **a)** 12 customers enter the bank
# 
# **b)** more than 12 customers enter the bank
# 
# **c)** customers do enter but none requires special services

# **9.** On each spin of a roulette wheel, a gambler bets on a "single number". The chance that the gambler wins the bet on a spin is $1/38$ independently of all other spins.
# 
# Suppose the gambler keeps making this bet until he has won six times. Let $X$ be the number of spins required. Find the cdf of $X$. Your answer should be a formula for the function.

# **10**. 
# Suppose you are running independent success/failure trials with probability 0.7 of success on each trial. Find the chance that you get 10 failures before the 15th success.

# **11.** 
# A courtyard is paved with 100 identical tiles. In an instant of rain, the number of raindrops on each tile has the Poisson (10) distribution independently of all other tiles.
# 
# Find the chance that more than 90 tiles have more than 5 raindrops on them.

# **12.** 
# Each Cal Cookie contains random amounts of blue M&Ms and gold M&Ms. No other color is allowed.
# 
# In one cookie, let $N_b$ be the number of blue M&Ms and $N_g$ the number of gold M&Ms. Let $M = N_b + N_g$ be the total number of M&Ms in the cookie. 
# 
# Suppose that $N_b$ and $N_g$ are independent and that each has the Poisson (4) distribution.
# 
# **a)** Find $P(N_b = 3 \mid M = 10)$.
# 
# **b)** Fill in the blanks with the name of a distribution and its parameters. Explain your answers.
# 
# Given $M = 10$, $N_b$ has the $\underline{~~~~~~~~~~~~~~~~~~~~~~~~~}$ distribution with parameters $\underline{~~~~~~~~~~~~~~~~~~~~~~~~~}$.
