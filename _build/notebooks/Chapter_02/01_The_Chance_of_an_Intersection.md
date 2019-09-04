---
redirect_from:
  - "/notebooks/chapter-02/01-the-chance-of-an-intersection"
interact_link: content/notebooks/Chapter_02/01_The_Chance_of_an_Intersection.ipynb
kernel_name: python3
has_widgets: false
title: 'The Chance of an Intersection'
prev_page:
  url: /notebooks/Chapter_02/00_Intersections_and_Conditioning.html
  title: 'Intersections and Conditioning'
next_page:
  url: /notebooks/Chapter_02/02_Symmetry_in_Simple_Random_Sampling.html
  title: 'Symmetry in Simple Random Sampling'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---


## The Chance of an Intersection



The intersection of two events is a subset of each of them, so its chance is less than or equal to the chance of each one and hence is at most equal to the minimum of the two chances.

![intersection](../../images/intersection.png)

$$
P(AB) ~ \le ~ \min(P(A), P(B))
$$



But how do we find it exactly? Let's start out with a simple example.



### Two Cards from a Deck of Three
I deal two cards at random without replacement from a deck that contains one red, one blue, and one green card. This means:

- I pick one of the three cards at random.
- Then I pick one card at random from the two cards that remain in the deck.

That is, I don't replace the card the first card I picked before drawing the second one.

What is the chance that I draw the blue card followed by the red card?

We can answer this by listing all possible outcomes and seeing which ones correspond to the event in question. 

The outcome space $\Omega$ is the set of all possible pairs of cards, keeping track of which was first and which was second. If we let R stand for the red card, B for the blue, and G for the green, then $\Omega = \{ RB, RG, BG, BR, GR, GB\}$.

The event "the blue card followed by the red card" consists of just one outcome, BR. 

The draws are at random, so all six pairs are equally likely. The chance of getting a blue card followed by a red card is therefore $1/6$.

It is illuminating to keep track of the draws in sequence and write the answer $1/6$ as a product:

$$
\begin{align*}
P(\text{the first card is blue and the second is red}) ~ = ~ \frac{1}{6} ~ &= ~ \frac{1}{3} \times \frac{1}{2} \\
&= ~ P(\text{the first card is blue}) \times \frac{1}{2}
\end{align*}
$$

The factor $1/2$ is the chance of drawing the red card from the reduced deck consisting of just the red and green cards. This probability is known as the *conditional probability of drawing a red card second, given that the first card drawn is blue*. 

We write

$$
\begin{align*}
& P(\text{the first card is blue and the second is red}) \\
& = ~ P(\text{the first card is blue})P(\text{the second is red} \mid \text{the first card is blue})
\end{align*}
$$

The vertical bar in the conditional probability is read as "given that".

That's still quite long, so we will introduce some notation that keeps track of the pair of cards in order. Define the following events:

- $B_1$ is the event that the first card is blue
- $R_2$ is the event that the second card is red

The event in question is the intersection $B_1 R_2$, and the result is

$$
P(B_1 R_2) ~ = ~ P(B_1)P(R_2 \mid B_1)
$$

This example motivates one of the fundamental rules of probability.



### Multiplication Rule
We now have a method of finding the chance of the intersection of any two events $A$ and $B$. The chance is given by 

$$
P(AB) ~ = ~ P(A)P(B \mid A)
$$

where the second factor on the right hand side is the *conditional probability that B occurs given that A occured*.

For example, suppose you deal two cards from a standard deck that has 52 cards of which 13 are hearts. You can assume that this means you pick one card at random from all 52 cards and then another at random from the remaining 51. Then

$$
P(\text{both cards are hearts}) ~ = ~ \frac{13}{52} \times \frac{12}{51}
$$

The second factor on the right hand side is the conditional probability that the second card is a heart given that the first card was a heart. If the first card was a heart then there are only 12 hearts among the 51 cards that remain after the first card is drawn.



In these examples about cards, the conditional probabilities we needed were easy to find. But sometimes it is not possible to find it based on the information given – someone has to go get more data, or summarize the available data in a different way, for us to know the conditional chance that we need.

For example, consider the randomly picked teen of the previous chapter and recall that we knew the chance that the teen used Facebook as well as the chance that the teen used Twitter. These chances were:

- $P(\text{used Facebook}) ~ = ~ 0.51$. That is, 51% of all teens in the population used Facebook.
- $P(\text{used Twitter}) ~ = ~ 0.32$. That is, 32% of all teens in the population used Twitter.

What is the chance that the teen used both platforms? Let's try to calculate it. By the multiplication rule,

$$
P(\text{used both Facebook and Twitter}) ~ = ~ 0.51 \times P(\text{used Twitter} \mid \text{used Facebook})
$$

But now we are stuck. The conditional probability $P(\text{used Twitter} \mid \text{used Facebook})$ is the proportion of teens who used Twitter *among those who used Facebook*. We don't know that proportion. Though the proportion of Twitter users among all teens is 32%, it need not be 32% among the Facebook users.

To find the proportion of teens who used both platforms, we must request the Pew Research Center to go back to the survey responses and find the proportion who used both platforms. We can't figure it out from the available summary because the summary only provides usage data for individual platforms, not pairs. 



