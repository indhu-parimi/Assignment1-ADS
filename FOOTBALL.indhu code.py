#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import python libraries
# importing pandas library
import pandas as pd
# importing matplotlib library
import matplotlib.pyplot as plt
# calling the csv file to read
# load dataset
data_set = pd.read_csv("wc_matches.csv")
# printing the dataset
data_set


# In[2]:


# pre-processing process
data_set.isnull().sum()


# In[3]:


# describe info from dataset
data_set.info()


# In[4]:


# defining the functions
def plot_lines(x, k):

    data = data_set
    # indexing the team
    data = data.set_index("team1")
    # set the index and lock it so there will bew no changes in it
    data_set1 = data.loc[[x]]
    # reset the index as team1
    data_set1 = data_set1.reset_index(level="team1")
    # groupby the data set
    data_set1 = data_set1.groupby("team1")
    # give input x-axis and y-axis
    data_set1.plot(x="team2", y=["adj_score1", "proj_score1", "proj_score2",
                   "adj_score2", "score1", "score2"], kind=k, figsize=(7, 5))
    plt.title("Adjacent score, projected score and score of teams againt {}".format(
        x)) 
    # print title name

    plt.legend(loc=(1.1, 0.2))
    plt.show()


# In[5]:


# print lineplot
plot_lines("Argentina", "line")


# In[6]:


# create fun and import bar plot
def bar_plot():
    data_set2 = data_set
    data_set2 = data_set2.groupby(["team1", "team2", "date"]).sum()  # group by
    data_set2 = data_set2.drop(["league_id", "spi1", "spi2", "prob1", "prob2", "probtie", "proj_score1",
                               "proj_score2", "xg1", "xg2", "nsxg1", "nsxg2", "adj_score1", "adj_score2"], axis=1) 
    # drop by
    # plotting bar chart
    data_set2.plot(kind="bar", figsize=(15, 5))
    plt.show()  # show visulization fun


bar_plot()


# In[7]:


# calling the function from the above defined function
plot_lines("Croatia", "box")


# In[ ]:
