#!/usr/bin/env python
# coding: utf-8

# ## Exercises ##

# **1.**
# Let $X$ have the distribution displayed in the table below.
# 
# |$~~~~~~~~~~~~~~~~x$|$-2$|$-1$|$0$|$1$|
# |---:|:---:|:---:|:---:|:---:|
# |$P(X=x)$|$0.2$|$0.25$|$0.35$|$0.2$|
# 
# Find
# 
# **a)** $E(X)$
# 
# **b)** $E(X-1)$
# 
# **c)** $E(\vert X - 1 \vert)$
# 
# **d)** $E((X-1)^2)$

# **2.**
# A true/false test consists of 25 questions. A student knows the correct answer to 10 of the questions. She guesses each of the other answers independently based on the toss of a coin. 
# 
# **a)** Find the expectation of the number of correct answers.
# 
# **b)** Find the chance that the student gets more than 20 questions right.

# **3.**
# A box contains four blank index cards and one that has a gold star on it. Cards are drawn one by one at random without replacement until the gold star appears. Let $D$ be the number of cards drawn.
# 
# **a)** Find the distribution of $D$.
# 
# **b)** Find $E(D)$.
# 
# **c)** Suppose all five cards were dealt one by one at random without replacement. If you saw the sequence of cards, would you be able to tell whether you were looking at the sequence forwards (that is, in the order in which the cards were drawn) or backwards? If the answer is "no", can you use it to give another justification for the answer to Part **b**?
# 
# **d)** Suppose you deal at random without replacement from a standard deck of 52 cards. Use the idea in Part **c** to find the expected number of cards dealt till the ace of spades appears.

# **4.**
# In roulette, the bet on a "split" pays 17 to 1 and there are 2 chances in 38 to win. "Pays 17 to 1" means that if a gambler bets one dollar on a split and wins the bet, then her net gain will be 17 dollars. If she loses the bet, then she loses her dollar; that is, her net gain is $-1$ dollars.
# 
# **a)** Suppose 200 gamblers bet on a split. Find the expectation of their total net gain.
# 
# **b)** Does your answer to Part **a** depend on whether the 200 bets were on the same or different spins of the roulette wheel?

# **5.**
# A coin is tossed four times. Let $X$ be the number of heads in the first three tosses and let $Y$ be the number of heads in the last three tosses.
# 
# **a)** Do $X$ and $Y$ have different distributions? Explain.
# 
# **b)** Are $X$ and $Y$ independent? Explain.
# 
# **c)** Make a joint distribution table for $X$ and $Y$. It might help to write out all the possible outcomes of four tosses of a coin, though it is not necessary.
# 
# **d)** Use your table in Part **c** to find $P(X = Y)$.
# 
# **e)** Use your table in Part **c** to find $E(\vert X - Y \vert)$.
# 
# **f)** Use your table in Part **c** to find the marginal distribution of $X$, and check that it is consistent with your answer in Part **a**. 

# **6.**
# A die is rolled 12 times. Find the expectation of
# 
# **a)** the number of times the face with five spots appears
# 
# **b)** the number of times an odd number of spots appears
# 
# **c)** the number of faces that don't appear
# 
# **d)** the number of faces that do appear

# **7.** A randomized controlled experiment has 100 participants of whom 40 are women. A simple random sample of 70 participants is assigned to the treatment group and the remaining 30 are in the control group. 
# 
# How many more women are expected to be in the treatment group than in the control group?

# **8.**
# A sports team consists of $n$ players. Each player has a backpack that from the outside looks the same as all the others'. Suppose each player picks up a backpack at random without replacement.
# 
# **a)** Fix an integer $k$ in the range 1 through $n$. What is the chance that Player $k$ picks up her own backpack?
# 
# **b)** Let $B$ be the number of players who pick up their own backpacks. Find $E(B)$.
# 
# **c)** For large $n$, approximately what is the distribution of $B$? Why?
# 
# **d)** Are your answers to Parts **b** and **c** consistent?

