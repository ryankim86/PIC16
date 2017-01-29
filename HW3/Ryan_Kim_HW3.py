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

"""
Using Data from https://snap.stanford.edu/data/email-Eu-core.html
Which is a dataset that represents communication between members of a large European research institution via email
Data contains entries of sender, recepient, timestamp
"""
#TODO: Make this entire process more efficient. Find a better way to organize nodes (maybe). Add directness. Find way to isolate nodes with no emails sent.
# or instead of directed, just aggregate total emails.
def network():
    import numpy as np
    import matplotlib.pyplot as plt
    
    
    # we know that the network has 90 nodes
    emailNetworkMatrix = np.zeros([90,90])
    
    # matrix will be such that entry i,j will hold the number of emails from person i to person j
    with open('email-Eu-core-Dept3.txt') as input_file:
        for line in input_file:
            emailers = line.split()
            """ 
            using the fact that the participants are given ID numbers that are integers,
            increment the value of entry i,j when person i sent an email to person j           
            """
            emailNetworkMatrix[int(emailers[0])][int(emailers[1])] +=1
    
    x=[i for i in range(90)]
    y=[i for i in range(90)]

    for i in range(90):	
        if i <= 45:
            x[i] = i
        else:
            x[i] = i - 45
        #x[i]=np.cos(2*np.pi*i/90) * 5
    for i in range(90):	
        if i <= 45:
            y[i] = 30
        else:
            y[i] = 60
        
    plt.ylim([-10,110])
    plt.xlim([-5,50])
    
    for i in range(90):
        for j in range(90):
            if emailNetworkMatrix[i][j] is not 0:
                if y[i] == y[j]:
                    y[j] += np.random.random_integers(-15, 15)
    
    for i in range(90):
        for j in range(90):
            plt.plot([x[i],x[j]], [y[i], y[j]], linewidth = emailNetworkMatrix[i][j] / 30, linestyle = '-', color = 'cyan')
            
    plt.plot(x,y,'o', color = 'gold', markersize = 5)
    
    return
    