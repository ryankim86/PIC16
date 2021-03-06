# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 21:00:06 2017

@author: Ryan Kim
"""

import sympy as sp

"""
Challenge 1: Selection, Bubble, Quick, and Merge Sorts for real numbers
"""

L=[2,7,4,9,2]

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
@function merge_sort: sorts numbers using the Merge Sort algorithm. Recursively divides List into halfs and then recreate them sorted. Time Complexity O(N*Log(N))
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
@function merge: Helper Function for merge_sort(). Takes two sorted List and creates a sorted List using all of the elements in the original two Lists.
It acheives this by comparing the front of the two Lists and seeing which is smaller and adding that to a new list. 
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
@function quickSort: helper function for quick_sort. Performs the sorting logic.
@param numList: list of numbers
@param lo: lowest index in range
@param hi: highest index in range
@return sorted List of numbers
"""
def quickSort(numList, lo, hi):
    
    # make sure indices make sense
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
    
    # otherwise, perform partitioning logic
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
    
    bubble = []
    select = []
    merge = []
    quick = []
    x = []
    
    # create a datapoint for a dataset of size 1, 2, 3, ... up to size n
    for i in range(0,n):
        
        selectionTime = 0
        bubbleTime = 0
        mergeTime = 0
        quickTime = 0
        
        # will run the test k times per sort
        for _ in range(k):
            
            # create a list of n natural numbers
            original = random.sample(range(0,i), i)
            
            randList = original

            # test Bubble Sort
            start = time.perf_counter()
            bubble_sort(randList)
            end = time.perf_counter()
            bubbleTime += (end - start)
            
            randList = original
            
            # test selection Sort
            start = time.perf_counter()
            select_sort(randList)
            end = time.perf_counter()
            selectionTime += (end - start)
            
            randList = original
            
            # test merge Sort
            start = time.perf_counter()
            merge_sort(randList)
            end = time.perf_counter()
            mergeTime += (end - start)
            
            randList = original
            
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
        
        x.append(i)
        bubble.append(bubbleTime)
        select.append(selectionTime)
        merge.append(mergeTime)
        quick.append(quickTime)
    
    # plot the times
    plt.plot(x, bubble, '-', color = 'blue', label = 'Bubble Sort')
    plt.plot(x, select, '-', color = 'red', label = 'Selection Sort')
    plt.plot(x, merge, '-', color = 'orange', label = 'Merge Sort')
    plt.plot(x, quick, '-', color = 'purple', label = 'Quick Sort')
    
    # set up plot
    plt.xlim([-1, n])
    plt.legend(loc = 'upper left')
    plt.title('Time Performance of Sorting Algorithms')
    plt.xlabel('List Length (' + str(k) + ' trials per Length)' )
    plt.ylabel('Time (sec)')
            
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
            -1 in place of infinity. Technically bad practice, but 
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
    
    # recreate the path by going through the previous nodes
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

"""
End Challenge 3
"""

"""
Challenge 4
"""

x0,x1,x2,x3,x4=sp.symbols('x0:5')

F1=(~x0 | x3) & (x2 | x4) & (x3 | ~x4) & (~x2 | ~ x3) & (~x0 | x4) 

F2=(~x0 | ~x3) & (x2 | x4) & (x3 | ~x4) & (~x2 | x3) & (~x0 | x4) & (x2 | ~x3) & (~x2 | x0)

"""
@function two_sat: Evaluates whether a 2-SAT expression can be satisfied in polynomial time. A pretty inefficient implementation. 
@expr: a sympy boolean expression in 2-CNF format
@return: If unsatisfiable, will return False. Otherwise, will return a dictionary using the symbols as keys which map to Boolean values that will satisfy the expression. 
"""
def two_sat(expr):
    import numpy as np
    
    # length of network that will be used to find satisfiability 
    n = len(expr.atoms())
    var = list(expr.atoms())

    network = np.zeros((2*n, 2*n))
    
    # since symbols might come in arbitrary order, have the symbols map to a unique index. Negations will map to (index + n)
    symbolIndex = {}
    for i in range(n):
        symbolIndex[var[i]] = i
        symbolIndex[sp.Not(var[i])] = i + n      
    
    # create a dictionary that gets the symbol based on index
    matrixSymbol = {v: k for k, v in symbolIndex.items()}
    
    # create the network associated with the expression
    for i in range(len(expr.args)):
        
        # we know there will only be 2 literals per block
        lit1 = expr.args[i].args[0]
        lit2 = expr.args[i].args[1]
        
        # populate network using (x|y) = (~x => y) equivalence relation
        row = symbolIndex[sp.Not(lit1)]
        column = symbolIndex[lit2]
        network[row, column] = 1
        
        # do the same using (x|y) = (~y => x) equivalence relation
        row = symbolIndex[sp.Not(lit2)]
        column = symbolIndex[lit1]
        network[row, column] = 1
    
    # use depth first search for each symbol to make sure that we don't have x => ~x and ~x => x
    toVisit = []
    path = []
    
    discovered = {}
    for key in symbolIndex:
        discovered[key] = False
    
    for symbol in var:
        
        # reset what has been discovered
        path = []
        for key in symbolIndex:
            discovered[key] = False
            
        # add first symbol to stack of nodes to be visisted
        toVisit.append(symbol)

        # start the search
        while len(toVisit) != 0:
            
            # take the most recently added item and search from there
            visit = toVisit.pop()
            
            """
            if path leads to negation of first symbal, start a second DFS to see if there is a cycle
            This is probably not the best way to do this, but just trying to brute force it at this point
            """
            if visit == sp.Not(symbol):
                
                # reset what has been discovered
                for key in symbolIndex:
                    discovered[key] = False
                    
                    nToVisit = []
                    nToVisit.append(sp.Not(symbol))
                    
                    while len(nToVisit) != 0:
                        nVisit = nToVisit.pop()
                        
                        # if there is a cycle, then NOT satisfiable
                        if nVisit == symbol:
                            return False
                        
                        # otherwise, visit a node if it has not been explored yet
                        if not discovered[nVisit]:
                            discovered[nVisit] = True
                            
                            # add neighbors to list of nodes to be visisted
                            for i in range(len(network[symbolIndex[nVisit]])):
                                if network[symbolIndex[nVisit], i] == 1:
                                    nToVisit.append(matrixSymbol[i])
            
            # if next node was NOT the negation we're looking for, then continue DFS 
            if not discovered[visit]:
                discovered[visit] = True
                path.append(visit)

                #check neighbors
                for i in range(len(network[symbolIndex[visit]])):
                    if network[symbolIndex[visit], i] == 1:
                        toVisit.append(matrixSymbol[i])
                        
        # if we find a path that connects all of the n symbols, then we have found a solution
        if len(path) == n:
            
            # create a dictionary
            returnDict = {}
            
            for symbol in path:
                
                # if you negate the symbol and it is one of the atoms of the expression, then it should be false
                if sp.Not(symbol) in var:
                    returnDict[sp.Not(symbol)] = False
                    
                # otherwise, value should be true
                else:
                    returnDict[symbol] = True
                    
            return returnDict
            
"""
End Challenge 4
"""