# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 16:12:13 2017

@author: Ryan Kim
"""

def estNoneValues(arr):
    import numpy as np
    from sklearn.decomposition import NMF
    
    # create our array (convert into a numpy array)
    arr = np.array(arr)
    
    # List of tuples to record where there are no values
    noneIndices = []
    returnValues = {}
    
    # determine rows/columns with value 'None'
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i,j] == None:
                noneIndices.append((i,j)) 
                
    # perform NMF on subarrays
    model = NMF(n_components = 3, init = 'random', random_state = 0)    
    for value in noneIndices:
        
        # extract subarrays for calculations
        rowRemoved = np.delete(arr,value[0],0)
        columnRemoved = np.delete(arr, value[1], 1)
        
        # take the user x feature matrix
        W = model.fit_transform(columnRemoved)

        # and the feature x movie matrix
        model.fit_transform(rowRemoved)
        H = model.components_
        
        # multiply the two parts to create matrix estimation
        estArr = np.dot(W,H)
        
        # update values
        arr[value[0], value[1]] = estArr[value[0], value[1]]
        returnValues[value] =  estArr[value[0], value[1]]
        
    return returnValues

def kNearest(predict):   
    import numpy as np
    import pandas as pd    
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.cross_validation import train_test_split
    
    # set the names of the columns
    names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']
    
    # load the training set
    df = pd.read_csv('iris.data', header = None, names = names)
    
    # will just use the sepal_length and petal_width 
    learningData = np.array(df.ix[:, [0,2]])
    classifier = np.array(df['class'])
    
    X_train, X_test, y_train, y_test = train_test_split(learningData, classifier, test_size = 0.33, random_state = 42)

    # perform K Nearest Neighbors calculations
    model = KNeighborsClassifier(n_neighbors = 3)
    
    # fitting the model
    model.fit(X_train, y_train)
    
    # predict the response
    return model.predict(predict)

def clustering():
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    from sklearn import cluster
    
        # set the names of the columns
    names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']
    
    # load the training set
    df = pd.read_csv('iris.data', header = None, names = names)
    
    # will just use the sepal_length and petal_width 
    learningData = np.array(df.ix[:, [0,2]])

    kMeanClustering = cluster.KMeans(n_clusters = 3)
    kMeanClustering.fit(learningData)
    
    labels = kMeanClustering.labels_
    centroids = kMeanClustering.cluster_centers_
    
    for i in range(3):
        
        # get all of the indices where label is i and plot
        points = learningData[np.where(labels == i)]
        plt.plot(points[:,0], points[:,1], 'o')
        
        # plot the centroids
        plt.plot(centroids[i, 0], centroids[i, 1], 'kx', markersize = 11)
        
        
    return 
    
    
    
    