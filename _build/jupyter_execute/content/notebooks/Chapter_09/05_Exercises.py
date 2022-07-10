#!/usr/bin/env python
# coding: utf-8

# ## Exercises ##

# **1.**
# All the patients at a doctor's office come in annually for a check-up when they are not ill. The temperatures of the patients at these check-ups are independent and identically distributed with unknown mean $\mu$. 
# 
# The temperatures recorded in 100 check-ups have an average of 98.2 degrees and an SD of 1.5 degrees. Do these data support the hypothesis that the unknown mean $\mu$ is 98.6 degrees, commonly known as "normal" body temperature? Or do they indicate that $\mu$ is less than 98.6 degrees?
# 
# Make a decision in the following steps.
# 
# **a)** State an appropriate null hypothesis in informal terms and also in terms of random variables.
# 
# **b)** State an appropriate alternative hypothesis.
# 
# **c)** What test statistic do you want to use? Justify your choice.
# 
# **d)** Find the $p$-value of the test, exactly if possible or approximately if it is not possible to get an exact answer.
# 
# **e)** At the 5% level, what is the conclusion of the test? Why?

# **2.**
# One of Gregor Mendel's models was about a type of pea plant that is either tall or short. His model was that each such plant is short with chance $1/4$, independently of all other plants. In the plants that he bred, he observed 787 tall ones and 277 short ones. Do the data support his model? Or do they indicate that the model is not good? Make a decision in the following steps.
# 
# **a)** State an appropriate null hypothesis in informal terms and also in terms of random variables.
# 
# **b)** State an appropriate alternative hypothesis.
# 
# **c)** What test statistic do you want to use? Justify your choice.
# 
# **d)** Find the $p$-value of the test, exactly if possible or approximately if it is not possible to get an exact answer.
# 
# **e)** At the 5% level, what is the conclusion of the test? Why?

# **3.**
# The $p$-value of a test of hypotheses is 1.5%.
# 
# **a)** Is the result statistically significant?
# 
# **b)** Is the result highly statistically significant?
# 
# **c)** If you decide to use 2% as the level of the test, which of the two hypotheses will you pick? 

# **4.**
# The $p$-value of a test of hypotheses is 0.001.
# 
# Say whether each of the following statements is true or false, and explain.
# 
# **a)** There is only about a 0.001 chance that the null hypothesis is true.
# 
# **b)** There is about a 0.999 chance that the alternative hypothesis is true.

# **5.**
# Suppose you toss a coin 400 times to test whether it is fair or unfair. And suppose you decide to use 5% as the level of significance.
# 
# Let $X$ be the number of heads in the 400 tosses. For which values of $X$ will your test conclude that the coin is unfair? Why?

# **6.**
# "One pound" bags of coffee produced by a local company actually contain a random amount of coffee. The amounts of coffee in the bags are i.i.d. with unknown mean $\mu$. 
# 
# In 100 bags the average amount of coffee is 16.3 ounces and the SD is 0.7 ounces. For comparison, an ounce is approximately the weight of five quarters.
# 
# Construct an approximate 95% confidence interval for the underlying mean $\mu$. Do the data indicate that $\mu = 16$ ounces?

# **7.**
# A survey organization studying households in a county takes a simple random sample of 500 households from all the households in the county.
# 
# - The size of a household is the number of people who live in it. The sizes of the sampled households have an average of 2.8 and an SD of 2.1.
# - Ten percent of the sampled households consist of just one person. Such households are called "single person" households.
# 
# **a)** If possible, construct an approximate 90% confidence interval for the average household size in the county. If this is not possible, explain why.
# 
# **b)** True or false: About 68% of the households in the sample had between 0.7 and 4.9 people.
# 
# **c)** If possible, construct an approximate 90% confidence interval for the percent of single person households in the county. If this is not possible, explain why not.

# **8.**
# A survey organization takes a large simple random sample of people in a country and uses the methods of our class to construct an approximate 95% confidence interval for the percent of senior citizens in the country. The interval goes from 16.8% to 23.2%.
# 
# In each part below, find the quantity if possible. If it is not possible, explain why.
# 
# **a)** the percent of senior citizens in the country
# 
# **b)** the percent of senior citizens in the sample
# 
# **c)** the sample size
# 
# **d)** and approximate 90% confidence interval for the percent of senior citizens in the population

