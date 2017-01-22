# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 12:45:05 2017

@author: Ryan Kim
"""

def mytype(theInput):
    import re

    # check if list by seeing if the first and last characters are [ and ], respectively
    if re.search(r'^\[{1}.+\]{1}$', str(theInput)) is not None:
        return '<class \'list\'>'        
    # check if integer by seeing if it is a string of digits with no .
    elif re.search(r'^\d+(?!\.)$', str(theInput)) is not None:
        return '<class \'int\'>'  
    # check if float by seeing it is a string of diigts with 1 .
    elif re.search(r'^\d+\.{1}\d+$',str(theInput)) is not None:
        return  '<class \'float\'>'   
    # otherwise, the input should be a string
    else: 
        return '<class \'string\'>'

def findpdfs(fileList):
    import re
    outputList = []
    for i in range(len(fileList)):
        # note to self, check for illegal special characters using (?!...)
        match = re.match(r'(^(?!\\)(?!\n).+)[\.]{1}(pdf|PDF)$',fileList[i])
        if match is not None:
            outputList.append(str(match.group(1)))
    return outputList
    
def names(inputName):
    import re    
    # find capitlizized words in the strings that are separated by a space
    match = re.findall(r'([A-Z][a-z]*)[\s-]?', inputName)
    if len(match) is 3:
        return match[2] + ", " + match[0] + " " + match[1][0]
    if len(match) is 2:
        return match[1] + ", " + match[0]
    else:
        print('Input Not Valid')
        return
            
            
        


