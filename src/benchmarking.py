import numpy as np
import matplotlib.pyplot as plt
from mpi4py import MPI
from .serial_mm import serial_matrix_multiply
from .distributed_mm import distributed_matrix_multiply
from .utils import generate_random_matrices

def run_benchmarks(matrix_sizes, num_processes_list):
    """Run benchmarks for different matrix sizes and number of processes using MS-MPI."""
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    
    serial_times = []
    parallel_times = []
    
    for n in matrix_sizes:
        # Generate test matrices
        A, B = generate_random_matrices(n)
        
        # Serial execution
        serial_time = 0
        if rank == 0:
            result, serial_time = serial_matrix_multiply(A, B)
            serial_times.append(serial_time)
            print(f"Matrix size: {n}x{n}")
            print(f"Serial time: {serial_time:.4f} seconds")
        
        # Parallel execution for different number of processes
        for num_procs in num_processes_list:
            if comm.Get_size() >= num_procs:
                C, parallel_time = distributed_matrix_multiply(A, B, n)
                if rank == 0:
                    parallel_times.append(parallel_time)
                    print(f"Parallel time ({num_procs} processes): {parallel_time:.4f} seconds")
                    # Verify results
                    if n <= 1000:  # Only verify for smaller matrices
                        serial_result, _ = serial_matrix_multiply(A, B)
                        np.testing.assert_almost_equal(C, serial_result, decimal=5)
    
    return serial_times, parallel_times

def plot_results(matrix_sizes, serial_times, parallel_times, num_processes_list):
    """Plot performance results."""
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    
    if rank == 0:
        plt.figure(figsize=(10, 6))
        plt.plot(matrix_sizes, serial_times, 'b-o', label='Serial')
        for i, num_procs in enumerate(num_processes_list):
            plt.plot(matrix_sizes, parallel_times[i::len(num_processes_list)], 
                    label=f'Parallel ({num_procs} procs)')
        
        plt.xlabel('Matrix Size')
        plt.ylabel('Execution Time (seconds)')
        plt.title('Matrix Multiplication Performance (MS-MPI)')
        plt.legend()
        plt.grid(True)
        plt.yscale('log')
        plt.savefig('performance_plot.png')
        plt.close()

def generate_report(matrix_sizes, serial_times, parallel_times, num_processes_list):
    """Generate performance report."""
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    
    if rank == 0:
        report = ["Performance Report (MS-MPI)", "================="]
        for i, n in enumerate(matrix_sizes):
            report.append(f"\nMatrix size: {n}x{n}")
            report.append(f"Serial time: {serial_times[i]:.4f} seconds")
            for j, num_procs in enumerate(num_processes_list):
                parallel_time = parallel_times[i*len(num_processes_list) + j]
                speedup = serial_times[i] / parallel_time if parallel_time > 0 else float('inf')
                report.append(f"Parallel time ({num_procs} procs): {parallel_time:.4f} seconds")
                report.append(f"Speedup: {speedup:.2f}x")
        
        with open('performance_report.txt', 'w') as f:
            f.write('\n'.join(report))
        return '\n'.join(report)