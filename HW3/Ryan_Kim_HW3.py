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
    teams = teams[['teamID', 'W']]
    
    # set index for easier look up
    teams = teams.set_index(['teamID'])
    
    playerSalaries = pd.read_csv('Salaries.csv')
    
    # add up player salaries
    salariesByTeam = playerSalaries[playerSalaries['yearID'] == 2012]
    salariesByTeam = salariesByTeam.groupby(['teamID'])['salary'].mean()

    # add summed salaries to team data
    teams = teams.join(salariesByTeam)    
    
    # plot wins
    plt.plot(teams['salary'], teams['W'], 'o')
    
    # adjust plot settings
    plt.ylim([50,100])
    plt.title('Average Player Salary vs Wins in MLB (2012)')
    plt.xlabel('Average Player Salary (USD)')
    plt.ylabel('Number of Wins in Season')
    plt.grid(True)
    
    return

def histogram():
    import matplotlib.pyplot as plt
    import pandas as pd
    
    battingData = pd.read_csv('Batting.csv')

    battingData = battingData[battingData['yearID'] == 2012]
    
    # some rows do not have run data, so only take ones with finite values 
    battingData = battingData['R']

    # plot histogram
    bins = plt.hist(battingData, bins= 13, range = [0, battingData.max()], color = ['crimson'])
    
    # extract values to create a curve following histogram bins
    binValue = bins[0]
    binCenters = .5 * (bins[1][1:]+bins[1][:-1])
    plt.plot(binCenters, binValue, linewidth = 2, linestyle = '--', color = 'cyan')
    
    plt.title('Player Runs (2012)')
    plt.xlabel('Number of Runs')
    plt.ylabel('Number of Players (Frequency)')
    plt.grid(True)
    plt.show()
    
    return
    