# **9.**
# A randomized controlled trial was conducted as part of a effort to encourage high school students from under-resourced communities to apply for college. The trial had 200 participants. A simple random sample of 95 participants received special coaching for the ACT. The remaining participants received no intervention. 
# 
# At the end of the experiment, the participants got to decide whether or not they would take the ACT. Among the 95 students in the treatment group, 75 decided to take the test. Among the 105 students in the control group, 70 decided to take it.
# 
# Is the difference statistically significant? Answer this question by performing a test of whether or not the intervention had any effect.

# **10.**
# Randomized experiments and tests of hypotheses are part of the standard methodology of science. The origin of the methods centered on an Englishwoman called Muriel Bristol and the English love of tea taken with milk. There has long been debate about whether the tea should be poured first, or the milk. Muriel Bristol claimed to Sir Ronald Fisher that she could tell which was poured first just by tasting the tea in the cup. 
# 
# To test her claim, Fisher provided eight cups of tea, four with the tea poured first and four with the milk poured first. Apart from this the cups and contents were identical. Muriel Bristol was asked to taste the tea in each cup and say whether milk or tea had been poured first. This experiment of [The Lady Tasting Tea](https://en.wikipedia.org/wiki/Lady_tasting_tea) became one of the pillars of modern science.
# 
# Fisher's colleagues reported that the lady identified all eight cups correctly. 
# 
# **a)** The lady knew that there were four cups of each kind, so if she had just picked four at random for the "milk first" group, how likely was she to pick the right four? 
# 
# **b)** Was the result statistically significant? As you know, the definition of statistical significance was also due to Fisher.

# **11.**
# A company that makes robots has 12 new robots all designed for the same task.
# 
# The company times all the robots as they complete their tasks. Then it modifies each robot's mechanism. After the modificiation, it times the robots again as they complete their tasks.
# 
# Assume that the first and second times for Robot $i$ are $(X_i, Y_i)$ and that the pairs $(X_1, Y_1), (X_2, Y_2), \ldots, (X_{12}, Y_{12})$ are i.i.d.
# 
# You can also assume that time is measured with enough precision that no two times come out exactly equal.
# 
# Nine out of the 12 robots performed faster after modification. Come with hypotheses that you can test to see whether the modifications did nothing or whether they made the robots faster. Perform the test at the 5% level and provide your conclusion. The test is called the *sign test* because it is based on the signs of the differences $D_i = Y_i - X_i$.

# **12.**
# A survey organization takes a simple random sample of 400 adults in a city. The annual incomes of the sampled people have an average of 68,000 dollars and an SD of 40,000 dollars.
# 
# **a)** Fill in the blank with one of the words "sample" or "city".
# 
# The interval "68,000 dollars $\pm$ 4,000 dollars" is an approximate 95% confidence interval for the average annual income of adults in the $\underline{~~~~~~~~~~~~~~~~~~~~~}$.
# 
# **b)** Pick all of the correct options and justify your choices. More than one option may be correct.
# 
# The normal curve used in the construction of the confidence interval in Part **a** is the distribution of
# 
# (i) the incomes of the adults in the city
# 
# (ii) the incomes of the adults in the sample
# 
# (iii) the averages of all possible simple random samples of 400 adults from the city
# 
# (iv) probabilities for how the average of a simple random sample of 400 adults from the city could come out
# 
# **c)** True or false (explain):
# 
# The incomes of approximately 95% of the adults in the city are in the range 68,000 dollars $\pm$ 4,000 dollars.
# 
# **d)** Fill in the blanks with the best choices you can make from the following set. You are welcome to use the same entry more than once.
# 
# - the average income of adults in the city
# - the average income of adults in the sample
# - 68,000 dollars
# - 40,000 dollars
# - 2,000 dollars
# 
# If you draw one adult at random from the city, that person's income has expectation equal to $\underline{~~~~~~~~~~~~~~~~~~~~~}$ and SD approximately equal to $\underline{~~~~~~~~~~~~~~~~~~~~~}$.
# 
# **e)** Fill in the blanks with the best choices you can make from the same set as in the previous part. Again you are welcome to use the same entry more than once.
# 
# If you draw a simple random sample of 400 adults from the city, the average income of the sampled adults has expectation equal to $\underline{~~~~~~~~~~~~~~~~~~~~~}$ and SD approximately equal to $\underline{~~~~~~~~~~~~~~~~~~~~~}$.

# In[ ]:




