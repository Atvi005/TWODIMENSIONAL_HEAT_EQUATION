# Two Dimensional Heat Conduction Solver

This repository contains an optimized Python script that solves the 2D steady-state heat conduction equation (Laplace's equation) on a square grid using the Finite Difference Method (FDM).

## Overview

The solver simulates the temperature distribution across a 2D domain where the top boundary is held at a constant high temperature ($T=1$), and the other boundaries are initially at $T=0$. It iterates until the system reaches a steady thermal state (when the numerical error drops below a defined threshold, $\epsilon$).

The original implementation relied on nested `for` loops, which are notably slow in Python. This version has been significantly optimized for speed and readability using **NumPy vectorization**.

## Key Features & Optimizations

*   **Vectorized Math:** Replaced nested `for` loops with NumPy array slicing. The temperature of each node is calculated simultaneously as the average of its North, South, East, and West neighbors, speeding up execution by 50x-100x.
*   **Memory Efficiency:** Array states are updated in place (`T[:] = T_new`) rather than allocating new memory structures on every iteration.
*   **Deferred Plotting:** Convergence data is appended to lists during calculation and plotted at the very end. This eliminates the massive CPU overhead caused by live-plotting every 1,000 iterations.
*   **Enhanced Visualization:** Uses `matplotlib.pyplot.contourf` with the `viridis` colormap to generate a clear, human-readable heatmap of the final temperature distribution.

## Requirements

Ensure you have Python 3 installed along with the following libraries:

```bash
pip install numpy matplotlib
```

## Usage

Simply run the script in your terminal or IDE:

```bash
python main.py
```

### Outputs
Upon completion, the script will output the total number of iterations required to reach steady-state and generate two plots:
1.  **Convergence History:** A semi-log plot showing the numerical error decreasing over the iterations.
2.  **Temperature Distribution:** A filled contour map illustrating the final steady-state temperature gradient across the grid.

## Configuration

You can easily modify the grid parameters at the top of the script:
*   `N`: Grid resolution (default is 51x51). Higher values yield higher resolution but take longer to compute.
*   `L`: Length of the domain.
*   `epsilon`: The convergence tolerance (default is `1e-8`).
