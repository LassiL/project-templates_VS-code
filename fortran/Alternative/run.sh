#!/bin/zsh
# This is run by ./run.sh, but I need permissions:
# chmod u+x scriptname.sh
gfortran helloworld.f90 -o myprogram
./myprogram
exit 0