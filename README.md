# Final Project
 
Analyzing and determining which box score stat contributes most towards 
baseball WAR using visualizations and a regression model.

All data used is extracted from pybaseball batting_stats and pitching_stats.

## Method

Using MLB data from 2018-2022, I split WAR into two categories:
                        Pitching and Batting.

I created new DataFrames which include WAR for the given player and season,
as well as many common box score statistics.

I split the DataFrames into smaller categorical DataFrames in order to 
compare and visualize which metrics in each category were most correlated 
to WAR. This was done using a matrix plot and a regression model.

After choosing the best one or two statistics from each category,
I created a new DataFrame with the strongest correlated statistics.

I made one last matrix plot to see whether it would be clear which statistics
stood out as the most correlated to WAR, then I made a correlation matrix
to truly know which statistics was most positively correlated to WAR.

## Comparing Time Frames

I extracted MLB data from 1871-2000 to see if the statistics most correlated
to WAR is the same as it was earlier in history.

I made a correlation matrix and found out that with batting data, 
the statistics most correlated to WAR were different than the past five years.

## Created by Tate Williams at Syracuse University

 
