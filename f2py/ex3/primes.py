"""This is run as:
    $ f2py -c primes.f95 -m primes #Which creates primes that I can import"""
#Shell commands written in python as:
import os
#os.system runs this command in the shell
#which creates primes that I can import
os.system("f2py -c primes.f95 -m primes") 
import primes
print(primes.__doc__)

print(primes.logical_to_integer.__doc__)

sieve_array = primes.sieve(100)
prime_numbers = primes.logical_to_integer(sieve_array, sum(sieve_array))
print(prime_numbers)