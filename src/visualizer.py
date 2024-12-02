# src/visualizer.py

import matplotlib.pyplot as plt
import numpy as np
from typing import List, Optional
import os

class NQueensVisualizer:
    def __init__(self):
        plt.style.use('seaborn-v0_8-darkgrid')
        self.colors = {
            'conflicts': 'b', # blue
            'success_rate': 'g', # green
            'iterations': 'r' # red
        }
        os.makedirs('results/figures', exist_ok=True)
        os.makedirs('results/data', exist_ok=True)

    def plot_conflicts_over_iterations(self, conflicts_history: List[int], n: int) -> None:
        plt.figure(figsize=(10, 6))
        plt.plot(range(1, len(conflicts_history) + 1), 
                conflicts_history, 
                f'{self.colors["conflicts"]}o-',  
                linewidth=2,
                markersize=6)
        plt.xlabel('Iteration')
        plt.ylabel('Number of Conflicts')
        plt.title(f'Conflicts Over Iterations for Hill Climbing (N={n})')
        plt.grid(True)
        plt.savefig(f'results/figures/conflicts_n{n}.png')
        plt.close()

    def plot_success_rate(self, board_sizes: List[int], success_rates: List[float]) -> None:
        plt.figure(figsize=(10, 6))
        plt.plot(board_sizes, 
                success_rates, 
                f'{self.colors["success_rate"]}s--', 
                linewidth=2,
                markersize=8)
        plt.xlabel('N (Board Size)')
        plt.ylabel('Success Rate')
        plt.title('Success Rate vs. N for Hill Climbing Algorithm')
        plt.grid(True)
        plt.savefig('results/figures/success_rate.png')
        plt.close()

    def plot_avg_iterations(self, board_sizes: List[int], avg_iterations: List[float]) -> None:
        plt.figure(figsize=(10, 6))
        plt.plot(board_sizes, 
                avg_iterations, 
                f'{self.colors["iterations"]}x-',  
                linewidth=2,
                markersize=8)
        plt.xlabel('N (Board Size)')
        plt.ylabel('Average Iterations')
        plt.title('Average Iterations to Solution vs. N')
        plt.grid(True)
        plt.savefig('results/figures/avg_iterations.png')
        plt.close()

    def visualize_board(self, board: np.ndarray, save: bool = False, filename: Optional[str] = None) -> None:
        n = len(board)
        plt.figure(figsize=(8, 8))
        board_img = np.zeros((n, n))
        board_img[::2, 1::2] = 1  
        board_img[1::2, ::2] = 1  
        plt.imshow(board_img, cmap='binary')
        for col, row in enumerate(board):
            plt.plot(col, row, 'ro', markersize=20, label='Queen' if col == 0 else "")
        plt.grid(True)
        plt.title(f'{n}-Queens Solution')
        plt.xticks(range(n))
        plt.yticks(range(n))
        if save:
            filename = filename or f'results/figures/board_n{n}.png'
            plt.savefig(filename)
        plt.close()

    def plot_all_metrics(self, 
                        board_sizes: List[int], 
                        success_rates: List[float],
                        avg_iterations: List[float],
                        sample_conflicts: List[int],
                        sample_n: int) -> None:
        plt.figure(figsize=(15, 10))
        # Plot 1: Success Rate
        plt.subplot(2, 2, 1)
        plt.plot(board_sizes, success_rates, f'{self.colors["success_rate"]}s--')
        plt.xlabel('N (Board Size)')
        plt.ylabel('Success Rate')
        plt.title('Success Rate vs. N')
        plt.grid(True)
        # Plot 2: Average Iterations
        plt.subplot(2, 2, 2)
        plt.plot(board_sizes, avg_iterations, f'{self.colors["iterations"]}x-')
        plt.xlabel('N (Board Size)')
        plt.ylabel('Average Iterations')
        plt.title('Average Iterations vs. N')
        plt.grid(True)
        # Plot 3: Sample Conflicts
        plt.subplot(2, 2, 3)
        plt.plot(range(1, len(sample_conflicts) + 1), sample_conflicts, f'{self.colors["conflicts"]}o-')
        plt.xlabel('Iteration')
        plt.ylabel('Number of Conflicts')
        plt.title(f'Conflicts Over Iterations (N={sample_n})')
        plt.grid(True)
        
        plt.tight_layout()
        plt.savefig('results/figures/combined_metrics.png')
        plt.close()