# **9.**
# Surveyors take a simple random sample of 100 households from the city. Let $X_1, X_2, \ldots, X_{100}$ be the annual incomes of the sampled households.
# 
# **a)** For each of the following quantities, say whether it is a parameter or a statistic.
# 
# - (i) $X_{15}$
# - (ii) the average annual income of the households in the sample
# - (iii) the average annual income of the households in the population
# - (iv) the average of the smallest and largest annual incomes among households in the sample
# - (v) the median annual income of the households in the population
# 
# **b)** Which of the following is an unbiased estimator of the average annual income of households in the population? More than one option might be correct; pick all that work.
# 
# - (i) $\frac{1}{100}\sum_{i=1}^{100}X_i$
# - (ii) $X_1$
# - (iii) $X_{15}$
# - (iv) $(X_1 + X_{15})/15$
# - (v) $(X_1 + 2X_{100})/3$

# **10.**
# Five thousand votes have been cast in an election. Each vote is either for Candidate A or for Candidate B. The voting is over but the results have not yet been announced. 
# 
# A polling organization wants to estimate the margin of victory for Candidate A. This parameter is defined as the proportion of votes for Candidate A minus the proportion of votes for Candidate B. Note that this margin of "victory" could be negative if Candidate B gets more votes than Candidate A.
# 
# The polling organization conducts an exit poll by surveying a simple random sample of 100 voters after all of the 5000 voters have finished voting.
# 
# **a)** Let $p$ be the proportion of the 5000 voters who voted for Candidate A. Express the margin of victory in terms of $p$.
# 
# **b)** Let $X$ be the number of sampled voters who voted for Candidate A. Use $X$ to constructed an unbiased estimator of the margin of victory.

# **11.**
# A data scientist believes that a randomly picked student at his school is twice as likely not to own a car as to own one car. He knows that no student has three cars, though some students do have two cars. He therefore models the probability distribution for the number of cars owned by a random student as follows. The model involves an unknown positive parameter $\theta$.
# 
# |$\text{number of cars}$| $0$ | $1$ | $~~~~~~~~~~~2$ |
# |---------------:|:---:|:---:|:---:|
# |$\text{probability}$| $2\theta$ | $\theta$ | $1 - 3\theta$|
# 
# Let $X_1, X_2, \ldots, X_n$ be the numbers of cars owned by $n$ random students picked independently of each other. Assuming that the data scientist's model is good, use the entire sample to construct an unbiased esimator of $\theta$.
# 
# [Hint: Start by finding $E(X_1)$.]

# **12.** 
# A coin is tossed four times. As in Exercise 5 above, let $X$ be the number of heads in the first three tosses and $Y$ the number of heads in the last three tosses.
# 
# **a)** The distribution of $Y$ is one of the famous ones. Provide its name, parameters, and expectation.
# 
# **b)** For each possible value $x$ of $X$, find $E(Y \mid X = x)$. Your answer to **5c** will be helpful.
# 
# **c)** Find $E(Y)$ by conditioning on $X$, and confirm that the result is the same as your answer to Part **a**.

# **13.**
# A survey organization in a town is studying families with children. Among the families that have children, the distribution of the number of children is as follows.
# 
# |Number of Children $n$|$1$|$2$|$3$|$4$|$5$|
# |:--------------------|:---:|:---:|:---:|:---:|:---:|
# |**Proportion with** $n$ **Children**|$0.2$|$0.4$|$0.2$|$0.15$|$0.05$|
# 
# Suppose each child has chance $0.51$ of being male, independently of all other children. What is the expected number of male children in a family picked at random from those that have children?

# **14.** 
# A die is rolled repeatedly.
# 
# **a)** Find the expected number of rolls till a face with more than 4 spots appears.
# 
# **b)** Find the expected number of rolls till a total of five sixes appear.
# 
# **c)** Find the expected number of rolls till two different faces have appeared.

# **15.**
# Ophelia has to call a utility company to get help with a problem at her apartment. Once she reaches a customer service representative, the length of the call till her problem is solved is random with an expectation of 7 minutes.
# 
# But it is not easy to reach a customer service representative.
# 
# - When Ophelia calls, there is 90% chance that she will be put on hold for an expected duration of 12 minutes before reaching a customer service representative.
# - There is a 10% chance that she will be put on hold for a random time with an expected duration of 8 minutes at which point the call will be cut off for no reason and she will have to call again. 
# 
# Ophelia needs her problem to be fixed, so she calls until she reaches a representative and her problem is solved. You can assume there is no lag between repeated calls and that all durations of holds and conversations with representatives are independent of each other.
# 
# Find the expected length of time Ophelia is on the phone till her problem is solved.
