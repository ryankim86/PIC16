# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 22:31:31 2017

@author: Ryan Kim
"""


def scatterPlot():
    import matplotlib.pyplot as plt
    import pandas as pd
    
    # grab win data by team for years after 2000. Data is from Lahman's Baseball Database
    teams = pd.read_csv('Teams.csv')
    teams = teams[teams['yearID'] == 2012]
    teams = teams[['yearID', 'teamID', 'W']]
    
    # set index for easier look up
    teams = teams.set_index(['yearID', 'teamID'])
    
    playerSalaries = pd.read_csv('Salaries.csv')
    
    # add up player salaries
    salariesByYearAndTeam = playerSalaries.groupby(['yearID', 'teamID'])['salary'].mean()

    # add summed salaries to team data
    teams = teams.join(salariesByYearAndTeam)    
    
    # plot wins
    plt.plot(teams['salary'][2012], teams['W'][2012], 'o')
    
    # adjust plot settings
    plt.ylim([50,100])
    plt.title('Average Player Salary vs Wins in MLB (2012)')
    plt.xlabel('Average Player Salary (USD)')
    plt.ylabel('Number of Wins in Season')
    plt.grid(True)
    
    return

def histogram():
    
    