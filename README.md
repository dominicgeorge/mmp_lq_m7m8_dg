## README.md

```markdown
# Distributed Matrix Multiplication using Microsoft MPI (MS-MPI)

## Overview

This project implements a distributed matrix multiplication algorithm using Microsoft MPI (MS-MPI) in Python, benchmarked against a serial implementation. It is designed to run on Windows with VS Code, PowerShell for execution, and Git Bash for Git operations, fulfilling requirements for distributed computing, performance evaluation, and scalability testing.

## Project Structure
```

mmp_lq_m7m8_dg/
├── src/
│ ├── **init**.py
│ ├── serial_mm.py # Serial matrix multiplication implementation
│ ├── distributed_mm.py # Distributed matrix multiplication using MS-MPI
│ ├── utils.py # Utility functions (matrix generation)
│ └── benchmarking.py # Benchmarking and visualization
├── scripts/
│ └── run_benchmarks.py # Script to run benchmarks
├── requirements.txt # Project dependencies
├── README.md # Project documentation
└── LICENSE # MIT License

````

## Prerequisites
- Windows 10/11
- Python 3.8+
- Microsoft MPI (MS-MPI) Runtime and SDK
- Git Bash for Git operations
- VS Code with Python and PowerShell extensions
- Visual Studio Build Tools (for compiling mpi4py)
- Dependencies listed in `requirements.txt`

## Installation on Windows
1. **Install Microsoft MPI (MS-MPI)**:
   - Download from [Microsoft MPI Downloads](https://www.microsoft.com/en-us/download/details.aspx?id=57467):
     - `msmpisetup.exe` (Runtime)
     - `msmpisdk.msi` (SDK)
   - Run `msmpisetup.exe` and follow prompts (installs to `C:\Program Files\Microsoft MPI\Bin`).
   - Run `msmpisdk.msi` and follow prompts (installs to `C:\Program Files (x86)\Microsoft SDKs\MPI`).
   - Add `C:\Program Files\Microsoft MPI\Bin` to system PATH:
     - Right-click Start > System > Advanced system settings > Environment Variables.
     - Edit `Path` under System Variables, add the path.
   - Verify in PowerShell:
     ```powershell
     mpiexec --version
     ```

2. **Install Visual Studio Build Tools**:
   - Download from [visualstudio.microsoft.com](https://visualstudio.microsoft.com/visual-cpp-build-tools/).
   - Install the “Desktop development with C++” workload (required for mpi4py compilation).

3. **Install Python**:
   - Download Python 3.8+ from [python.org](https://www.python.org/downloads/).
   - Ensure “Add Python to PATH” is checked during installation.
   - Verify in PowerShell:
     ```powershell
     python --version
     pip --version
     ```

4. **Install Git Bash**:
   - Download from [git-scm.com](https://git-scm.com/download/win).
   - Verify in Git Bash:
     ```bash
     git --version
     ```

5. **Clone the Repository**:
   - In Git Bash:
     ```bash
     git clone https://github.com/dominicgeorge/mmp_lq_m7m8_dg.git
     cd mmp_lq_m7m8_dg
     ```

6. **Set Up Virtual Environment**:
   - In PowerShell:
     ```powershell
     cd path\to\mmp_lq_m7m8_dg
     python -m venv venv
     .\venv\Scripts\Activate.ps1
     ```

7. **Install Dependencies**:
   - In PowerShell (with virtual environment activated):
     ```powershell
     pip install -r requirements.txt
     ```
   - If `mpi4py` fails, specify MS-MPI paths:
     ```powershell
     pip install mpi4py --global-option=build_ext --global-option="-I/C:/Program Files (x86)/Microsoft SDKs/MPI/Include" --global-option="-L/C:/Program Files/Microsoft MPI/Bin" --global-option="-lmsmpi"
     ```

## Usage
1. **Open in VS Code**:
   - In PowerShell:
     ```powershell
     cd path\to\mmp_lq_m7m8_dg
     code .
     ```
   - Select the virtual environment’s Python interpreter (`.venv\Scripts\python.exe`).
   - Set PowerShell as the default terminal (File > Preferences > Settings > `terminal.integrated.defaultProfile.windows`).

2. **Run Benchmarks**:
   - In PowerShell (with virtual environment activated):
     ```powershell
     mpiexec -n 4 python scripts\run_benchmarks.py
     ```
   - Adjust `-n 4` based on CPU cores (check with `Get-CimInstance Win32_Processor | Select-Object NumberOfCores`).
   - Outputs:
     - `performance_plot.png`: Performance comparison plot.
     - `performance_report.txt`: Detailed report with execution times and speedup.
     - Console output of the report.

3. **View Results**:
   - Open `performance_plot.png` for the performance graph.
   - Open `performance_report.txt` for metrics.

## Features
- **Serial Implementation**: Uses NumPy for efficient matrix multiplication.
- **Distributed Implementation**:
  - Partitions matrix A by rows among processes using MS-MPI.
  - Uses MPI operations (broadcast, scatter, gather) for communication.
- **Benchmarking**:
  - Tests matrix sizes: 100x100, 500x500, 1000x1000.
  - Tests process counts: 1, 2, 4.
  - Measures execution time and calculates speedup.
- **Visualization**: Generates plots comparing serial and parallel performance.
- **Verification**: Validates parallel results against serial implementation.

## Performance Report
The project generates `performance_report.txt` with:
- Execution times for serial and parallel implementations.
- Speedup for different process counts and matrix sizes.

## Example Output
````

# Performance Report (MS-MPI)

Matrix size: 100x100
Serial time: 0.0001 seconds
Parallel time (1 procs): 0.0002 seconds
Speedup: 0.50x
...

````

## Notes
- Process count (`-n 4`) should not exceed CPU cores.
- Result verification is limited to matrices ≤1000x1000 to manage memory.
- If `mpiexec` fails, ensure `C:\Program Files\Microsoft MPI\Bin` is in PATH and restart PowerShell.
- If `mpi4py` fails to install, verify Visual Studio Build Tools and MS-MPI SDK are installed.

## Troubleshooting
- **mpiexec Not Found**:
  - Verify PATH includes `C:\Program Files\Microsoft MPI\Bin`.
  - Reinstall `msmpisetup.exe`.
- **mpi4py Installation Fails**:
  - Ensure `msmpisdk.msi` and Visual Studio Build Tools are installed.
  - Retry with explicit paths:
    ```powershell
    pip install mpi4py --global-option=build_ext --global-option="-I/C:/Program Files (x86)/Microsoft SDKs/MPI/Include" --global-option="-L/C:/Program Files/Microsoft MPI/Bin" --global-option="-lmsmpi"
    ```
- **Permission Errors**:
  - Run PowerShell as Administrator:
    ```powershell
    Start-Process powershell -Verb RunAs
    ```

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for improvements or bug fixes.
````