### Inclusion-Exclusion
If two events are not mutually exclusive, then their intersection helps us find the chance of their union. 

In the figure below, the blue region is the union of the events $A$ and $B$.

![inclusion-exclusion](../../images/incl_excl.png)

We know that if we try to find $P(A \cup B)$ by just adding $P(A)$ and $P(B)$, our answer will be too big. The figure shows that the answer will be too big because we will have included the intersection $AB$ twice: once as part of $A$ and then again as part of $B$.

So if we try to find $P(A \cup B)$ by adding $P(A)$ and $P(B)$ then we must fix our error by subtracting $P(AB)$:

$$
P(A \cup B) ~ = ~ P(A) + P(B) - P(AB)
$$

This is called an *inclusion-exclusion* formula. Bonferroni developed a sequence of such formulas for an increasing number of events in the union.

Notice that the inclusion-exclusion formula is true for all events $A$ and $B$. The addition rule is only for mutually exclusive events, which is of course the case when $P(AB) = 0$.

Suppose I roll a die twice. What is the chance that the face with six spots appears at least once? 

Let $S_i$ be the event that the die shows a six on Roll $i$. Then the probability we want is 

$$
P(S_1 \cup S_2) ~ = ~ P(S_1) + P(S_2) - P(S_1S_2)
~ = ~ \frac{1}{6} + \frac{1}{6} - P(S_1)P(S_2 \mid S_1) 
$$

by the inclusion-exclusion formula and the multiplication rule. Now $P(S_2 \mid S_1) = 1/6$ because the chance that the second roll is a six is not affected by what appeared on the first roll. So

$$
P(S_1 \cup S_2) ~ = ~ \frac{1}{6} ~ + ~ \frac{1}{6} ~ - ~ \frac{1}{6} \cdot \frac{1}{6} ~ = ~ \frac{11}{36}
$$

Sometimes you can avoid using inclusion-exclusion by approaching the problem in a different way. The event "at least one six" is the complement of "no sixes", and so

$$
P(\text{at least one six in two rolls}) ~ = ~ 1 - P(\text{no sixes in two rolls}) ~ = ~ 1 ~ - ~ \frac{5}{6} \cdot \frac{5}{6} ~ = ~ \frac{11}{36}
$$

as before. This method has the advantage that it extends immediately to more rolls. For example,

$$
P(\text{at least one six in 10 rolls}) ~ = ~ 1 - \big{(}\frac{5}{6}\big{)}^{10}
$$



### Intersection of Several Events

The standard deck consists of 13 cards in each of four *suits*: hearts, diamonds, spades, and clubs. Suppose you deal five cards from a well-shuffled deck. This means the five cards are dealt at random without replacement, and is a good model for a 5-card poker hand.

**Question 1:** What is the chance that all five cards are hearts?

**Answer:** By a natural extention of the multiplication rule, the answer is

$$
P(\text{all five are hearts}) ~ = ~ \frac{13}{52} \cdot \frac{12}{51} \cdot \frac{11}{50} \cdot \frac{10}{49} \cdot \frac{9}{48}
$$

Formally, if $H_i$ is the event that Card $i$ is a heart, then we have extended the multiplication rule to say

$$
P(H_1H_2H_3H_4H_5) ~ = ~ P(H_1)P(H_2 \mid H_1)P(H_3 \mid H_1H_2)P(H_4 \mid H_1H_2H_3)P(H_5 \mid H_1H_2H_3H_4)
$$

Notice that the answer is a fraction of a fraction of a fraction ... and so on. Each time you impose a new condition – for example, "Card 3 has to be a heart too" – you reduce the chance of getting what you want. 

The extension can be proved easily by induction; we will leave that to another class.

**Question 2:** What is the chance that all four cards are of the same suit?

**Answer:** This kind of hand is called a flush. Resist the impulse to say that the answer is the same as that in Question 1. Before you calculate, compare the two events:

- all five cards are hearts
- all five cards are of the same suit

The latter is more likely because it includes the former and also includes other possibilities. For example it includes "all five cards are spades".

This observation leads to one natural way to solve the problem: **Partition** the event into smaller pieces (that is, make an exhaustive list of distinct ways it can happen), and add up the chances of the pieces. 

$$
\begin{align*}
& P(\text{all five cards are hearts}) \\
&= ~ P(\text{all hearts or all diamonds or all spades or all clubs}) ~~~~~~~~~ \text{(union of mutually exclusive events)} \\
&= ~ 4 \times \frac{13}{52} \cdot \frac{12}{51} \cdot \frac{11}{50} \cdot \frac{10}{49} \cdot \frac{9}{48} ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \text{(addition rule)}
\end{align*}
$$

Partitioning events, informally known as "listing the ways," is a fundamental method of calculating chances.

Another good way to think about this problem is to take one card at a time. For the event to occur,

- the first card can be any card in the deck,
- the second card must be of the same suit as the first,
- the third card must be of the same suit as the first two, etc

So

$$
P(\text{all five cards are hearts}) ~ = ~ \frac{52}{52} \cdot \frac{12}{51} \cdot \frac{11}{50} \cdot \frac{10}{49} \cdot \frac{9}{48}
$$

which is the same as the answer we got by partitioning.

