import numpy, matplotlib.pyplot as plt
from scipy.stats.kde import gaussian_kde

data = numpy.loadtxt('data.dat', dtype='float', delimiter='\t', unpack=True)

def probdist(colno):
	global data
	plt.subplot(2,2,colno+1)
	kde = gaussian_kde( data[colno] )
	dist_space = numpy.linspace( min(data[colno]), max(data[colno]), 100 )
	plt.plot( dist_space, kde(dist_space) )
	plt.title('Distribution for column %d'%(colno+1))
	
plt.suptitle('Probability Distribution of Data in file')
probdist(0)
probdist(1)
probdist(2)
probdist(3)
mng = plt.get_current_fig_manager()
mng.resize(*mng.window.maxsize())
plt.show()

# import numpy as np
# import scipy.stats as stats
# import matplotlib.pyplot as plt

# data = np.loadtxt('data.dat', dtype='float', delimiter='\t', unpack=True)
# data = sorted(data[0])
# fit = stats.norm.pdf(data, np.mean(data), np.std(data))
# plt.plot(data,fit,'-')
# # plt.hist(data,normed=True)
# plt.show()