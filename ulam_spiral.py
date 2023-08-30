import numpy as np

def create_matrix(n):
    dim = np.ceil(np.sqrt(n)).astype(int)
    matrix = np.arange(1, n)
    num_to_pad = dim**2-n
    matrix = np.pad(matrix, (0, num_to_pad+1))
    matrix = matrix.reshape(dim, dim)
    vec_modify_num = np.vectorize(modify_num)
    matrix = vec_modify_num(matrix)
    return matrix

def is_prime(n):
    if n == 0 or n == 1: return False
    sqrt_n = np.floor(np.sqrt(n)).astype(int)
    for i in range(2, sqrt_n+1):
        if n % i == 0: return False
    return True

def modify_num(n):
    if is_prime(n): return 1
    return 0

print(create_matrix(28))
