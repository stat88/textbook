#!/usr/bin/env python
# coding: utf-8

# ## Functions of Random Variables ##

# When we work with random variables, we often want to consider functions of them. For example, if $X$ is a random length in inches then $Y = 2.54X$ is the length in centimeters, and $W = \vert X - 12 \vert $ measures how far $X$ is from 12 inches.
# 
# If we know the distribution of $X$ we can easily find the expectation of any function of $X$, as in the example below.
# 
# Let $X$ have the uniform distribution on $\{ -1, 0, 1 \}$, and let $Y = X^2$. Let's find $E(Y)$.
# 
# Here is a distribution table for $X$, with values of $Y$ as well.
# 
# |$y = x^2$| $~~~~1$ | $~~~~0$ | $~~~~1$ |
# |--------:|:---:|:---:|:---:|
# |$~~~~~~~~~~~~~~~~~~~ x$| $-1$ | $0$ | $1$ |
# |$P(X = x)$ | $1/3$ | $1/3$ | $1/3$ |
# 
# At a glance you can see that $Y$ has the value $1$ with chance $2/3$ and the value $0$ with chance $1/3$, so $E(Y) = 2/3$.
# 
# But because of the distributive property, we don't even have to collect terms. We can just find $E(Y)$ as the weighted average of the top row, with the weights in the bottom row.
# 
# $$
# E(Y) ~ = ~ (-1)^2\frac{1}{3} + 0^2\cdot\frac{1}{3} + 1^2\cdot\frac{1}{3} = \frac{2}{3}
# $$
# 
# This method can be expressed in a formula that has an unfortunate way of making the operation seem more complicated than it is.
# 
# Let $Y = g(X)$ be a function of the random variable $X$. Then
# 
# $$
# E(g(X)) ~ = ~ \sum_{\text{all }x} g(x)P(X=x)
# $$
# 
# This just expresses what we did in our example for the function $g$ defined by $g(x) = x^2$:
# 
# - Take a value $x$ of the original random variable $X$.
# - Apply the function $g$ to create $g(x)$, the corresponding value of $Y$.
# - Weight this by $P(X=x)$, to get the product $g(x)P(X=x)$.
# - Add these products over all possible values $x$ of $X$.
# 
# For example, if $W = \min(X, 0.5)$ is the smaller of $X$ and 0.5 in our example above, then
# 
# $$
# \begin{align*}
# E(W) ~ &= ~ \min(-1, 0.5)\frac{1}{3} + \min(0, 0.5)\frac{1}{3} + \min(1, 0.5)\frac{1}{3} \\
# &= ~ (-1)\frac{1}{3} + 0\cdot\frac{1}{3} + 0.5\cdot\frac{1}{3} ~ \approx ~ -0.167
# \end{align*}
# $$

# ### Functions on the Outcome Space ###
# 
# The method above extends to finding the expectation of a function of any number of random variables. That's important because data scientists often want to use functions of random samples to make inferences about unknown quantities.
# 
# Recall that our construction of random variables started with the space $\Omega$ consisting of outcomes of our experiment. We defined a random variable as a numerical function on $\Omega$. For example, if $X$ is the number of heads in two tosses of coin then we can set $\Omega = \{ HH, HT, TH, TT\}$ and 
# 
# $$
# X(HH) = 2, ~~ X(HT) = 1 = X(TH), ~~ X(TT) = 0
# $$
# 
# In general, for an outcome $\omega$ in $\Omega$, the value of $X$ is $X(\omega)$.
# 
# This helps us make precise the idea that a function of a random variable is itself a random variable. For example, let $g$ be the function defined by $g(x) = x^2$. Then $g(X)$ is defined by composing two functions as follows:
# $ g(X(\omega)) ~ = ~ (X(\omega))^2$ for every $\omega \in \Omega$. Thus $g(X)$ is also a function on $\Omega$ and hence is a random variable.
# 
# Most commonly, we work with multiple random variables defined on the same space. Here is an example.
# 
# Suppose two draws are made at random without replacement from a population that has five elements labeled $ 1, 2, 2, 3, 3 $. Define the following random variables:
# 
# - $X_1$ is the number on the first draw
# - $X_2$ is the number on the second draw
# - $S = X_1 + X_2$ is sum of the numbers on the two draws
# 
# We will now create a table of all possible values of the pair $(X_1, X_2)$ and the probabilities of all the pairs. We will then use the table to find probabilities of events involving $X_1$, $X_2$, and $S$.

