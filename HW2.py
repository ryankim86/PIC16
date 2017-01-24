# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 12:45:05 2017

@author: Ryan Kim
"""

def mytype(theInput):
    import re

    # check if list by seeing if the first and last characters are [ and ], respectively
    if re.search(r'^\[{1}.*\]{1}$', str(theInput)) is not None:
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
    for file in fileList:
        # note to self, check for illegal special characters using (?!...)
        match = re.match(r'(^(?!\\)(?!\n)(?!\/).+)[\.]{1}(pdf|PDF)$', file)
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
        
def findemail(url):
    import re
    import urllib.request
    #txt = 'cmarshak [at] math [dot] ucla [dot] edu [dot] mex [dot] hi'
    txt = str(urllib.request.urlopen(url).read())
    # grab fairly simple emails (or incomplete complex ones)
    shortMatch = re.findall(r'([A-Za-z0-9\.\-+_]+[ ]?)(@|at | at | _at_ | \[at\] | \[\<i\>at\<\/i\>\] )([A-Za-z0-9\.\-+_ ]+)(\.| dot | dot| _dot_ | \[dot\] | \[\<i\>dot<\/i>\] )([A-Za-z]+)', txt)
    
    # complex email (i.e. more than 1 'dot' in the domain name)
    longMatch = re.findall(r'([A-Za-z0-9\.\-+_]+[ ]?)(@|at | at | _at_ | \[at\] | \[\<i\>at\<\/i\>\] )([A-Za-z0-9\.\-+_ ]+)(?:(\.| dot | dot| _dot_ | \[dot\] | \[\<i\>dot<\/i>\] )([A-Za-z]+))+(\.| dot | dot| _dot_ | \[dot\] | \[\<i\>dot\<\/i\>\] )([A-Za-z]+)', txt)

    if len(longMatch) is 0 and len(shortMatch) is 0:
        print('No emails found on this page')
        return
    else:
        if len(longMatch) is 0:
            matches = shortMatch
        elif len(shortMatch) is 0:
            matches = longMatch
        else:
            matches = longMatch if len(longMatch[0]) > len(shortMatch[0])  else shortMatch
        
    returnEmail = ''
    for match in matches[0]:
        print (match)
        piece = match.replace(' ', '')
        if piece == 'at' or piece == '_at_' or piece == '[at]' or piece == '[<i>at</i>]':
            piece = '@'
        elif piece  == 'dot' or piece  == '_dot_' or piece == '[dot]' or piece == '[<i>dot</i>]':
            piece = '.'
                

        returnEmail+=piece
    print(returnEmail)
        
# defining a global variable
happiness_dictionary = {}

def happiness(englishText):
    import re
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
            
    return (rawHappinessScore / numMatchedWordsInDict)
        