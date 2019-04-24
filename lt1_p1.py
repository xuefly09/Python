# -*- coding: utf-8 -*-
import random
import math
import matplotlib.pyplot as plt
import numpy as np

class RandVar:
    def exp(lamda):
        rannum = random.uniform(0, 1)
        res = (-1.0/lamda)*math.log(rannum)
        return res

    def gen_plot():
        lst = []
        for i in range(1000):
            lst.append(RandVar.exp(4))
            i+=1
        data_size = len(lst)

        # Set bins edges
        data_set = sorted(set(lst))
        bins=np.append(data_set, data_set[-1]+1)

        # Use the histogram function to bin the data
        counts, bin_edges = np.histogram(lst, bins = bins, density = False)

        counts = counts.astype(float)/data_size
        
        # Find the cdf
        cdf = np.cumsum(counts)

        # Plot the cdf
        plt.plot(bin_edges[0:-1], cdf,linestyle='--', marker="o", color='b')
        plt.ylim((0,1))
        plt.ylabel("CDF")
        plt.grid(True)

        plt.show()


RandVar.gen_plot()