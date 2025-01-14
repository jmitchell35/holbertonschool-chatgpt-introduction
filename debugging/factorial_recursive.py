#!/usr/bin/python3
import sys

def factorial(n):
    '''
    Calculates the factorial of a given number using recursive approach.
    
    Parameters:
        n (int): A non-negative integer for which factorial needs to be calculated.
    
    Returns:
        int: The factorial of n (n!), which is the product of all positive integers 
             from 1 to n. Returns 1 for n = 0.
    '''
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

f = factorial(int(sys.argv[1]))
print(f)
