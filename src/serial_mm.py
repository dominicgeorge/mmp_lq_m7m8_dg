import numpy as np
import time

def serial_matrix_multiply(A, B):
    """Perform serial matrix multiplication using NumPy."""
    start_time = time.time()
    result = np.dot(A, B)
    end_time = time.time()
    return result, end_time - start_time