# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 12:59:59 2017

@author: Ryan Kim
"""


"""
Part of Challenge 1 Test case:
@param im: numpy array representing the image
@p: percentage of Salt and Pepper noise. Acceptable input is a floating point number between 0 and 1
"""
def saltAndPepper(im, p):
    import random
    import numpy as np
    import matplotlib
    
    # pseudorandom number 
    randNum = 0  
    
    for i in range(len(im)):
        for j in range(len(im[0])):
            # generate a pseudorandom number
            randNum = random.random()
            
            # if number falls between 0 and p, make pixel white
            if randNum < p:
                im[i,j] = 1
            # if number is between p and 2*p, make pixel black
            elif randNum >= p and randNum < 2*p:
                im[i,j] = 0
            
            # otherwise, leave as-is
    matplotlib.pyplot.imshow(im, cmap = 'gray')
    return np.array(im)

"""
Challenge 1: Will blur a grayscale image (remove noise) using either Mean or Gaussian Filtering
@param image: a numpy array representing the image
@param k: dimesion of the filter. Must be odd. Default value is 3
@param option: Uniform vs Gaussian. Input 'g' for Gaussian and 'u' for uniform. Default is Gaussian
@param sigma: sigma parameter for the Gaussian distribution. Default value is 1
@return filteredImage: a numpy array representing the image with the noise removed
"""
def blurring(image, k = 3, option = 'g', sigma = 1):
    import matplotlib
    import numpy as np
    import math
    
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
    if option == 'g':
        for i in range(k):
            for j in range(k):
                imFilter[i, j] = (1/(2*math.pi*sigma))*math.exp(-1*((i-math.floor(k/2))**2 + (j-math.floor(k/2))**2)/(2*(sigma**2)))
        imFilter /= np.sum(imFilter)
    
    # apply filter
    for i in range(math.floor(k/2), len(filteredImage) - math.floor(k/2)):
        for j in range(math.floor(k/2), len(filteredImage[i]) - math.floor(k/2)):
            tempValue = np.array(image[i - math.floor(k/2): i + math.ceil(k/2), j - math.floor(k/2) : j + math.ceil(k/2)])
            tempValue = np.multiply(tempValue, imFilter)
            filteredImage[i, j] = np.sum(tempValue)
    
    matplotlib.pyplot.imshow(filteredImage, cmap = 'gray')
    return filteredImage
    
"""
Challenge 2: Will detect vertical, horizontal, or both 
@param image: a numpy array representing the image
@param option: selects edge type. 'v' for vertical. 'h' for horizontal. 'b' for both
@return edgeImage: returns a numpy array representing the image
"""
def detect_edge(image, option = 'b'):
    import matplotlib
    import numpy as np
    import math
    
    # create Sobel matrices for vertical 
    sVertical= np.array([[-1,0,1], [-2,0,2], [-1,0,1]], dtype = np.float)
    sHorizontal = np.array([[1,2,1], [0,0,0], [-1,-2,-1]], dtype = np.float)
    
    # array to temporarily store image array values
    tempValue = np.zeros((3,3))
    
    # image for return
    edgeImage = np.zeros((image.shape[0], image.shape[1]), dtype = np.float)
    
    # apply sobel filter    
    for i in range(math.floor(3/2), len(image) - math.floor(3/2)):
        for j in range(math.floor(3/2), len(image[i]) - math.floor(3/2)):
            
            # grab a 3 by 3 block
            tempValue = np.array(image[i - math.floor(3/2): i + math.ceil(3/2), j - math.floor(3/2) : j + math.ceil(3/2)])
            
            # both
            if option == 'b':
                vert = np.multiply(tempValue, sVertical)
                hori = np.multiply(tempValue, sHorizontal)
                edgeValue = np.sqrt(np.sum(vert)**2 + np.sum(hori)**2)
            # vertical
            elif option == 'v':
                tempValue = np.multiply(tempValue, sVertical)
                edgeValue = np.sum(tempValue)
            # horizontal
            elif option == 'h':
                tempValue = np.multiply(tempValue, sHorizontal)
                edgeValue = np.sum(tempValue)
            
            # store value in the return matrix
            edgeImage[i,j] = edgeValue
    
    matplotlib.pyplot.imshow(edgeImage, cmap = 'gray')    
    return np.array(edgeImage)

"""
Challenge 3: Will split a grayscale image into foreground and highground using the Otsu Threshold method
@param image: a numpy array representing the image
@return returnMask: will return a mask matrix with True/False values representing pixels. True will be foreground pixels and false will be background pixels.
"""
def otsu_threshold(image):
    from PIL import Image
    import numpy as np
    import matplotlib
    
    im = Image.fromarray(image)
    nim = np.array(image)
    hist = im.histogram()
    
    # create matrix that will store True/False values whether it is in the foreground or not
    returnMask = np.zeros((nim.shape[0], nim.shape[1]), dtype = np.bool)
    
    # tuple to store the highest variance and its correpsonding threshold
    maxVar = (0,0)
    
    # check every threshold value for the Otsu Method
    for t in range(1,255):
        
        # calculate Total Count
        omegaZero = np.sum(hist[0:t-1])
        omegaOne = np.sum(hist[t:254])
        
        # if there are no counts in either group, go to next threshold value
        if omegaZero == 0 or omegaOne == 0:
            continue
        
        muZero = 0
        muOne = 0
        
        # calculate expectation of each group
        for i in range(255):
            if i <= t-1:
                muZero += (1/omegaZero)*i*hist[i]
            else:
                muOne += (1/omegaOne)*i*hist[i]
        
        # calculate the variance. Replace if variance is higher
        currVar = omegaZero*omegaOne*(muZero-muOne)**2
        maxVar = (t, currVar) if maxVar[1] < currVar else maxVar
        
    # using the threshold, create the mask
    for i in range(len(nim)):
        for j in range(len(nim[i])):
            returnMask[i,j] = True if nim[i,j] <= maxVar[0] else False
            
    matplotlib.pyplot.imshow(returnMask, cmap = 'gray')   
    return np.array(returnMask, dtype = np.bool)

"""
Challenge 4: Will locate the background of an image and blur it
@param image: a numpy array representing the image
"""
def blur_background(image):
    import numpy as np
    import matplotlib
    
    # save the value of the original image
    originalImage = np.array(image)
    
    # create a blurred image
    blurredImage = blurring(image, 17, 'g', 2)
    
    # generate mask that stores things that are in the foreground
    mask = otsu_threshold(image)

    # replace blurred pixels with original on the masku
    for i in range(len(blurredImage)):
        for j in range(len(blurredImage[i])):
            if mask[i,j] == True:
                blurredImage[i,j] = originalImage[i,j]
                
    matplotlib.pyplot.imshow(blurredImage, cmap = 'gray')   
    
    return blurredImage
    



"""
Takes an image path and returns a numpy array representing the image in grayscale
"""
def grayscale(imagePath): 
    import numpy as np
    import matplotlib
    from PIL import Image
   
    im = Image.open(imagePath)
    nim = np.array(im)
    
    grayscale = 0.2125 * nim[:,:,0] + 0.7514 * nim[:,:,1] + 0.0721 * nim[:,:,2]
    matplotlib.pyplot.imshow(grayscale, cmap = 'gray')

    return np.array(grayscale)

"""
creates a simple image that has at least 3 colors as well as horizontal/vertical/diagonal edges
"""
def createSimpleImage():
    import numpy as np   
    import matplotlib
    
    im = np.zeros((200,200))
    im[25:-25, 25:-25] = 1
    
    for i in range(25, len(im)):
        im[i,i:50] = 0.25
        
    for i in range(25, len(im) - 25):
        for j in range(25, i):
            im[i,j] = .60
            
    matplotlib.pyplot.imshow(im, cmap = 'gray')
    return np.array(im)