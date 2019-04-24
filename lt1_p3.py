import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde

def customDistr(table):
	""" returns a random value that is distributed according to a customized
		distribution generated from a lookup table
	"""
	outcome = [x[0] for x in table]
	possi = [x[1] for x in table]

	result = np.random.choice(outcome, p = possi)
	return result

inp = [[5, 0.03],
	   [10, 0.13],
	   [20, 0.22],
	   [40, 0.12],
	   [70, 0.17],
	   [100, 0.08],
	   [110, 0.2],
	   [115, 0.05]]


def getresults():
    result = []
    for i in (range(1000)):
        num = customDistr(inp)
        result += [num]
    result = np.sort(result)
    print(result)
    density = gaussian_kde(result)
    xs = np.linspace(0, 115, 200)
    density.covariance_factor = lambda : 0.01
    density._compute_covariance()
    plt.plot(xs, density(xs))
    plt.show()
    
getresults()

"The graph does reflect the properties of the distribution provided in Table 1."