#include <iostream> 
#include "vector.hpp"

int main(int argc, char const *argv[])
{
    vector v{1.0, 2.0, 3.0};

    double l = v.length();

    std::cout << "Length = " << l << "\n"; 
    return 0;
}
