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
    print(equation[0])
    print(equation[1])

    # go through the input and find the elements involved
    leftMatches = re.findall('([A-Za-z\d]+)', equation[0])
    rightMatches = re.findall('([A-Za-z\d]+)', equation[1])
    
    Matches = re.findall('([A-Z]{1}[a-z]?)(\d)?', equation[0])
    for match in Matches:
        print(match)
    
    # create a list of symbols
    n = len(leftMatches)+len(rightMatches)
    symbolString = 'x0:' + str(n)
    xList = sp.symbols(symbolString)
    xList = ['x%d'%i for i in range(n)]
    
    # create a dictionary that will store the dictionaries to store components of the eq
    left = {}
    right = {}
    
    # parse through chemical blocks
    for i in range(len(leftMatches)):
        elementMatches = re.findall('([A-Z]{1}[a-z]?)(\d)?', leftMatches[i])
        left['x%d'%i] = {}
        for match in elementMatches:
            if match[0] in left['x%d'%i]:
                prevValue = left['x%d'%i][match[0]]
                if len(match[1]) == 0:
                    left['x%d'%i][match[0]] = prevValue + 1
                else:
                    left['x%d'%i][match[0]] = prevValue + int(match[1])
            else:
                if len(match[1]) == 0:
                    left['x%d'%i][match[0]] = 1
                else:
                    left['x%d'%i][match[0]] = int(match[1])
    for i in range(len(leftMatches), n-1):
        elementMatches = re.findall('([A-Z]{1}[a-z]?)(\d)?', rightMatches[i])
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
    
    return

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
        # cycle through three colors
        color = ''
        if j % 3 == 0:
            color = 'red'
        elif j % 3 == 1:
            color = 'purple'
        elif j % 3 == 2:
            color = 'cyan'
            
        # add the next term
        function += (sp.diff(sp.cos(x), x, j).subs(x,0)*(x**j)*(1/math.factorial(j)))
        # plot
        plot1.extend(sp.plotting.plot(function, (x,-5,5), line_color = color, show = False))
        
    # show plot
    plot1.show()
    return
        