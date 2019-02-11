import scipy as sp,scipy.integrate,numpy as np

result1 = sp.integrate.quad((lambda x : x),0,10)
result2 = sp.integrate.quad((lambda x : x**2),-5,5)
result3 = sp.integrate.quad((lambda x : np.sin(x)),0,(np.pi/2))

print '\nintegration of x dx from x= 0 to 10\n%.3f'%result1[0]
print '\nintegration of x^2 dx from x= -5 to 5\n%.3f'%result2[0]
print '\nintegration of sin(x) dx from x= 0 to pi/2\n%.3f'%result3[0]