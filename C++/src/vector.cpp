#include <math.h>
#include "vector.hpp"

double vector::length()
{
    return sqrt(x*x + y*y + z*z);
}