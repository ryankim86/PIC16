# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 12:59:59 2017

@author: ryan
"""

# takes an image path as input and converts it to a grayscale image
def grayscale(imagePath): 
    import numpy as np
    import matplotlib
    import math
    from PIL import Image
   
    im = Image.open(imagePath)
    nim = np.array(im)
    
    grayscale = 0.2125 * nim[:,:,0] + 0.7514 * nim[:,:,1] + 0.0721 * nim[:,:,2]
    matplotlib.pyplot.imshow(grayscale, cmap = 'gray')
   # print(grayscale[51 - math.floor(3/2): 51 + math.ceil(3/2), 50 - math.floor(3/2) : 50 + math.ceil(3/2)])
    return grayscale
    
def blurring(image, k = 3, option = 'u', sigma = 1):
    import numpy as np
    import math
    import matplotlib
    
    # check for invalid inputs
    if k % 2 == 0:
        print('k must be odd')
        return
    if option != 'g' and option != 'u':
        print('noise removal option must be \'g\' or \'u\'')
        return
    if option  == 'g' and sigma <= 0:
        print('sigma must be greater than 0 for Gaussian Filter')
        return 
    
    # create filter matrix of dim kxk
    imFilter = np.zeros((k, k), dtype = np.float64)
    # create a matrix to temporarily store values
    tempValue = np.zeros((k, k), dtype = np.float64)
    # create a return array
    filteredImage = image
    
    # uniform
    if option == 'u':
        imFilter[:,:] = 1 / k**2
    
    # gaussian
    
    
    # apply filter
    for i in range(math.floor(k/2), len(filteredImage) - math.floor(k/2)):
        for j in range(math.floor(k/2), len(filteredImage[i]) - math.floor(k/2)):
            tempValue = np.array(image[i - math.floor(k/2): i + math.ceil(k/2), j - math.floor(k/2) : j + math.ceil(k/2)])
            tempValue *= imFilter
            filteredImage[i][j] = np.sum(tempValue)
    
    matplotlib.pyplot.imshow(filteredImage, cmap = 'gray')