# ### Joint Distribution ###
# We know how to make a distribution table for a single random variable. We will now extend this to a table that displays the *joint distribution* of two random variables. 
# 
# The joint distribution of random variables $X$ and $Y$ consists of all pairs $(x, y)$ that are possible values of the pair $(X, Y)$, along with all the corresponding probabilities $P(X=x, Y=y)$.
# 
# Here is the *joint distribution table* of the random variables $X_1$ and $X_2$ defined above.
# 
# |$~~~~~~~~~~~~~~~$|$X_2=1$|$X_2=2$|$X_2=3$|
# |----------------:|:---:|:---:|:---:|
# |$X_1=1$| $~~~~~ 0 ~~~~~$ |$~~~~~\frac{2}{20}~~~~~$|$~~~~~\frac{2}{20}~~~~~$|
# |$X_1=2$| $~~~~~\frac{2}{20}~~~~~$ |$~~~~~\frac{2}{20}~~~~~$|$~~~~~\frac{4}{20}~~~~~$|
# |$X_1=3$| $~~~~~\frac{2}{20}~~~~~$ |$~~~~~\frac{4} {20}~~~~~$|$~~~~~\frac{2}{20}~~~~~$|
# 
# Each cell of the table represents an intersection: an event of the form $(X_1 = i, X_2 = j)$ for $i$ and $j$ in the range 1, 2, 3. The quantity displayed in the cell is $P(X_1 = i, X_2 = j)$.
# 
# For example, the cell $X_1 = 2, X_2 = 3$ displays $P(X_1 = 2, X_2 = 3) = \frac{2}{5} \cdot \frac{2}{4} = \frac{4}{20}$.
# 
# The table partitions the whole outcome space according to the pairs of values of $X_1$ and $X_2$. So the sum of all the probabilities in the table is equal to 1.
# 
# The chance of any event determined by $X_1$ and $X_2$ can be calculated cell by cell using the addition rule:
# 
# - If the cell is in the event, include its probability.
# - If the cell is not in the event, skip it.
# 
# For example, 
# 
# $$
# \begin{align*}
# &P(X_1 = X_2) \\
# &= ~ P(X_1 = 1, X_2 = 1) + P(X_1 = 2, X_2 = 2) + P(X_1 = 3, X_2 = 3) \\
# &= ~ 0  + \frac{2}{20} + \frac{2}{20} ~ = ~ \frac{1}{5}
# \end{align*}
# $$
# 
# For $S = X_1 + X_2$,
# 
# $$
# P(S = 5) ~ = ~ P(X_1 = 2, X_2 = 3) + P(X_1 = 3, X_2 = 2) ~ = ~ \frac{4}{20} + \frac{4}{20} ~ = ~ \frac{2}{5}
# $$

# ### "Marginal" Distribution ###
# If you have the joint distribution of two random variables, then you can find the distribution of each one.
# 
# For example, the event $X_1 = 1$ consists of the cells in the top row of the joint distribution table above, so
# 
# $$
# P(X_1 = 1) ~ = ~ 0 + \frac{2}{20} + \frac{2}{20} ~ = ~ \frac{4}{20} ~ = ~ \frac{1}{5}
# $$
# 
# This confirms what you already knew from the definition of $X_1$.
# 
# To get each probability in the distribution of $X_1$, we have to add all the probabilities in the corresponding row of the table above. Since the sums are often written in the margins of the table, as shown below, the distribution of $X_1$ is also called the *marginal* distribution of $X_1$.
# 
# 
# |$~~~~~~~~~~~~~~~$|$X_2=1$|$X_2=2$|$X_2=3$|Dist of $X_1$|
# |----------------:|:---:|:---:|:---:|:----------------|
# |$X_1=1$| $~~~~~ 0 ~~~~~$ |$~~~~~\frac{2}{20}~~~~~$|$~~~~~\frac{2}{20}~~~~~$|$~~~~~\frac{4}{20} = \frac{1}{5}~~~~~$ |
# |$X_1=2$| $~~~~~\frac{2}{20}~~~~~$ |$~~~~~\frac{2}{20}~~~~~$|$~~~~~\frac{4}{20}~~~~~$|$~~~~~\frac{8}{20} = \frac{2}{5}~~~~~$|
# |$X_1=3$| $~~~~~\frac{2}{20}~~~~~$ |$~~~~~\frac{4} {20}~~~~~$|$~~~~~\frac{2}{20}~~~~~$|$~~~~~\frac{8}{20} = \frac{2}{5}~~~~~$|
# 
# You can get the distribution of $X_2$ by summing along columns.

