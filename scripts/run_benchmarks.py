import sys
import os

# Ensure the project root is in sys.path for proper package imports
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from src.benchmarking import run_benchmarks, plot_results, generate_report

def main():
    """Run matrix multiplication benchmarks using MS-MPI."""
    # Benchmark parameters
    matrix_sizes = [100, 500, 1000]
    num_processes_list = [1, 2, 4]
    
    # Run benchmarks
    serial_times, parallel_times = run_benchmarks(matrix_sizes, num_processes_list)
    
    # Generate results
    plot_results(matrix_sizes, serial_times, parallel_times, num_processes_list)
    report = generate_report(matrix_sizes, serial_times, parallel_times, num_processes_list)
    
    # Print report
    print(report)

if __name__ == "__main__":
    main()