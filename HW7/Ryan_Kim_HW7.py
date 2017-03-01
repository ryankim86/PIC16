# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 21:00:06 2017

@author: Ryan Kim
"""

"""
Challenge 1: Selection, Bubble, Quick, and Merge Sorts for real numbers
"""

"""
@function selection_sort: sorts numbers using selection sort. Selects the smallest value of subarrays and places them in the correct position. Time complexity O(N**2)
@param numList: a list of real numbers
@return : a list of sorted real numbers
"""
def select_sort(numList):
    
    # for each entry in the List
    for i in range(len(numList)):
        
        # start with storing the current item's index
        currentMin = i
        
        # check every element after that point
        for j in range(i,len(numList)):
            
            # if any value is less than the current minimum, update.
            if numList[j] < numList[currentMin]:
                currentMin = j
        
        # once second for loop ends, swap the two values
        if i != currentMin:
            numList[i], numList[currentMin] = numList[currentMin], numList[i]
    
    return numList

"""
@function bubble_sort: sorts numbers using Bubble Sort. Moves larger values up to the end. Time complexity O(N**2)
@param numList: a list of real numbers
@return : a list of real numbers sorted in nondecreasing order
"""
def bubble_sort(numList):
    
    for i in range(len(numList)):
        for j in range(i+1, len(numList)):
            
            # if the next element is smaller, then swap
            if numList[i] > numList[j]:
                numList[i], numList[j] = numList[j], numList[i]
    
    return numList
      
"""
@function merge_sort: sorts numbers using Merge Sort algorithm. Recursively divides List into halfs and then recreate them sorted. Time Complexity O(N*Log(N))
@param numList: a list of real numbers
@return : a list of real numbers sorted in nondecreasing order
"""
def merge_sort(numList):
    
    # recursive stopping condition. if half is just of size 1 or 0
    if len(numList) <= 1:
        return numList
        
    else:
        # create the two halves of the array
        mid = int(len(numList) / 2)
        left = numList[:mid]
        right = numList[mid:]
        
        # recursively call merge_sort on the two half of the arrays and merge them.
        return merge(merge_sort(left), merge_sort(right))
    
"""
@function merge: takes two sorted List and creates a sorted List using all of the elements in the original two Lists.
It acheives this by comparing the front of the two Lists and seeing which is smaller.
@param list1: a sorted list of real numbers
@param list2: a sorted list of real numbers
@return : sorted list created form the contents of list1 and list2
"""

def merge(list1, list2):
    
    sortedList = []
    
    firstIndex = 0
    secondIndex = 0
    while firstIndex < len(list1) or secondIndex < len(list2):
        
        # if one list was exhausted before the other, then append the rest
        if firstIndex >= len(list1):
            sortedList += list2[secondIndex:]
            secondIndex = len(list2)
        elif secondIndex >= len(list2):
            sortedList += list1[firstIndex:]
            firstIndex = len(list1)
            
        # otherwise, compare the "front" element, and select the smaller of the two
        elif list1[firstIndex] <= list2[secondIndex]:
            sortedList.append(list1[firstIndex])
            firstIndex += 1
        else:
            sortedList.append(list2[secondIndex])
            secondIndex += 1
            
    return sortedList
    
    
"""
@function quick_sort: sorts numbers using the Quick Sort algorithm. It achieves this by dividing list into two sections, using a pivot value. 
This value will be selected from one of the list values pseudo-randomly. Time complexity: average O(N*Log(N)); worst-case: O(N**2)
Adapted from implementation in 'Algorithms' by Sedgewick and Wayne (Originally written in Java)
@param numList: a list of numbers 
@return : a sorted list of numbers
"""
def quick_sort(numList):
    from random import shuffle
    
    # shuffle list for better pivot selection
    shuffle(numList)
    
    # call helper function to perform sort
    return quickSort(numList, 0, len(numList) - 1)
    
"""
@function quickSort: helper function o quick_sort. Performs the sorting logic.
@param numList: list of numbers
@param lo: lowest index in range
@param hi: highest index in range
@return sorted List of numbers
"""
def quickSort(numList, lo, hi):
    if hi >= lo:
    
        # find pivot
        pivotIndex = partition(numList, lo, hi)
        
        # sort the left and right sides using the pivot to split up the array
        quickSort(numList, lo, pivotIndex - 1)
        quickSort(numList, pivotIndex + 1, hi)
    
    return numList
    
    
"""
@function partition: partitions the list based on pivot; all values to the left of the pivot will be less than or equal. And all values right will be greater than or equal
@param numList: a list of numbers
@param pivot: a real number, will be used to divide numList into two parts
@return : index of the pivot that partitioned numList
"""
def partition(numList, lo, hi):
    # select first item to be pivot. Since List was presumably shuffled earlier, reduced chance of terrible pivot
    pivot = numList[lo]
    
    index1 = lo + 1
    index2 = hi
    
    # if list of size 2, just do simple swap
    if index1 >= index2:
        if pivot > numList[index2]:
            numList[lo], numList[index2] = numList[index2], numList[lo]
            return index2
        else:
            return lo
    
    while True:

        # start from left side of the list
        while numList[index1] <= pivot and index1 <= index2:
            # keep going until we find an element larger than the pivot
            index1 += 1
            
            # stop if left index reaches the end
            if index1 == hi:
                break

        # do the same starting from the end of the list. find a value that is less than the pivot
        while numList[index2] >= pivot and index2 >= index1:
            index2 -= 1
            
            if index2 == lo:
                break

        # if left and right indices ever cross, stop
        if index1 >= index2:
            break
        
        # swap the value of the two indices that are on the wrong side
        else:
            numList[index1], numList[index2] = numList[index2], numList[index1]
        
    # put pivot in the correct position
    numList[lo], numList[index2] = numList[index2], numList[lo]
        
    # return index of pivot
    return index2
    
"""
End Challenge 1
"""

"""
Challange 2
"""

"""
@function performanceTest: plots the times for sorting of the four sorting algorithms implemented in Challenge 1
@param n: natural number. Will be the highest size of data we consider in performance test
#param k: natural numer. Number of trials done for each length of trial data
@return will display a plot of the different times for the four different sorts
"""
def performanceTest(n, k):
    import random
    import matplotlib.pyplot as plt
    import time
    
    # create a datapoint for a dataset of size 1, 2, 3, ... up to size n
    for i in range(0,n):
        
        selectionTime = 0
        bubbleTime = 0
        mergeTime = 0
        quickTime = 0
        
        # will run the test k times per sort
        for _ in range(k):
            
            # create a list of n natural numbers
            randList = random.sample(range(0,i), i)

            # test Bubble Sort
            start = time.perf_counter()
            bubble_sort(randList)
            end = time.perf_counter()
            bubbleTime += (end - start)
            
            # create a list of n natural numbers
            randList = random.sample(range(0,i), i)
            
            # test selection Sort
            start = time.perf_counter()
            select_sort(randList)
            end = time.perf_counter()
            selectionTime += (end - start)
            
            # create a list of n natural numbers
            randList = random.sample(range(0,i), i)
            
            # test merge Sort
            start = time.perf_counter()
            merge_sort(randList)
            end = time.perf_counter()
            mergeTime += (end - start)
            
            # create a list of n natural numbers
            randList = random.sample(range(0,i), i)
            
            # test quick Sort
            start = time.perf_counter()
            quick_sort(randList)
            end = time.perf_counter()
            quickTime += (end - start)
            
        # average sorting times
        bubbleTime /= k
        selectionTime /= k
        mergeTime /= k
        quickTime /= k
        
        if i == n-1:
            plt.plot(i, bubbleTime, 'o', color = 'blue', label = 'Bubble Sort')
            plt.plot(i, selectionTime, 'o', color = 'red', label = 'Selection Sort')
            plt.plot(i, mergeTime, 'o', color = 'orange', label = 'Merge Sort')
            plt.plot(i, quickTime, 'o', color = 'purple', label = 'Quick Sort')
        else:
            plt.plot(i, bubbleTime, 'o', color = 'blue')
            plt.plot(i, selectionTime, 'o', color = 'red')
            plt.plot(i, mergeTime, 'o', color = 'orange')
            plt.plot(i, quickTime, 'o', color = 'purple')

    
    plt.xlim([-1, n])
    plt.legend(loc = 'upper right')
        
    plt.xlabel('List Length (' + str(k) + ' trials per Length)' )
    plt.ylabel('Time')
            
    return

"""
End Challange 2
"""

"""
Challenge 3
"""

N=[[0,3,1,0,0,6],[3,0,1,1,0,0],[1,1,0,0,2,0],[0,1,0,0,1,2],[0,0,2,1,0,1],[6,0,0,2,1,0]]

"""
@function dijkstra_shortestpath: calculates the shortest path from v to w
Based off pseudocode from: https://en.wikipedia.org/wiki/Dijkstra's_algorithm
@param N: numpy array representing the network to find path 
@param v: index of start vertex
@param w: index of end vertex
@return : list containing the shortest path from v to w. If no such path exists, it will return an empty list

