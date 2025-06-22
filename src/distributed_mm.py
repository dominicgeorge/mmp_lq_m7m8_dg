import numpy as np
from mpi4py import MPI
import time

def distributed_matrix_multiply(A, B, n):
    """Perform distributed matrix multiplication using Microsoft MPI (MS-MPI)."""
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()
    
    # Initialize result matrix
    C = np.zeros((n, n)) if rank == 0 else None
    
    # Calculate rows per process
    rows_per_process = n // size
    start_row = rank * rows_per_process
    end_row = start_row + rows_per_process if rank < size - 1 else n
    
    # Local computation
    local_C = np.zeros((end_row - start_row, n))
    
    start_time = time.time()
    
    # Broadcast B to all processes
    B = comm.bcast(B, root=0)
    
    # Scatter A to processes
    local_A = np.zeros((end_row - start_row, n))
    if rank == 0:
        sendbuf = A
    else:
        sendbuf = None
    counts = [rows_per_process * n] * size
    displs = [i * rows_per_process * n for i in range(size)]
    
    # Adjust counts for last process
    if rank == size - 1:
        counts[-1] = (n - (size-1) * rows_per_process) * n
    
    comm.Scatterv([sendbuf, counts, displs, MPI.DOUBLE], local_A, root=0)
    
    # Local matrix multiplication
    local_C = np.dot(local_A, B)
    
    # Gather results
    comm.Gatherv(local_C, [C, counts, displs, MPI.DOUBLE], root=0)
    
    end_time = time.time()
    
    return C, end_time - start_time