#!/usr/bin/env python
# coding: utf-8

# # Inference #

# In probability theory, we are interested in outcomes of experiments that involve chance. We start with a probabilistic *model*, which is a set of assumptions about the chances governing the experiment. We can then calculate probabilities for how the experiment could come out. 
# 
# Statistical inference works in the opposite order. We start with observed outcomes of an experiment. We then try to work backwards to make *inferences* about the experiment that led to the observed outcomes. That is, we try to make conclusions about the chance processes that generated the data.
# 
# Data 8 addresses several questions of statistical inference, using simulation and the bootstrap as its primary methods. In particular, it covers *tests of hypotheses* about the process that generated the data, and also *estimation* of unknown parameters of that process. In this chapter we address the same questions with a more theoretical perspective.
