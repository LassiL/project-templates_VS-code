#!/bin/zsh
# This is run by ./run.sh, but I need permissions:
# chmod u+x run.sh
gfortran fmodule.f90 main.f90
./a.out
exit 0