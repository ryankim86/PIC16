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

def happiness(englishText):
    
    fid = open('/home/ryan/Documents/PIC16/happiness_dictionary.txt','r')
    txt = fid.read()
    exec(txt, globals())
    
    numMatchedWordsInDict = 0
    rawHappinessScore = 0
    p = re.compile('([A-Za-z]+)[\s-]?')
    matches = p.findall(englishText)
    
    for match in matches:
        if match.lower() in happiness_dictionary:
            numMatchedWordsInDict+=1
            rawHappinessScore+=happiness_dictionary[match.lower()]
    if numMatchedWordsInDict == 0:
        return 0
    else:
        return (rawHappinessScore / numMatchedWordsInDict)

#fid = open('/home/ryan/Documents/PIC16/HW4/GulTravel.txt','r')
#Rtxt = fid.read()

def story_arc(story):
    
    # parse through string and separate words 
    p = re.compile('([A-Za-z]+)[\s-]?')
    matches = p.findall(story)
        
    # passStrings will be passed into the happiness function to calculate a happiness score.
    passString1 = ""
    passString2 = ""
    counter = 0
    counter2 = 0
    
    x = []
    y = []
    
    # a data point will be every 50 words
    for match in matches:
        if counter2 <= 24:
            passString1 += match
        elif counter2 >= 25 and counter2 < 50:
            passString1 += " " + match
            passString2 += " " + match
        elif counter2 == 50:
            x.append(counter)
            counter += 10
            y.append(happiness(passString1))
            counter2 = 24
            passString1 = passString2
            passString2 = ""
        counter2 += 1
    
    plt.xlim([-50, counter + 50])
    plt.ylim([4,6])
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
    