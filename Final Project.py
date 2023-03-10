#!/usr/bin/env python
# coding: utf-8

# In[67]:


from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
from pybaseball import batting_stats
from pybaseball import pitching_stats
from pybaseball import lahman
lahman.download_lahman()
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'notebook')
import seaborn as sns


# In[80]:


# All box score pitching stats with WAR from 2018-2022
pitching_data = pitching_stats(2018,2022)
pitcher_WAR_data = pitching_data[['Season', 'Name', 'Team', 'Age', 'W', 'L', 'WAR', 'ERA', 'G', 'GS', 'CG', 'ShO', 'SV', 'BS', 'IP', 'H', 'R', 'ER', 'HR', 'BB', 'HBP', 'SO']]
pitcher_WAR_data


# In[81]:


# Creating separate pitching DataFrames to represent different types of stats
pitcher_wins_saves = pitcher_WAR_data[['WAR', 'W', 'L', 'SV', 'BS']]
pitcher_games_innings = pitcher_WAR_data[['WAR', 'G', 'GS', 'CG', 'ShO', 'IP']]
pitcher_era = pitcher_WAR_data[['WAR', 'H', 'HR', 'R', 'ER', 'ERA']]
pitcher_strikeouts = pitcher_WAR_data[['WAR', 'SO', 'BB', 'HBP']]


# In[82]:


# Pitcher_wins_saves matrix plot
sns.pairplot(pitcher_wins_saves, diag_kind = 'kde', kind='reg', plot_kws={'line_kws':{'color':'red'}, 
                                                                          'scatter_kws':{'alpha':0.2}})
# Wins are most correlated in this group


# In[83]:


# Pitcher_games_innings matrix plot
sns.pairplot(pitcher_games_innings, diag_kind = 'kde', kind='reg', plot_kws={'line_kws':{'color':'red'}, 
                                                                          'scatter_kws':{'alpha':0.2}})
# Games, Games Started, and Innings Pitched are most correlated in this group


# In[84]:


# Pitcher_era matrix plot
sns.pairplot(pitcher_era, diag_kind = 'kde', kind='reg', plot_kws={'line_kws':{'color':'red'}, 
                                                                          'scatter_kws':{'alpha':0.2}})
# Hits are most correlated in this group, but are not a clear positive correlation


# In[85]:


# Pitcher_strikeouts matrix plot
sns.pairplot(pitcher_strikeouts, diag_kind = 'kde', kind='reg', plot_kws={'line_kws':{'color':'red'}, 
                                                                          'scatter_kws':{'alpha':0.2}})
# Strikeouts are most correlated in this group


# In[90]:


# New DataFrame with the most correlated stats to pitching WAR
pitcher_WAR_corr = pitcher_WAR_data[['Name', 'WAR', 'W', 'G', 'GS', 'IP', 'SO']]
pitcher_WAR_corr


# In[91]:


# Matrix plot of most correlated stats to pitching WAR
sns.pairplot(pitcher_WAR_corr, diag_kind = 'kde', kind='reg', plot_kws={'line_kws':{'color':'red'}, 
                                                                          'scatter_kws':{'alpha':0.2}})
# Visually it seems as if Wins and Strikeouts are most positively correlated


# In[96]:


# Correlation matrix to determine which stat is most positively correlated
pitcher_WAR_corr.corr()

# Strikeouts is 77.83% correlated to WAR which is the most among box score statistics


# In[98]:


# All box score batting stats with WAR from 2018-2022
batting_data = batting_stats(2018,2022)
batter_WAR_data = batting_data[['Season', 'Name', 'Team', 'Age', 'WAR', 'G', 'AB', 'PA', 'H', '1B', '2B', '3B', 'HR', 'R', 'RBI', 'BB', 'SO', 'HBP', 'SB', 'AVG', 'OBP', 'SLG', 'OPS']]
batter_WAR_data


# In[99]:


# Creating separate batting DataFrames to represent different types of stats
batter_bip = batter_WAR_data[['WAR', 'H', '1B', '2B', '3B', 'HR']]
batter_games = batter_WAR_data[['WAR', 'G', 'AB', 'PA', 'R', 'RBI']]
batter_averages = batter_WAR_data[['WAR', 'AVG', 'OBP', 'SLG', 'OPS']]
batter_non_bip = batter_WAR_data[['WAR', 'SO', 'BB', 'HBP', 'SB']]


# In[100]:


# Batter_bip matrix plot
sns.pairplot(batter_bip, diag_kind = 'kde', kind='reg', plot_kws={'line_kws':{'color':'red'}, 
                                                                          'scatter_kws':{'alpha':0.2}})
# Hits and Homeruns are most correlated in this group


# In[101]:


# Batter_games matrix plot
sns.pairplot(batter_games, diag_kind = 'kde', kind='reg', plot_kws={'line_kws':{'color':'red'}, 
                                                                          'scatter_kws':{'alpha':0.2}})
# Most of these stats are strongly correlated to WAR, but it seems like Runs and RBIs are slightly more correlated to WAR


# In[102]:


# Batter_averages matrix plot
sns.pairplot(batter_averages, diag_kind = 'kde', kind='reg', plot_kws={'line_kws':{'color':'red'}, 
                                                                          'scatter_kws':{'alpha':0.2}})
# OBP and OPS are most correlated in this group


# In[103]:


# Batter_non_bip matrix plot
sns.pairplot(batter_non_bip, diag_kind = 'kde', kind='reg', plot_kws={'line_kws':{'color':'red'}, 
                                                                          'scatter_kws':{'alpha':0.2}})
# Walks are most correlated in this group


# In[104]:


# New DataFrame with the most correlated stats to batting WAR
batter_WAR_corr = batter_WAR_data[['Name', 'WAR', 'H', 'HR', 'R', 'RBI', 'BB', 'OBP', 'OPS']]
batter_WAR_corr


# In[108]:


# Matrix plot of most correlated stats to batting WAR
sns.pairplot(batter_WAR_corr, diag_kind = 'kde', kind='reg', plot_kws={'line_kws':{'color':'red'}, 
                                                                          'scatter_kws':{'alpha':0.2}})
# Visually it seems as if Runs and OPS are most positively correlated


# In[107]:


# Correlation matrix to determine which stat is most positively correlated
batter_WAR_corr.corr()

# Runs is 71.44% correlated to WAR which is the most among box score statistics


# In[128]:


# Pitching data from 1871-2000
all_pitching_data = pitching_stats(1871, 2000)
all_pitcher_WAR_data = all_pitching_data[['Name', 'WAR', 'W', 'L', 'ERA', 'G', 'GS', 'CG', 'ShO', 'SV', 'BS', 'IP', 'H', 'R', 'ER', 'HR', 'BB', 'HBP', 'SO']]
all_pitcher_WAR_data


# In[129]:


# Correlation matrix for pitching WAR
all_pitcher_WAR_data.corr()

# Strikeouts  is still most correlated at 69.71% with Wins close behind at 68.09%


# In[124]:


# Batting data from 1871-2000
all_batting_data = batting_stats(1871, 2000)
all_batter_WAR_data = all_batting_data[['Name', 'WAR', 'G', 'AB', 'PA', 'H', '1B', '2B', '3B', 'HR', 'R', 'RBI', 'BB', 'SO', 'HBP', 'SB', 'AVG', 'OBP', 'SLG', 'OPS']]
all_batter_WAR_data


# In[126]:


# Correlation matrix for batting WAR
all_batter_WAR_data.corr()

# Runs is less correlated than OBP, SLG, and OPS which is 73.16% correlated to WAR


# In[ ]:




