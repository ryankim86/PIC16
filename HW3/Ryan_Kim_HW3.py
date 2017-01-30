# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 22:31:31 2017

@author: Ryan Kim
"""

# begin Problem 1

def scatterPlot():
    import matplotlib.pyplot as plt
    import pandas as pd
    
    # grab win data by team for 2012. Data is from Lahman's Baseball Database
    teams = pd.read_csv('Teams.csv')
    teams = teams[teams['yearID'] == 2012]
    teams = teams[['teamID', 'W']]
    
    # set index for easier look up
    teams = teams.set_index(['teamID'])
    
    playerSalaries = pd.read_csv('Salaries.csv')
    
    # average player salaries
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
    
# end Problem 1

# begin Problem 2

"""
Using Data from https://snap.stanford.edu/data/email-Eu-core.html
Which is a dataset that represents communication between members of a large European research institution via email
Data contains entries of sender, recepient, timestamp
"""
#TODO: Make this process by using only aggregate emails so less iteration has to happen when plotting (maybe)
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
    
    # create nodes
    x = []
    y = []

    for i in range(90):	
        if i <= 45:
            x.append(i)
            y.append(30)
        else:
            x.append(i - 45)
            y.append(60)
            
    # set up plot
    plt.ylim([-10,110])
    plt.xlim([-5,50])
    plt.title('Email Communication in a Euro Research Institution')
    plt.tick_params(
        axis = 'both',
        which = 'both',
        left = 'off',
        labelleft = 'off',
        right = 'off',
        bottom = 'off',
        top = 'off',
        labelbottom ='off'
    )
    
    # shuffle the y values a little
    for i in range(90):
        for j in range(90):
            if emailNetworkMatrix[i][j] is not 0:
                if y[i] == y[j]:
                    y[j] += np.random.random_integers(-1,1)*np.random.random() * 15
    
    # plot everything
    for i in range(90):
        for j in range(90):
            plt.plot([x[i],x[j]], [y[i], y[j]], linewidth = emailNetworkMatrix[i][j] / 30, linestyle = '-', color = 'cyan')
        plt.annotate(str(i), (x[i], y[i]), xytext = (x[i]+0.25,y[i]+0.25))
            
    plt.plot(x,y,'o', color = 'gold', markersize = 11)
    
    return

# end Problem 2

# begin Problem 3

# creates Sierpinski's Triangle
def turtleFractal(order, length):
    import turtle as turt
    
    # set speed so drawing doesn't get pedantic
    turt.speed('fastest')

    # base case, draw a triangle
    if order == 0:
        for i in range(3):
            turt.forward(length)
            turt.left(120)
    # otherwise, recursively call for three smaller triangles to be made
    else:        
        # create left corner triangle
        turtleFractal(order - 1, length / 2)
        
        # move over to create right corner triangle
        turt.forward(length / 2)
        turtleFractal(order - 1, length / 2)
        
        # move over to create top triangle
        turt.left(120)
        turt.forward(length / 2)
        turt.right(120)
        turtleFractal(order - 1, length / 2)
        
        # return to original position
        turt.right(120)
        turt.forward(length / 2)
        turt.left(120)

# end Problem 3

# begin Problem 4
def prettyColors():
    import matplotlib.pyplot as plt
    
    # create 256 x 128 grid
    clrs = [[[0,0,0] for j in range(128)] for _ in range(256)]
    
    # red
    for i in range(32):
        for j in range(4):
            for k in range(256):
                clrs[k][i*4+j][0]=i/31.0
            
    # green
    for i in range(32):
        for j in range(8):
            for k in range(128):
                clrs[i*8+j][k][1]=i/31.0
    # blue 
    blue = [[0,1,2,3], 
            [4,5,6,7],
            [8,9,10,11],
            [12,13,14,15],
            [16,17,18,19],
            [20,21,22,23],
            [24,25,26,27],
            [28,29,30,31]]
        
    for i in range(256):
        for j in range(128):
            clrs[i][j][2] = blue[i%8][j%4] / 31.0
                
    # set up plot
    plt.tick_params(
        axis = 'both',
        which = 'both',
        left = 'off',
        labelleft = 'off',
        right = 'off',
        bottom = 'off',
        top = 'off',
        labelbottom ='off'
    )
    
    # display
    plt.imshow(clrs)
    return
# end Problem 4
