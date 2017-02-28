# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 21:00:06 2017

@author: ryan
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
    return quickSort(numList, 0, len(numList) -1)
    
"""
@function quickSort: helper function o quick_sort. Performs the sorting logic.
@param numList: list of numbers
@param lo: lowest index in range
@param hi: highest index in range
@return sorted List of numbers
"""
def quickSort(numList, lo, hi):
    if hi >= lo:
    
        pivotIndex = partition(numList, lo, hi)
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
    
    if lo >= hi:
        return lo
    
    # select first item to be pivot. Since List was presumably shuffled earlier, reduced chance of terrible pivot
    pivot = numList[lo]
    
    index1 = lo + 1
    index2 = hi
    
    while True:
        # start from left side of the list
        while numList[index1] <= pivot:
            # keep going until we find an element larger than the pivot
            index1 += 1
            
            # stop if left index reaches the end
            if index1 == hi:
                break

        # do the same starting from the end of the list. find a value that is less than the pivot
        while numList[index2] >= pivot:
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