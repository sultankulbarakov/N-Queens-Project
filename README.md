# N-Queens Problem Using Hill Climbing

## Project Overview

This project implements and analyzes the Hill Climbing algorithm to solve the N-Queens problem. The goal is to place N queens on an N×N chessboard such that no two queens threaten each other (no two queens share the same row, column, or diagonal).

## Installation Requirements

Required Python packages:
```bash
pip3 install numpy matplotlib
```

## Project Structure

```
N-Queens-Project/
│
├── src/
│   ├── hill_climbing.py      # Core algorithm implementation
│   ├── board.py              # Board representation and utilities
│   └── visualizer.py         # Visualization functions
│
├── analysis/
│   └── performance_analysis.py
│
└── results/
    └── figures/              # Generated plots and visualizations
```

### Core Implementation (`src/`)

#### `hill_climbing.py`
Contains the main `NQueensSolver` class that implements the hill climbing algorithm.

Key methods:
- `__init__(n)`: Creates a solver for an n×n board
- `solve(max_restarts=100, max_iterations=1000)`: Tries to find a solution using hill climbing
  - Returns a solution board if found, None otherwise
  - Records number of conflicts after each iteration
- `_calculate_conflicts(board)`: Counts how many queens are threatening each other
- `_get_best_neighbor(board)`: Finds the board configuration with fewest conflicts among neighbors
- `visualize_board(board)`: Creates a text representation of the board state

#### `board.py`
Handles the chessboard representation and basic board operations.

Key methods:
- `place_queen(col, row)`: Places a queen at the specified position
- `remove_queen(col)`: Removes a queen from a column
- `is_under_attack(row, col)`: Checks if a position is threatened by any queen
- `get_conflicts()`: Counts total conflicts on the board
- `random_state()`: Generates a random board configuration
- `get_neighbor_states()`: Generates all possible neighbor states

#### `visualizer.py`
Creates visualizations for analyzing algorithm performance.

Key methods:
- `plot_conflicts_over_iterations(conflicts_history, n)`: Shows how conflicts decrease during solving
- `plot_success_rate(board_sizes, success_rates)`: Shows success rates for different board sizes
- `plot_avg_iterations(board_sizes, avg_iterations)`: Shows average iterations needed for different sizes
- `visualize_board(board)`: Creates a graphical visualization of a board configuration

### Analysis (`analysis/`)

#### `performance_analysis.py`
Analyzes how well the algorithm performs for different board sizes.
- Tests board sizes from 4×4 to 20×20
- Measures success rates and iterations needed
- Generates plots stored in results/figures/
- Prints detailed performance statistics

## How to Run

1. Solve an N-Queens puzzle:
```python
from src.hill_climbing import NQueensSolver

# Create solver for 8×8 board
solver = NQueensSolver(8)
solution = solver.solve()

if solution is not None:
    print("Solution found!")
    print(solver.visualize_board(solution))
```

2. Run performance analysis:
```bash
python3 analysis/performance_analysis.py
```

## Results

The algorithm's performance varies with board size:
- Small boards (N=4): ~37% success rate
- Medium boards (N=8-12): 6-15% success rate
- Large boards (N=14-20): <5% success rate

Average iterations needed increases with board size:
- N=4: ~3 iterations
- N=20: ~11 iterations

Complete results and visualizations are saved in the results/figures/ directory.

## Author

Sultan Kulbarakov  
Auburn University  
szk0222@auburn.edu