#include <stdio.h>
#include <stdlib.h>
#include "vector.h"

int main(int argc, char const *argv[])
{
    struct vector v = {1.0, 2.0, 3.0};
    double l;

    l = length(v);

    printf("length = %8.4f\n", l);
    return 0;
}
