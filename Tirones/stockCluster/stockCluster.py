import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as dat
import datetime

from matplotlib.collections import LineCollection

from sklearn import cluster, covariance, manifold

class stockCluster:

    def __init__(self, stockList):
        self.stockList = stockList

    def setStockList(self, stockList):
        self.stockList = stockList

    def makeCluster(self, keyString='variation'):
        
        names = [company.getName() for company in self.stockList]

        names = np.array(names)

        print names
        openPrice = np.array([company.getOpen() for company in self.stockList]).astype(np.float)
        closePrice = np.array([company.getClose() for company in self.stockList]).astype(np.float)
        
        if keyString == 'Open':
            X = openPrice.copy().T

        elif keyString == 'Close':
            X = closePrice.copy().T
        
        elif keyString == 'variation':
            variation = openPrice - closePrice
            X = variation.copy().T

                ###############################################################################
        # Learn a graphical structure from the correlations
        edge_model = covariance.GraphLassoCV()

        # standardize the time series: using correlations rather than covariance
        # is more efficient for structure recovery
        X /= X.std(axis=0)
        edge_model.fit(X)

        ###############################################################################
        # Cluster using affinity propagation

        _, labels = cluster.affinity_propagation(edge_model.covariance_)
        n_labels = labels.max()

        print labels

        for i in range(n_labels + 1):
            print('Cluster %i: %s' % ((i + 1), ', '.join(names[labels == i])))



