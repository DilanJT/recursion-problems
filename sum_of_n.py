"""
Question : a program to calculate the sum of the first 'n' natural nubers

"""

def sum_of_n(n):
    total = 0
    for i in range(1, n+1):
        total = total + i
    return total
    
print(sum_of_n(10))

def sum_of_n_recursive(n):
    if n == 1:
        return 1
    total = n + sum_of_n_recursive(n-1)
    return total
    
print(sum_of_n_recursive(3))
    