import numpy as np, matplotlib.pyplot as plt

a=np.random.randint(1000,size=100)
b=np.random.randint(1000,size=100)
print 'Generated random number arrays :'
print 'X =',sorted(a)
print 'Y =',sorted(b)

plt.subplot(221)
plt.xlabel('X values')
plt.ylabel('Y values')
plt.title('Line Graph for random values')
plt.plot(sorted(a),sorted(b))

plt.subplot(222)
plt.xlabel('X values')
plt.ylabel('Y values')
plt.title('Histogrm for random values')
plt.hist(a)

plt.subplot(223)
plt.xlabel('X values')
plt.ylabel('Y values')
plt.title('Scatter plot')
plt.scatter(sorted(a),sorted(b))
plt.show()