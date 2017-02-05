# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 11:02:32 2017

@author: Ryan Kim
"""

import matplotlib.pyplot as plt
import numpy as np
import re

Zachary_network=[
[1,1,1,1,1,1,1,1,1,0,1,1,1,1,0,0,0,1,0,1,0,1,0,0,0,0,0,0,0,0,0,1,0,0],
[1,1,1,1,0,0,0,1,0,0,0,0,0,1,0,0,0,1,0,1,0,1,0,0,0,0,0,0,0,0,1,0,0,0],
[1,1,1,1,0,0,0,1,1,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,1,0],
[1,1,1,1,0,0,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[1,0,0,0,1,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[1,0,0,0,0,1,1,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[1,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[1,1,1,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[1,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1],
[0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,1,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[1,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[1,1,1,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
[0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
[1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,1],
[1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,1],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,1,0,1,0,0,1,1],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1,0,0,0,1,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,1,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,1],
[0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,0,0,0,0,0,1],
[0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,1],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,1,0,0,1,1],
[0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,0,0,1,1,1],
[0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,1,0,0,1,0,1,0,1,1,0,0,0,0,0,1,1,1,1,1],
[0,0,0,0,0,0,0,0,1,1,0,0,0,1,1,1,0,0,1,1,1,0,1,1,0,0,1,1,1,1,1,1,1,1]]


# defining a global variable
happiness_dictionary = {}

fid = open('/home/ryan/Documents/PIC16/HW4/GulTravel.txt','r')
Rtxt = fid.read()

def story_arc(story):
    
    # open the happiness dictionary
    fid = open('/home/ryan/Documents/PIC16/happiness_dictionary.txt','r')
    txt = fid.read()
    exec(txt, globals())
    
    # parse through string and separate words 
    p = re.compile('([A-Za-z]+)[\s-]?')
    matches = p.findall(story)        

    # counters
    numMatchedWordsInDict = 0
    prev25RawScore = 0
    rawHappinessScore = 0
    averagedScore = 0
    xCounter = 0
    scoreFloor = 9
    scoreCeiling = 0
    
    # A point will be 200 words. This value can be changed, and the rest of the code should adjust
    wordsPerBlock = 200
    
    # Lists for plotting
    x = []
    y = []
    
    # a data point will be every 50 words
    for match in matches:
        # only count word if it is in the dictionary
        if match.lower() in happiness_dictionary:
            numMatchedWordsInDict+=1
            
            if numMatchedWordsInDict == wordsPerBlock:
                
                # if it is the first 50 words, then normal average
                if prev25RawScore == 0:
                    averagedScore = rawHappinessScore / numMatchedWordsInDict
                # otherwise, average with last score so points are more continuous
                else:
                    averagedScore = (rawHappinessScore + prev25RawScore) / (1.50*wordsPerBlock)
                    
                # adjust plot y-range if necessary
                if averagedScore < scoreFloor:
                    scoreFloor = averagedScore
                if averagedScore > scoreCeiling:
                    scoreCeiling = averagedScore

                rawHappinessScore = 0
                prev25RawScore = 0
                
                #add points
                x.append(xCounter)
                y.append(averagedScore)
                
                # reset for new point
                numMatchedWordsInDict = 0
                xCounter += 1
                
            # keep track of the score of the last half of the previous block
            elif numMatchedWordsInDict >= (wordsPerBlock / 2):
                rawHappinessScore += happiness_dictionary[match.lower()]
                prev25RawScore += happiness_dictionary[match.lower()]
                
            # otherwise add word's happiness score to a running total
            else:
                rawHappinessScore+=happiness_dictionary[match.lower()]
    # plot
    plt.xlim([-50, xCounter + 50])
    plt.title('Story Happiness Arc')
    plt.ylim([int(scoreFloor),int(scoreCeiling)+1])
    plt.xlabel('Words in Blocks of ' + str(wordsPerBlock))
    plt.ylabel('Happiness Score')
    plt.plot(x,y, '-')
    
"""
Helper Function used for both Challenge 2 and 3
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
Challange 2
@param networkMatrix: A network in matrix form. Can be either a numpy array or a List of Lists
@return scoreVector: score vector of the network
@return rankVector: vector of indices of scoreVector in terms of nonincreasing score order
"""
def pagerank(networkMatrix): 
    
    # create transition matrix
    networkMatrix = np.array(networkMatrix, dtype = 'double')
    for i in range(len(networkMatrix)):
        columnSum = np.sum(networkMatrix[:,i])
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
Challenge 3
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

def pageRankVsDegree(networkMatrix):
    return

"""
Challenge 5
@param G: binary network matrix
@param v: index of node that is at the beginning of path
@param w: index of node that is at the end of path
@param k: path length desired
@return numberofPaths: number of paths of length k

"""
def number_paths(G, v, w, k):
    return np.linalg.matrix_power(G,k)[v][w]
    