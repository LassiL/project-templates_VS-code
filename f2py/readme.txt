compile fortran
    $ gfortran -O2 -lblas -llapack solve1.f90 -o myapp

compile to python module with f2py (activate conda env with numpy first)
    $ f2py -c -m f2pylapack f2pylapack.f90 -lblas -llapack


#Useful references for fortran:
	- https://users.soe.ucsc.edu/~ylee/18spring/ams129/chapters/chapt02/ch02_fortran_blas_lapack.html
	- https://nbviewer.org/github/mgaitan/fortran_magic/blob/master/documentation.ipynb
	- https://pnavaro.github.io/python-fortran/01.f2py.html
	- https://numpy.org/devdocs/f2py/f2py-examples.html
	- https://www.numfys.net/howto/F2PY/ 
	- https://people.sc.fsu.edu/~jburkardt/f77_src/lapack_examples/lapack_examples.html
	- http://numerical.recipes/oldverswitcher.html
	- https://pages.mtu.edu/~shene/COURSES/cs201/NOTES/F90-Subprograms.pdf