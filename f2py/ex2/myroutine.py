import numpy as np
import myroutine #imports myroutine*.so which has been compiled by
                 #python -m numpy.f2py -c myroutine.f90 -m myroutine
                 #see: https://numpy.org/devdocs/f2py/f2py-examples.html
                 #and: https://pnavaro.github.io/python-fortran/01.f2py.html
print(myroutine.__doc__)
x = myroutine.s(2,3, np.array([5,6,7]))
print(x)
