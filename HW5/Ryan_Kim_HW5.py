# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 19:01:52 2017

@author: Ryan Kim
"""

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
        