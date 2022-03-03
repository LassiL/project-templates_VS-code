import numpy as np
#A = np.array([[1, 2.5], [-3, 4]])
#b = np.array([1,2.5])
n = 5
A = np.random.rand(n,n)
b = np.random.rand(1,n)
import f2pylapack
print(f2pylapack.solve(A,b))
print(f2pylapack.solve.__doc__)
