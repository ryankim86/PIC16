# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 19:01:52 2017

@author: Ryan Kim
"""

"""
Challenge 1
"""
def balance(eq):
    import re
    import sympy as sp
    
    # split the equation into its two halves
    equation = eq.split('=', 1)

    # go through the input and find the elements involved
    leftMatches = re.findall('([A-Za-z\d]+)', equation[0])
    rightMatches = re.findall('([A-Za-z\d]+)', equation[1])
         
    #Matches = re.findall('([A-Z]{1}[a-z]?)(\d)?', equation[0])
    
    # create a list of symbols
    n = len(leftMatches) + len(rightMatches)
    symbolString = 'x0:' + str(n)
    xList = ['x%d'%i for i in range(n)]
    xList = sp.symbols(symbolString)
    
    # create a dictionary that will store the dictionaries to store components of the eq
    left = {}
    right = {}
    uniqueElements = {}
    
    # parse through chemical blocks for both sides of the equation
    for i in range(len(leftMatches)):
        
        # find the individual elements within each chemical block
        elementMatches = re.findall('([A-Z]{1}[a-z]?)(\d)?', leftMatches[i])
        
        # create a dictionary that will hold the number of each element within that block. Keys are the element symbol
        left['x%d'%i] = {}
        
        # calculate how many of each element is within block
        for match in elementMatches:
            
            # if key already in the dictionary, then add to the previous value
            if match[0] in left['x%d'%i]:
                prevValue = left['x%d'%i][match[0]]
                if len(match[1]) == 0:
                    left['x%d'%i][match[0]] = prevValue + 1
                else:
                    left['x%d'%i][match[0]] = prevValue + int(match[1])
                    
            # otherwise, record a new key
            else:
                if len(match[1]) == 0:
                    left['x%d'%i][match[0]] = 1
                else:
                    left['x%d'%i][match[0]] = int(match[1])
                    
            # keep track of elements in equation
            uniqueElements[match[0]] = True
                    
    # repeat for right side of the equation
    for i in range(len(leftMatches), n):
        elementMatches = re.findall('([A-Z]{1}[a-z]?)(\d)?', rightMatches[i-len(leftMatches)])
        right['x%d'%i] = {}
        for match in elementMatches:
            if match[0] in right['x%d'%i]:
                prevValue = right['x%d'%i][match[0]]
                if len(match[1]) == 0:
                    right['x%d'%i][match[0]] = prevValue + 1
                else:
                    right['x%d'%i][match[0]] = prevValue + int(match[1])
            else:
                if len(match[1]) == 0:
                    right['x%d'%i][match[0]] = 1
                else:
                    right['x%d'%i][match[0]] = int(match[1])
            uniqueElements[match[0]] = True
      
    # add coefficients for linear system to augmented matrix
    counter = 0      
    augMatrix = sp.zeros(len(uniqueElements), n+1)
    for element in uniqueElements:
        for i in range(len(left)):
            if element in left['x%d'%i]:
                augMatrix[counter, i] = int(left['x%d'%i][element])
        for i in range(len(leftMatches), n):
            if element in right['x%d'%i]:
                augMatrix[counter, i] = int(-1*right['x%d'%i][element])
        counter += 1
        
    linSolu = sp.solve_linear_system(augMatrix, *xList)

    # create a sympy matrix to store the results of the linear eq. solver
    varMatrix = sp.zeros(n,1)
    count = 0
    for key in linSolu:
        varMatrix[count] = linSolu[key]
        count += 1
    
    # substitute 2 for any free variable
    for i in range(n):
        if xList[i] not in linSolu:
            varMatrix = varMatrix.subs(xList[i], 1)
            varMatrix[i] = 1
    
    # create output string
    returnString = ''
    for i in range(len(leftMatches)):
        returnString += str(varMatrix[i]) + leftMatches[i]
        if i == len(leftMatches)-1:
            returnString += ' = '
        else:
            returnString += ' + '
    for i in range(len(rightMatches)):
        returnString += str(varMatrix[len(leftMatches)+i]) + rightMatches[i]
        if i != len(rightMatches)-1:
            returnString += ' + '
    
    if len(linSolu) == 0:
        return 'No Solution'
    else:
        return returnString

"""
Challenge 3
"""
def taylor_figure(k):
    import sympy as sp
    import math
    
    x = sp.Symbol('x')
    
    # plot cos(x)  
    plot1 = sp.plotting.plot(sp.cos(x),(x,-5,5), line_color = 'black', show = False)
    
    function = 0
    # Maclaurin Exp: f(x) = f(a) + f'(a)(x-a) + f''(a)(x-a)^2/2! + f^3(a)(x-a)^3/3! + ...
    for j in range(k+1):
        # cycle through five colors
        color = ''
        if j % 5 == 0:
            color = 'red'
        elif j % 5 == 1:
            color = 'purple'
        elif j % 5 == 2:
            color = 'cyan'
        elif j % 5 == 3:
            color = 'blue'
        elif j % 5 == 4:
            color = 'yellow'
            
        # add the next term
        function += (sp.diff(sp.cos(x), x, j).subs(x,0)*(x**j)*(1/math.factorial(j)))
        # plot
        plot1.extend(sp.plotting.plot(function, (x,-5,5), line_color = color, show = False))
        
    # show plot
    plot1.show()
    return