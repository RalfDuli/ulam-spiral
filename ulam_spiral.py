import numpy as np

class UlamSpiral:

    def __init__(self, dim) -> None:
        if dim < 2:
            self.matrix: np.array = None
            raise Exception("Dimensions of Ulam Spiral is less than 2")
        else:
            self.matrix: np.array = self.create_matrix(dim)

    def __str__(self) -> str:
        return str(self.matrix)

    def create_matrix(self, dim: int) -> np.array:
        '''
        Creates the Ulam Spiral matrix, representing
        each prime number as 1 and each nonprime
        number as 0.
        '''

        # Creates a dim x dim 0 matrix
        matrix = np.zeros(dim**2).reshape(dim, dim)

        # Draws a spiral on the matrix
        num = 1
        if dim % 2 == 0:
            row_index = np.ceil(dim/2).astype(int)
            col_index = np.floor(dim/2).astype(int) - 1
        else:
            row_index = int(dim/2)
            col_index = int(dim/2)
        steps_to_move = 1
        
        matrix[row_index][col_index] = num
        num += 1
        col_index += 1
        matrix[row_index][col_index] = num

        while True:
            try:
                # Traverse up
                for i in range(steps_to_move):
                    row_index -= 1
                    num += 1
                    matrix[row_index][col_index] = num
                is_drawing_finished = not np.any(matrix == 0)
                if is_drawing_finished:
                    break
                if num != 2 and dim != 2:
                    steps_to_move += 1
                # Traverse left
                for i in range(steps_to_move):
                    if i == dim-1: 
                        break
                    col_index -= 1
                    num += 1
                    matrix[row_index][col_index] = num
                is_drawing_finished = not np.any(matrix == 0)
                if is_drawing_finished:
                    break
                # Traverse down
                for i in range(steps_to_move):
                    row_index += 1
                    num += 1
                    matrix[row_index][col_index] = num
                is_drawing_finished = not np.any(matrix == 0)
                if is_drawing_finished:
                    break
                steps_to_move += 1
                # Traverse right
                for i in range(steps_to_move):
                    col_index += 1
                    num += 1
                    matrix[row_index][col_index] = num
                is_drawing_finished = not np.any(matrix == 0)
                if is_drawing_finished:
                    break
            except:
                break
        
        # Modifies matrix into a sequence of 1's and 0's,
        # denoting whether the number at its position
        # is prime
        vec_modify_num = np.vectorize(self.modify_num)
        matrix = vec_modify_num(matrix)
        return matrix

    def modify_num(self, n: int) -> int:
        '''
        Takes an integer n as a parameter and returns
        1 if n is prime. If not, the function returns 0.
        '''
        def is_prime(n):
            if n == 0 or n == 1: return False
            sqrt_n = np.floor(np.sqrt(n)).astype(int)
            for i in range(2, sqrt_n+1):
                if n % i == 0: return False
            return True
    
        if is_prime(n): return 1
        return 0


# Testing out Ulam Spirals with dimensions in the range [2,10)
for i in range(2,10):
    spiral = UlamSpiral(i)
    print(spiral)