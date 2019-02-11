import scipy as sp,scipy.integrate,numpy as np, matplotlib.pyplot as plt
from scipy.stats.kde import gaussian_kde

print """-----------------------------------------------------------------
|		Analysis of Rainfall Time series data		|
-----------------------------------------------------------------\n"""

states = np.loadtxt('rainfall_stats.csv',dtype='str', delimiter='\t', usecols=[0])
for i in range(len(states)):
	print i+1,states[i]
print "\nChoose the number given before the state names"
stateno1,stateno2 = input("For State A : ")-1,input("For State B : ")-1

monthno = input("\nEnter a month number : ")-1
months=['January','February','March','April','May','June','July','August','September','October','November','December']

def monthwise(n,m):
	col=map(lambda x:6*(n)+x,[1,2,3,4,5,6])
	monthdata=np.loadtxt('rainfall_stats.csv',dtype='float', delimiter='\t', usecols=col)
	return (monthdata[m,:],states[m])

data1 = monthwise(monthno,stateno1)
data2 = monthwise(monthno,stateno2)

def probdist(D):
	x,y=D
	kde = gaussian_kde(x)
	dist_space = np.linspace( min(x), max(x), 100 )
	plt.plot( dist_space, kde(dist_space) )
	plt.title('%s'%y)

plt.suptitle('Rainfall Distribution for %s'%months[monthno])
plt.subplot(1,2,1)
probdist(data1)

plt.subplot(1,2,2)
probdist(data2)

mng = plt.get_current_fig_manager()
mng.resize(*mng.window.maxsize())
plt.show()


print """\n---------------To check the correlation between the data---------------"""
PCC = scipy.stats.pearsonr(data1[0],data2[0])
print "\nPearson correlation coefficient :",PCC[0]
print "the 2-tailed p-value :",PCC[1]

if PCC[0]<0:
	print "\nNegative Correlation"
elif PCC[0]>0:
	print "\nPositive Correlation"
else :
	print "\nNo Correlation"
print """\n-----------------------------------------------------------------------"""