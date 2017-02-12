# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 11:02:32 2017

@author: Ryan Kim
"""

import matplotlib.pyplot as plt
import numpy as np
import re

# defining a global variable
happiness_dictionary = {}

"""
Challenge 1: will plot the happiness arc of a story.
This quantity can be changed by adjusting the 'initialWordsPerBlock' variable in function body.
@param story: A story in string format
"""
def story_arc(story):
    
    # the first point will be this many words. All subsequent points will be the average of 1.50 times many more words
    initialWordsPerBlock = 400
    x = []
    y = []
    
    # open the happiness dictionary
    fid = open('/home/ryan/Documents/PIC16/happiness_dictionary.txt','r')
    txt = fid.read()
    exec(txt, globals())
    
    # parse through string and separate words 
    p = re.compile('([A-Za-z\']+)[\s-]?')
    matches = p.findall(story)     

    # counters
    numMatchedWordsInDict = 0
    prevHalfRawScore = 0
    rawHappinessScore = 0
    averagedScore = 0
    xCounter = 0
    
    # Lists for plotting
    x = []
    y = []
    
    # a data point will be every (1.5*initialWordsPerBlock) words
    for match in matches:
        # only count word if it is in the dictionary
        if match.lower() in happiness_dictionary:
            numMatchedWordsInDict += 1
            
            # calculate average after enough words counted
            if numMatchedWordsInDict == initialWordsPerBlock:
                
                # if it is the first (initialWordsPerBlock) words, then normal average
                if prevHalfRawScore == 0:
                    averagedScore = rawHappinessScore / numMatchedWordsInDict
                # otherwise, average with last half of the previous score so points are more continuous
                else:
                    averagedScore = (rawHappinessScore + prevHalfRawScore) / (1.50 * initialWordsPerBlock)
                    
                rawHappinessScore = 0
                prevHalfRawScore = 0
                
                #add points
                x.append(xCounter)
                y.append(averagedScore)
                
                # reset for new point
                numMatchedWordsInDict = 0
                xCounter += 1
                
            # keep track of the score of the last half of the previous block
            elif numMatchedWordsInDict >= (initialWordsPerBlock / 2):
                rawHappinessScore += happiness_dictionary[match.lower()]
                prevHalfRawScore += happiness_dictionary[match.lower()]
                
            # otherwise add word's happiness score to a running total
            else:
                rawHappinessScore+=happiness_dictionary[match.lower()]
                
    # plot
    plt.xlim([-50, xCounter + 50])
    plt.title('Story Happiness Arc')
    plt.ylim([int(min(y)),int(max(y))+1])
    plt.xlabel('Words in Blocks of ' + str(int(1.50*initialWordsPerBlock)))
    plt.ylabel('Happiness Score')
    plt.plot(x,y, '-')
    
    return
    
"""
Helper Function used for both Challenge 2 and 3. Will order vectors
@param vector: a vector or a List
@return rankVector: another vector of indices in order of nonincreasing rank
"""
def createRankVector(vector):
    tupleList = []   
    vectorRank = []
    
    # create tuples containing vector element value and index
    for i in range(len(vector)):
        tupleList.append((vector[i],i))

    # sort tuples based on vector component value
    tupleList.sort(reverse = True)

    # append indices into an array in order of vector[index]'s value
    for i in range(len(tupleList)):
        vectorRank.append(tupleList[i][1])
    
    return np.array(vectorRank)

"""
Challange 2: Calculates pagerank of a network
@param networkMatrix: A network in matrix form. Can be either a numpy array or a List of Lists
@return scoreVector: score vector of the network
@return rankVector: vector of indices of scoreVector in terms of nonincreasing score order
"""
def pagerank(networkMatrix): 
    
    # create transition matrix
    networkMatrix = np.array(networkMatrix, dtype = 'double')
    for i in range(len(networkMatrix)):
        columnSum = np.sum(networkMatrix[:,i])
        
        # if unconnected node, ignore
        if columnSum == 0:
            continue
        
        networkMatrix[:,i]/=columnSum

    # calculate eigenvectors and values
    eigVals, eigVecs = np.linalg.eig(networkMatrix)

    # find the value of the eigenvalue equal to 1 using the fact 1 is the greatest value
    eigValIndex = np.argmax(eigVals)
    
    # extract column containing the eigenvector we want
    vector = eigVecs[:,eigValIndex]
    
    # calculate eigenvector scale constant as 1/sum of the vector components so that our Probability Distriubtion is correct
    vector /= np.sum(eigVecs[:,eigValIndex])
    
    # return the eigenvector the list converted into a numpy array
    return vector, createRankVector(vector)
    
"""
Challenge 3: calculates the degree score of a network
@param networkMatrix: a network in matrix form
@return degreeVector: a vector containing the degrees of nodes in network
@return rankVector: a vector of indices of degreeVector in nonincreasing degree value
"""
def degree(networkMatrix):
    
    # cast into numpy array 
    networkMatrix = np.array(networkMatrix)
    
    degreeList = []
    
    # sum each row. Push result to a List
    for i in range(len(networkMatrix)):
        degreeList.append(np.sum(networkMatrix[i,:]))
    
    # return List cast as a numpy array and its associated rank vector
    return np.array(degreeList), createRankVector(degreeList)

"""
Challenge 4: plots degree/strength vs pagerank
This example will use data from: http://konect.uni-koblenz.de/networks/arenas-jazz
"""
def pageRankVsDegree():
    
    # we know that the network has 198 nodes
    messageNetworkMatrix = np.zeros([198,198])
    
    with open('jazz.txt') as input_file:
        for line in input_file:
            messageParticipants = line.split()
            # musicians are assigned integers from 1 to 198. If there exists edge, matrix[i-1][j-1] and matrix[j-1][i-1] equal 1
            messageNetworkMatrix[int(messageParticipants[0])-1][int(messageParticipants[1])-1] = 1
            messageNetworkMatrix[int(messageParticipants[1])-1][int(messageParticipants[0])-1] = 1
        
    pageRankVector = pagerank(messageNetworkMatrix)
    strengthVector = degree(messageNetworkMatrix)  
  
    # plot  
    plt.plot(strengthVector[0], pageRankVector[0],'o', color = 'gold', markersize = 11)
    plt.xlabel('Strength Centrality')
    plt.ylabel('PageRank Value')
    
    return

G=[[0,1,1,0],[1,0,1,0],[1,1,0,1],[0,0,1,0]]
v=0
w=3
k=20

"""
Challenge 5: calculates the number of paths of length k between two nodes
@param G: binary network matrix
@param v: index of node that is at the beginning of path
@param w: index of node that is at the end of path
@param k: path length desired
@return numberofPaths: number of paths of length k

"""
def number_paths(G, v, w, k):
    return np.linalg.matrix_power(G,k)[v][w]
    