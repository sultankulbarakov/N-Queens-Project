# analysis/performance_analysis.py

import sys
import os
# Adding the project root directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.hill_climbing import NQueensSolver
from src.visualizer import NQueensVisualizer
import numpy as np
from typing import List, Tuple
import time

def analyze_performance(n: int, num_trials: int = 100) -> Tuple[float, float, List[int]]:
    # Analyzing algorithm performance for a specific board size
    solver = NQueensSolver(n)
    successes = 0
    total_iterations = 0
    sample_history = None
    for _ in range(num_trials):
        # Single restart for clean metrics
        solution = solver.solve(max_restarts=1)  
        if solution is not None:
            successes += 1
            total_iterations += len(solver.conflicts_history)
            # Keeping one successful history for plotting
            if sample_history is None:  
                sample_history = solver.conflicts_history
    
    success_rate = successes / num_trials
    avg_iterations = total_iterations / successes if successes > 0 else 0
    return success_rate, avg_iterations, sample_history

def main():
    # Running performance analysis and generate visualizations
    visualizer = NQueensVisualizer()
    # Testing range of board sizes, 4x4 through 20x20
    board_sizes = range(4, 21, 2)  
    results = []
    print("Running performance analysis...")
    for n in board_sizes:
        print(f"Analyzing {n}x{n} board...")
        success_rate, avg_iters, conflicts = analyze_performance(n)
        results.append((success_rate, avg_iters, conflicts))
        # Saving sample conflicts plot for N=12
        if n == 12 and conflicts is not None:
            visualizer.plot_conflicts_over_iterations(conflicts, n)
    # Unzipping results
    success_rates, avg_iterations, _ = zip(*results)
    # Generating individual plots
    visualizer.plot_success_rate(list(board_sizes), list(success_rates))
    visualizer.plot_avg_iterations(list(board_sizes), list(avg_iterations))
    # Generating combined plot
    sample_n = 12
    sample_conflicts = next((r[2] for i, r in enumerate(results) 
                           if board_sizes[i] == sample_n and r[2] is not None), [])
    visualizer.plot_all_metrics(
        list(board_sizes),
        list(success_rates),
        list(avg_iterations),
        sample_conflicts,
        sample_n
    )
    # Printing summary statistics
    print("\nPerformance Summary:")
    print("-------------------")
    for i, n in enumerate(board_sizes):
        print(f"Board Size {n}x{n}:")
        print(f"  Success Rate: {success_rates[i]:.2%}")
        print(f"  Avg. Iterations: {avg_iterations[i]:.2f}")
        print()

if __name__ == "__main__":
    main()