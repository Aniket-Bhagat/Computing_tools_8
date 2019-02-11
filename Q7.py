import scipy as sp,scipy.integrate,numpy as np, matplotlib.pyplot as plt

Pop = np.loadtxt('populations.txt', delimiter='\t', unpack=True).astype('int')
Population  = Pop[1:].T

print "---------------------------------------a---------------------------------------\n"
means = (Pop[1:]).mean(axis=1)
stdv = (Pop[1:]).std(axis=1)
print '\t\t\t\tHare','\t\tLynx','\t\tCarrot'
print '\tMean :\t\t',means
print 'Standard Daviations :\t',stdv

print "\n---------------------------------------b---------------------------------------\n"
y = Pop[0][np.argmax(Pop[1:],axis=1)]
print 'Max Population Years for each species :\n Hare Lynx Carrot'
print y

print "\n---------------------------------------c---------------------------------------\n"
names = ['Hare', 'Lynx', 'Carrot']
w = np.take(names,np.argsort(Pop[1:].T,axis=1))
w = w.tolist()
z = zip(Pop[0],w)
print '''Given a Dictionary with key as Years and
values are list having species arranged in ascending order :'''
print dict(z)

print "\n---------------------------------------d---------------------------------------\n"
print 'Following is the list of years where any of the populations is above 50000 :'
print Pop[0][np.any(Pop[1:]>50000,axis=0)]

print "\n---------------------------------------e---------------------------------------\n"
a = (Pop[0][np.argsort(Pop[1:],axis=1)[:,:2]])
a = a.tolist()
b = zip(names,a)
print 'Top 2 years for each species when they had the lowest populations :'
print b

print "\n---------------------------------------f---------------------------------------\n"
plt.plot(Pop[0], Pop[2], 'hr-', Pop[0], np.gradient(Pop[1]), 'h-')
plt.legend(['Lynx', 'Gradient of Hare'], loc='upper center')
print 'Plotting a graph...'
plt.show()
print 'Closed'

print "\n---------------------------------------g---------------------------------------\n"
print 'Correlation between Lynx and Gradient of Hare :'
print np.corrcoef(Pop[2], np.gradient(Pop[1]))
print "\n-------------------------------------------------------------------------------\n"