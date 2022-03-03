!! https://nbviewer.org/github/mgaitan/fortran_magic/blob/master/documentation.ipynb
subroutine solve(A, b, x, n)
    ! solve the matrix equation A*x=b using LAPACK
    implicit none

    real*8, dimension(n,n), intent(in) :: A
    real*8, dimension(n), intent(in) :: b
    real*8, dimension(n), intent(out) :: x

    integer :: i, j, pivot(n), ok

    integer, intent(in) :: n
    x = b

    ! find the solution using the LAPACK routine SGESV
    call DGESV(n, 1, A, n, pivot, x, n, ok)
    
end subroutine