"""
def dijkstra_shortestpath(N, v, w):
    import numpy as np
    
    N = np.array(N)
    
    # create a dictionaries to keep track of nodes
    distance = {v:0}
    prevNode = {}
    Q = [v]
    
    # store unvisited nodes. 
    for i in range(len(N)):
        if i != v:
            """
            -1 in place of infinity. Technically, bad practice, but 
            should work because alg. only works for positives weights.
            """
            distance[i] = -1
            Q.append(i)
    
    currNode = v
    
    while len(Q) != 0:
        
        # find vertex with minimum distance
        nonInfiniteNodes = []
        for value in Q:
            if distance[value] != -1: 
                nonInfiniteNodes.append(value)
        currNode = min(nonInfiniteNodes)
        
        # node has been visisted
        Q.remove(currNode)
        
        # find neighbors of u:
        neighbors = []
        for i in range(len(N[currNode])):
            if N[currNode, i] > 0:
                neighbors.append(i)
        
        # look at the neighbors of the current node
        for node in neighbors:
            
            # calculate the distance from start to neighbor on THIS path
            alt = distance[currNode] + N[currNode, node]
            
            # if path distance has been set previously
            if distance[node] != -1:
                # if this new distance is less than currently stored distance, replace
                if alt < distance[node]:
                    distance[node] = alt
                    prevNode[node] = currNode
                    
            # if no distance path has been calculated previously, set distance
            else:
                distance[node] = alt
                prevNode[node] = currNode
    
    # recreate the path going through the previous nodes
    path = []
    trackNode = w
    
    # if no prev node defined for the
    if trackNode not in prevNode:
        return []
    
    # keep going through shortest path's previous nodes until we get to beginning
    while trackNode in prevNode:
        path.insert(0, trackNode)
        trackNode = prevNode[trackNode]
        
    # if never make it to the start, no path exists
    if trackNode != v:
        return []
    # otherwise, add the start node back in.
    else:
        path.insert(0, trackNode)
            
    return path