# ### Expectations of Functions ###
# We can find the expectation of any function $g$ of two random variables $X$ and $Y$ by extending our method for finding the expectation of a function of $X$.
# 
# - Take a cell of the joint distribution table of $X$ and $Y$. This corresponds to one possible value $(x, y)$ of the pair $(X, Y)$.
# - Apply the function $g$ to get $g(x,y)$.
# - Weight this by the probability in the cell, to get the product $g(x,y)P(X=x, Y=y)$
# - Add these products over all the cells of the table.
# 
# This is a bit laborious but straightforward. Here for reference is the joint distribution table of $X_1$ and $X_2$ from the examples above. Let's use it to find $E(\vert X_1 - X_2 \vert)$, the expected value of how far apart the the two draws are.
# 
# |$~~~~~~~~~~~~~~~$|$X_2=1$|$X_2=2$|$X_2=3$|
# |----------------:|:---:|:---:|:---:|
# |$X_1=1$| $~~~~~ 0 ~~~~~$ |$~~~~~\frac{2}{20}~~~~~$|$~~~~~\frac{2}{20}~~~~~$|
# |$X_1=2$| $~~~~~\frac{2}{20}~~~~~$ |$~~~~~\frac{2}{20}~~~~~$|$~~~~~\frac{4}{20}~~~~~$|
# |$X_1=3$| $~~~~~\frac{2}{20}~~~~~$ |$~~~~~\frac{4} {20}~~~~~$|$~~~~~\frac{2}{20}~~~~~$|
# 
# We will find $E(\vert X_1 - X_2 \vert)$ by executing the plan described above.
# 
# - The contribution of the cell $X_1 = 1, X_2 =1$ is clearly 0.
# - The contribution of the cell $X_1 = 1, X_2 =2$ is $\vert 1 - 2 \vert \frac{2}{20} = \frac{2}{20}$.
# - The contribution of the cell $X_1 = 1, X_2 =3$ is $\vert 1 - 3 \vert \frac{2}{20} = \frac{4}{20}$.
# - And so on.
# 
# It's a bit of pain, but you can go through the process for all nine cells of the table and add up all the contributions to get $E(\vert X_1 - X_2 \vert) = \frac{20}{20} = 1$.

# ### Additivity of Expectation ###
# It will come as a relief that you can find $E(X+Y)$ without going through the long process outlined above. Because of the distributive property, the long calculation simplifies and we get
# 
# $$
# E(X+Y) ~ = ~ E(X) + E(Y)
# $$
# 
# no matter what the joint distribution of $X$ and $Y$.
# 
# This *additivity* is one of the most important properties of expectation, because it is true whether the random variables are dependent or independent. 
# 
# One way to prove the formula is to apply our long-hand method for finding $E(S)$ and then do the algebraic simplification. Another is to make an equivalent definition of expectation on the outcome space $\Omega$ and use it instead. But we won't take the time for that. We will just focus on applications.
# 
# The rest of the chapter consists of powerful uses of additivity. For now, let's find $E(S)$ in our example above.
# 
# - $E(X_1) = 1\cdot\frac{1}{5} + 2\cdot\frac{2}{5} + 3\cdot\frac{2}{5} = 2.2$.
# - By the symmetry of draws without replacement, the distribution of $X_2$ is the same as that of $X_1$ and hence $E(X_2) = 2.2$. You can also check this by finding the marginal distribution of $X_2$ and calculating its expectation.
# 
# By additivity, the expectation of $S = X_1 + X_2$ is
# 
# $$
# E(S) ~ = ~ E(X_1) + E(X_2) ~ = ~ 2.2 + 2.2 ~ = ~ 4.4
# $$

# In[ ]:




