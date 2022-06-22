#!/usr/bin/env python
# coding: utf-8

# ## Conditional Expectation ##

# As our course begins to move towards estimation and prediction, it is a good idea to formalize some ways of quantifying how one variable is related to another. We are going to want to use information given about one variable to predict the unknown value of another.
# 
# In the language of random variables, "information given about one variable" is conditioning, of course. You have been calculating conditional probabilities and conditional distributions for some time now. We will start this section with a formal definition of a conditional distribution, though you can continue to work with your intuitive sense of what that is if you prefer.
# 
# Here is an example followed by the definition. After that, we will define conditional expectation.

# ### Conditional Distribution ###
# Let $X$ and $Y$ be i.i.d., and suppose $X$ has the distribution given below.
# 
# |$~~~~~~~~~~~~~~~~~x$| $1$ | $2$ | $3$ |
# |---:|:---:|:---:|:---:|
# |$P(X = x)$|$0.25$|$0.5$|$0.25$|
# 
# Let $S = X+Y$.
# 
# The joint distribution of $X$ and $S$ is the set of all possible values $(x, s)$ of the pair $(X, S)$, along with all the probabilities $P(X = x, S = s)$. 
# 
# An example of the probability calculations:
# 
# $$
# P(X = 2, S = 3) ~ = ~ P(X = 2, Y = 1) ~ = ~ 0.5 \times 0.25 ~ = ~ 0.125
# $$
# 
# As usual, we will display the joint distribution in a table.
# 
# |$~~~~~~~~~~~~~~~~~~~~~~$| $X = 1$ | $X = 2$ | $X = 3$ |
# |:---------------:|:---|:---|:---|
# |$S = 2$|$~~~~~0.0625~~~~~$|$~~~~~~0~~~~~~$|$~~~~~~0~~~~~~$|
# |$S = 3$|$~~~~~0.125~~~~~$|$~~~~~0.125~~~~~$|$~~~~~~0~~~~~~$|
# |$S = 4$|$~~~~~0.0625~~~~~$|$~~~~~0.25~~~~~$|$~~~~~0.0625~~~~~$|
# |$S = 5$|$~~~~~~0~~~~~~$|$~~~~~0.125~~~~~$|$~~~~~0.125~~~~~$|
# |$S = 6$|$~~~~~~0~~~~~~$|$~~~~~~0~~~~~~$|$~~~~~~0.0625~~~~~~$|
# 
# Recall that summing along the rows will give us the distribution of $S$:
# 
# |$~~~~~~~~~~~~~~~~~s$| $2$ | $3$ | $4$ | $5$ | $6$ |
# |---:|:---:|:---:|:---:|:---:|:---:|
# |$P(S = s)$|$0.0625$|$0.25$|$0.375$|$0.25$|$0.0625$|
# 
# Now suppose someone runs the experiment and tells you that $S = 3$. Given this information, what is the distribution of $X$?
# 
# Given $S=3$, you can ignore all the rows of the table except the one corresponding to $S = 3$. 
# 
# The probabilities in that row don't form a probability distribution, because they don't sum to 1. But it's clear by looking at the row that given the sum $S = 3$, the first draw is equally likely to be 1 or 2. 
# 
# To turn the row into a probability distribution, we have to divide each element by the sum of the row. We'll get the same answer in the first two cells, and the third will be 0.
# 
# The calculation for the first cell is
# 
# $$
# P(X = 1 \mid S = 3) ~ = ~ \frac{P(X = 1, S = 3)}{P(S = 3)} ~ = ~ 
# \frac{0.125}{0.25} ~ = ~ 0.5
# $$
# 
# By analogous calculations in all the cells, we get one *conditional distribution* in each row:
# 
# |$~~~~~~~~~~~~~~~~~~~~~~$| $X = 1$ | $X = 2$ | $X = 3$ |
# |:---------------:|:---|:---|:---|
# |Conditional distribution of $X$ given $S = 2$|$~~~~~1~~~~~$|$~~~~~0~~~~~$|$~~~~~~0~~~~~~$|
# |Conditional distribution of $X$ given $S = 3$|$~~~~~0.5~~~~~$|$~~~~~0.5~~~~~$|$~~~~~~0~~~~~~$|
# |Conditional distribution of $X$ given $S = 4$|$~~~~~0.1667~~~~~$|$~~~~~0.6667~~~~~$|$~~~~~0.1667~~~~~$|
# |Conditional distribution of $X$ given $S = 5$|$~~~~~~0~~~~~~$|$~~~~~0.5~~~~~$|$~~~~~0.5~~~~~$|
# |Conditional distribution of $X$ given $S = 6$|$~~~~~0~~~~~$|$~~~~~0~~~~~$|$~~~~~~1~~~~~~$|
# 
# #### Definition ####
# In general, if $V$ and $W$ are two random variables on the same outcome space, then for a fixed value $w$ of $W$, the *conditional distribution of $V$ given $W=w$* is:
# 
# - the set of all possible values of $V$ under the condition that $W=w$, and
# - all the corresponding conditional probabilities $P(V = v \mid W = w)$
# 
# There are four letters in that last probability, so it's a good idea to be clear about what each one represents. The two upper case letters $V$ and $W$ are the names of the two random variables. It is important to note that the number $w$ is *fixed*: it is the known value of $W$. The number $v$ represents a generic possible value of $V$ and is the only number that could vary.
# 
# In our example about the conditional distribution of $X$ given $S=3$, the probabilities along the row corresponding to $S=3$ are $P(X = x \mid S = 3)$ where $x$ could be 1 or 2. In fact $x$ could also be 0, but we don't count that as a possible value of $X$ given $S=3$.
# 
# In the table above, the conditional distributions given different values of $S$ are different. In other words, the distribution of $X$ changes depending on the given value of $S$. Knowing the value of $S$ changes the probabilities for $X$, so $X$ and $S$ are dependent. You knew that already based on the descriptions of the two variables, and you now have confirmation in the conditional distributions.

