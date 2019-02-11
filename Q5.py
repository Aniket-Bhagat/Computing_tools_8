import scipy as sp,scipy.linalg

a=sp.array([[41,15,96,31],[10,21,33,-11],[70,-31,11,10],[25,-22,28,-49]])
b=sp.array([46,45,50,57])

val = sp.linalg.solve(a,b)

print '''Given equations are :
41*x +  15*y + 96*z +  31*t = 46
10*x +  21*y + 33*z -  11*t = 45
70*x -  31*y + 11*z +  10*t = 50
25*x -  22*y + 28*z -  49*t = 57'''

print '\nValues of variables satisfying above equations :'
print 'x = %9f\ny = %9f\nz = %9f\nt = %9f'%tuple(val)