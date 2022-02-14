#!/usr/bin/env python
# coding: utf-8

# ## Homework 2
# 
# Please complete the functions below. These functions are for to simulate a fair and a biased die. 
# 
# The biased die has probabilities {0.20, 0.10, 0.15, 0.15, 0.15, 0.25}.
# 
# Create 2 visualizations that shows outcomes of multiple rolls of a fair die and biased die. 
# * Visualization for fair die
# * Visualization for biased die
# 
# Repeat the process programatically and take the mean to create a new list. This list will be used to compare means of biased & unbiased dice. 
# * Create a historgram showing means of biased & unbiased die
# 
# * Use subcharts
# * All visualizations must have appropriate titles.
# * There are 3 visualization and expected format is 
# ```
#  [V1] [V2]
#  [   V3  ]
#  ```

# In[ ]:


import random 
import matplotlib.pyplot as plt

trial_count = 500

def fair_die_simulation(trials):
    """
    returns an array of randomly numbers between 1 and 6. 
    """
    
    options = [1,2,3,4,5,6]
    simulations = []
    return simulations


# In[ ]:


def biased_die_simuations(trials, weights=[0.25, 0.15, 0.15, 0.15, 0.15, 0.15]):
    """
    returns an array of randomly numbers between 1 and 6 with the probabilty of assosiated weight. 
    for instance: for weights: [0.25, 0.15, 0.15, 0.15, 0.15, 0.15]
    1 has 0.25 change to be selected, 2 has 0.15 chance and so on...
    """
    
    options = [1,2,3,4,5,6]
    simulations = []
    return simulations


# In[ ]:





# In[ ]:


biased = biased_die_simuations(trial_count)
fair = fair_die_simulation(trial_count)

# biased_mean_list = ...
# unbiased_mean_list = ...


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