# ### Conditional Expectation ###
# 
# The expectation of $X$, also called the *unconditional expectation* of $X$, is easy to see from the distribution table:
# 
# |$~~~~~~~~~~~~~~~~~x$| $1$ | $2$ | $3$ |
# |---:|:---:|:---:|:---:|
# |$P(X = x)$|$0.25$|$0.5$|$0.25$|
# 
# Clearly $E(X) = 2$ by symmetry. If you want, you can calculate it using the defintion of expectation. But using symmetry is quicker.
# 
# Now suppose we know the value of $S$. Given that $S$ has the value $s$, the conditional distribution of $X$ is just an ordinary distribution and thus has an expectation. This is called the *conditional expectation of $X$ given $S=s$* and is denoted $E(X \mid S = s)$. Remember that this expectation depends on the given value $s$.
# 
# |$~~~~~~~~~~~~~~~~~~~~~~$| $X = 1$ | $X = 2$ | $X = 3$ |$E(X \mid S = s)$|
# |:---------------:|:---|:---|:---|:---:|
# |Conditional distribution of $X$ given $S = 2$|$~~~~~1~~~~~$|$~~~~~0~~~~~$|$~~~~~~0~~~~~~$|$~~~~~~~~~~~~1~~~~~~~~~~~~$|
# |Conditional distribution of $X$ given $S = 3$|$~~~~~0.5~~~~~$|$~~~~~0.5~~~~~$|$~~~~~~0~~~~~~$|$~~~~1.5~~~~~~~~~$|
# |Conditional distribution of $X$ given $S = 4$|$~~~~~0.1667~~~~~$|$~~~~~0.6667~~~~~$|$~~~~~0.1667~~~~~$|$~~~~~~2~~~~~~~~~~~~$|
# |Conditional distribution of $X$ given $S = 5$|$~~~~~~0~~~~~~$|$~~~~~0.5~~~~~$|$~~~~~0.5~~~~~$|$~~~~~2.5~~~~~~~~~$|
# |Conditional distribution of $X$ given $S = 6$|$~~~~~0~~~~~$|$~~~~~0~~~~~$|$~~~~~~1~~~~~~$|$~~~~~~~~~~~~3~~~~~~~~~~~~$|
# 
# The values of $E(X \mid S=3)$ and $E(X \mid S=5)$ are clear by symmetry. The value of $E(X \mid S=4)$ can be calculated using the definition of expectation:
# 
# $$
# E(X \mid S = 4) ~ = ~ 1(0.1667) + 2(0.6667) + 3(0.1667) ~ = ~ 2
# $$

# ### Expectation by Conditioning ###
# 
# We know that $E(X) = 2$. We also know the conditional expectation of $X$ given each value of $S$:
# 
# |$~~~~~~~~~~~~~~~~~~~~~~~~~s$|$2$|$3$|$4$|$5$|$6$|
# |---------------:|:---:|:---:|:---:|:---:|:---:|
# |$E(X \mid S=s)$|$1$|$1.5$|$2$|$2.5$|$3$|
# 
# Surely the unconditional expectation $E(X) = 2$ is some kind of average of all these conditional expectations.
# 
# And indeed it is. It is the weighted average of all the conditional expectations, where the weights are the chances of the given events.
# 
# We found those chances earlier, in the distribution of $S$:
# 
# |$~~~~~~~~~~~~~~~~~s$| $2$ | $3$ | $4$ | $5$ | $6$ |
# |---:|:---:|:---:|:---:|:---:|:---:|
# |$P(S = s)$|$0.0625$|$0.25$|$0.375$|$0.25$|$0.0625$|
# 
# Augment the conditional expectation table by another row, as follows:
# 
# |$~~~~~~~~~~~~~~~~~~~~~~~~~s$|$2$|$3$|$4$|$5$|$6$|
# |---------------:|:---:|:---:|:---:|:---:|:---:|
# |$E(X \mid S=s)$|$1$|$1.5$|$2$|$2.5$|$3$|
# |$P(S = s)$|$0.0625$|$0.25$|$0.375$|$0.25$|$0.0625$|
# 
# And now find the weighted average of the conditional expectations:
# 
# $$
# 1(0.0625) + 1.5(0.25) + 2(0.375) + 2.5(0.25) + 3(0.0625) ~ = ~ 2 ~ = ~ E(X)
# $$

# We will conclude the chapter by examining this new way of calculating expectation.

# In[ ]:




