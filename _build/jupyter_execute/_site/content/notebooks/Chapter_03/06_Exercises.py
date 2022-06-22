#!/usr/bin/env python
# coding: utf-8

# ## Exercises ##

# **1.**
# In a move in the game Monopoly, a die is rolled twice. Let $D_1$ be the number of spots on the first roll, $D_2$ the number of spots on the second roll, and $S = D_1 + D_2$ the total number of spots on the two rolls.
# 
# **a)** Find the distribution of $S$.
# 
# **b)** Find $P(S > 7)$.
# 
# **c)** Find $P(|S - 7| \le 2)$.

# **2.**
# A true-false test has 20 questions. 
# 
# **a)** Dev hasn't studied at all, so he guesses each answer by tossing a coin. Let $R$ be the number of questions that Dev gets right. Find $P(R > 16)$. 
# 
# **b)** Aram, Chendi, and Samir haven't studied either. So each of them also guesses every answer by tossing a coin. What is the chance that none of them gets more than 16 questions right? 

# **3.**
# Yi likes to bet on "red" at roulette. Each time she bets, her chance of winning is $18/38$ independently of all other times. Suppose she bets repeatedly on red. Find the chance that:
# 
# **a)** she wins four of the first 10 bets
# 
# **b)** she wins at most four of the first 10 bets
# 
# **c)** the third time she wins is on the 10th bet
# 
# **d)** she needs more than 10 bets to win five times

# **4.** Akaash bets a dollar repeatedly on a "split" at roulette. 
# 
# - Each time he bets, his chance of winning is $2/38$ independently of other times. 
# - Each time he wins a bet, his net gain is 17 dollars. 
# - Each time he loses a bet, he loses a dollar; that is, his net gain is $-1$ dollars.
# 
# Suppose he bets 90 times. What is the chance that he makes money? In other words, what is the chance that his total net gain is positive?

# **5.** A standard deck consists of 52 cards. Each card has a color, a suit, and a rank, as follows.
# 
# - There are 13 cards in each of four suits: hearts, diamonds, spades, and clubs.
# - Hearts and diamonds are red. Spades and clubs are black.
# - In each suit, the cards are of 13 ranks: Ace, 2, 3, $\ldots$, 10, Jack, Queen, King.
# - The Jacks, Queens, and Kings are called face cards.
# 
# Throughout this course, "dealt" means "sampled at random without replacement".
# 
# A bridge hand consists of 13 cards dealt from the deck.
# 
# **a)** Find the chance that the hand contains two aces.
# 
# **b)** Find the chance that the hand contains more than two aces.
# 
# **c)** Find the chance that the hand contains six face cards. 

# **6.** In a population of 200 voters, 70 are registered with Party A and the other 130 are registered with Party B. A simple random sample of 40 voters is drawn from this population. Let $V$ be the number of sampled voters who are registered with Party A, and let $W = 40 - V$ be the number of sampled voters who are registered with Party B Find:
# 
# **a)** $P(V = 10)$
# 
# **b)** $P(V > 10)$
# 
# **c)** $P(W < 3V)$

# **7.**
# Every time Adalie buys a lottery ticket, her chance of winning is 1 in a million, independently of all other times. What is the smallest number of lottery tickets Adalie has to buy so that the chance that that she wins at least once is more than 50%?
# 
# [You might want to use a Jupyter notebook cell to find the numerical value, just to get a sense of the magnitude. Use `np.log(x)` for $\log(x)$ and `np.e` for $e$. Here $\log$ means the natural logarithm.]

# **8.**
# Yiwen, Shashank, and Ophelia go out to dinner together every week. Each time, each of them tosses a coin. If one person's coin lands differently from both the others, that person is the "odd one out" and has to pay for everyone's dinner. If nobody is the odd one out then each person pays for their own dinner.
# 
# Suppose they do this for 15 weeks.
# 
# **a)** What is the chance that there is an odd one out at least once?
# 
# **b)** What is the chance that Yiwen never has to pay for her own dinner?

# **9.** A coin is tossed 200 times. Let $X_1$ be the number of heads in the first 100 tosses and let $X_2$ be the number of heads in the last 100 tosses.
# 
# **a)** True or false (explain): $X_1 = X_2$.
# 
# **b)** Do $X_1$ and $X_2$ have the same distribution? Why or why not?

# **10.** A standard deck consists of 52 cards, 4 of which are aces. A simple random sample of 26 cards is drawn from the deck. Let $X_1$ be the number of aces in the sample and let $X_2$ be the number of aces among the cards that were not drawn in the sample.
# 
# **a)** True or false (explain): $X_1 = X_2$.
# 
# **b)** Do $X_1$ and $X_2$ have the same distribution? Why or why not?
