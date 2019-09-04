---
redirect_from:
  - "/notebooks/chapter-02/02-symmetry-in-simple-random-sampling"
interact_link: content/notebooks/Chapter_02/02_Symmetry_in_Simple_Random_Sampling.ipynb
kernel_name: python3
has_widgets: false
title: 'Symmetry in Simple Random Sampling'
prev_page:
  url: /notebooks/Chapter_02/01_The_Chance_of_an_Intersection.html
  title: 'The Chance of an Intersection'
next_page:
  url: /notebooks/Chapter_02/03_Bayes_Rule.html
  title: 'Bayes Rule'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---


## Symmetry in Simple Random Sampling



Sampling individuals at random without replacement is one of the most natural ways to collect a random sample from a finite population. It is called *simple random sampling* and will be studied extensively in this course.

But before we get to large populations, we will examine simple random sampling in the context of dealing hands of cards from a deck (or population) of size 52. This will help us see some beautiful symmetries that arise when we sample at random without replacement.



### Product Rule of Counting
We saw earlier that if you deal five cards from a well-shuffled deck then

$$
P(\text{all five are hearts}) ~ = ~ \frac{13}{52} \cdot \frac{12}{51} \cdot \frac{11}{50} \cdot \frac{10}{49} \cdot \frac{9}{48}
$$

Those products are worth a second look.

If you deal one card, the number of possible outcomes is 52.

If you deal two cards without replacement, the number of possible pairs (first card, second card) is $52 \times 51$.

- There are 52 options for the first card.
- For each of these options, there are 51 options for the second card.
- So the total number of (first card, second card) pairs is $52 \times 51$.

By extension, the total number of sequences of five cards (first, second, third, fourth, fifth) is $52 \times 51 \times 50 \times 49 \times 48$, the denominator in the answer above.

The numerator is the number of sequences in which all five cards are hearts.

Note that a sequence keeps track of the cards in order: the sequence *a, b, c* is different from *b, c, a*.

The *product rule of counting* says that if you are constructing a sequence of items in $k$ stages, and the number of options at Stage $i$ is $n_i$, then the total number of sequences you can create is $n_1n_2n_3 \ldots n_k$.

Even simple experiments can have a large number of possible outcomes.

- If you roll a die 3 times, there are $6^3 = 216$ sequences of faces.
- If you toss a coin 10 times, there are $2^{10} = 1024$ possible sequences of heads and tails.
- If you deal all 52 cards in a standard deck, there are $52!$ possible sequences or *permutations*. That'a lot of possibilities:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
import math
math.factorial(52)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
80658175170943878571660636856403766975289505440883277824000000000000
```


</div>
</div>
</div>



If an outcome space is enormous then events in which we are interested might be large as well. It's not pleasant to contemplate listing all the outcomes in an event that contains millions of them. So instead, let's see if we can find some simplifications.



### Symmetry
The deck has an equal number of red and black cards: hearts and diamonds are red and spades and clubs are black.

If you deal two cards (from now on, we will not keep saying "without replacement"), what is the chance that the second card is red?

Had the question been about the first card, the answer would have been immediate: $26/52$.

But it's about the second card. Here are a few ways to go about answering. By the end, you'll see which one is the best.

**Answer 1:** You can slog through the calculation by partitioning the event according to what the first card was. If $B_i$ is the event that a black card appears at Position $i$ and $R_i$ is the event that a red card appears at Position $i$, then

$$
\begin{align*}
P(R_2) ~ &= ~ P(B_1R_2) + P(R_1R_2) \\
&= ~ \frac{26}{52} \cdot \frac{26}{51} + \frac{26}{52} \cdot \frac{25}{51} \\
&= ~ \frac{26}{52} \big{(} \frac{26}{51} + \frac{25}{51} \big{)} \\
&= ~ \frac{26}{52} \cdot \frac{51}{51} \\
&= ~ \frac{26}{52}
\end{align*}
$$



Aha! The chance that the second card is red is the same as the chance that the first card is red!

When you get a simple answer like this, always try to understand it better. There might be a simpler explanation that you have missed.

**Answer 2:** Another way to find $P(R_2)$ is to count all the pairs (first card, second card) and also count all the pairs in which the second card is red. Then $P(R_2)$ is the second count divided by the first.

The denominator is $52 \times 51$ as we already know.

There are several ways to evaluate the numerator. Let's use one of the simpler ones. It relies on noticing that you get to decide what the "first stage" in your construction of the pair should be.

- Place a red card in Position 2. There are 26 ways to do this.
- Now place any of the remaining cards in Position 1. There are 51 ways to do this. 

The numerator is therefore $51 \times 26$. Now we have

$$
P(R_2) ~ = ~ \frac{51 \times 26}{52 \times 51} ~ = ~ \frac{26}{52}
$$

That's simpler than Answer 1 but it still doesn't get to the heart of the matter. Answer 3 does.

**Answer 3:** If someone deals all 52 cards and shows you the entire sequence backwards, you would not be able to tell that it was backwards. If they dealt the cards in a circle, you would not be able to tell which was the first card they dealt.

It doesn't matter which position you are looking at. What matters is that you don't know anything about the cards at the other positions. So every card is equally likely to be at the position you are considering. That means

$$
P(R_2) ~ = ~  P(R_1) ~ = ~ P(R_{17}) ~ = ~ P(R_{52}) ~ = ~ P(R_i) ~ = ~ \frac{26}{52} ~~~ \text{for every } i = 1, 2, \ldots , 52
$$

This symmetry is very powerful and saves a lot of calculation. 

For example, if you deal a deck of cards then

$$
\begin{align*}
P(R_{20}R_{33}) ~ &= ~ \frac{26}{52} \cdot \frac{25}{51} \\ \\
P(R_{20}B_{33}) ~ &= ~ \frac{26}{52} \cdot \frac{26}{51} \\ \\
P(B_{18} \mid R_{21}R_{40}) ~ &= ~ \frac{26}{50} 
\end{align*}
$$

and so on.

