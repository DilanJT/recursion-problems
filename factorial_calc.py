
# problem : factorial calc
#  Given a non negative integer n, calaculates the factorial of n, dented as n!

"""
The factorial of a non negative integer 'n', denoted by 'n!', is the product of all positive integers less than or equal to 'n'
"""

def factorial_loop(n):
    result = 1
    for i in range(1, n + 1):
        result *= i

    return result

factorial_loop(5)

# Recursive solution

def recursive_factorial(n):
    if (n == 0):
        return 1
        
    return n * recursive_factorial(n-1)
    
print(recursive_factorial(5))