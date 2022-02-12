#!/usr/bin/env python
# coding: utf-8

# # Rules
# 
# - We will grade only the answer cells, so make sure that you type your answer inside of the answer cell. 
# 
# - Make sure that your code is working when you restart the kernel. Notebooks are great tools for exploration but we should be very careful as we are writing codes. For more, please check: [Why notebooks suck](https://towardsdatascience.com/5-reasons-why-jupyter-notebooks-suck-4dc201e27086)
# 
# - Make sure that your results are in the correct format. If we ask you to return a list, your answer should be in a list format. If the question asks you to return a scalar (float, int, etc.) then make sure that your answer is in the correct format.
# 
# ## Homework
# 
# 1. Correct the formatting of markdown cells
#     * Use appropriate headers
# 1. Finish the coding sections.

# Question-1
# 
# Write a Python function to return a **list** of all the numbers from 1 to n which are divisible by 5. `n` will be given as an argument to your function.
# 

# In[1]:


# Your Answer Cell
# you can edit the function below. 
# Don't change function name and parameter names.
# you can define new variables (if needed) inside of the function.

def divisible_five(given_number):
    my_list=[]
    for a in range(1, given_number+1):
        if a%5==0:
            my_list.append(a)
    return my_list

divisible_five(121)


# Question-2
# 
# Write a function that returns the sum of the parameters
# 

# In[2]:


# Your Answer Cell
# you can edit the function below. 
# Don't change function name and parameter names.
# you can define new variables inside of the function.

def my_function(a, b):

    return(a+b)


## your answer above

my_function(3, 5)


# Question-3 (Shell & Magic Commands)
# 

# Question-3-a
# 
# Below print current working directory.

# In[2]:


## Answer Cell 
get_ipython().run_line_magic('pwd', '')


# Question-3-b
# 
# Below list all the files and folders in the current working directory.

# In[4]:


## Answer Cell
get_ipython().run_line_magic('ls', '')


# Question-3-c
# 
# Create 'my_script.py' that prints 'Your First Name-Your Last Name' in the same directory and run this scripy in the cell below.

# In[5]:


## Answer Cell
get_ipython().run_line_magic('echo', 'print("Bharath kumar Putturu") > my_script.py')
get_ipython().system('python my_script.py')


# In[ ]:




