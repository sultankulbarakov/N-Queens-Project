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
    ├── figures/              # Generated plots and visualizations
    └── data/                 # Performance data
```

## Implementation Details

### Key Components

1. **Hill Climbing Algorithm** (`hill_climbing.py`)
   - Random initialization of queens (one per column)
   - Iterative improvement by moving queens to reduce conflicts
   - Random restarts when stuck in local optima
   
2. **Board Management** (`board.py`)
   - Efficient board representation using 1D array
   - Conflict calculation for rows and diagonals
   - State management and neighbor generation

3. **Visualization** (`visualizer.py`)
   - Performance metrics plotting
   - Board state visualization
   - Success rate and iteration analysis

### Performance Analysis (`performance_analysis.py`)
Analyzes algorithm performance across different board sizes (4x4 to 20x20) measuring:
- Success rate
- Average iterations to solution
- Conflict reduction patterns

## Experimental Results

### Success Rates
- Small boards (N=4): ~37% success rate
- Medium boards (N=8-12): 6-15% success rate
- Large boards (N=14-20): <5% success rate

### Average Iterations
- Increases with board size
- N=4: ~3 iterations
- N=20: ~11 iterations
- Performance gap at N=14 due to no successful solutions

### Key Findings
1. Algorithm performs best on smaller board sizes
2. Success rate decreases significantly with board size
3. When successful, larger boards require more iterations
4. Current implementation struggles with N≥14

## Limitations and Future Improvements

### Current Limitations
1. Low success rates for larger board sizes
2. Single-restart performance analysis may underestimate potential
3. No parallelization for multiple attempts

### Potential Improvements
1. Implement multiple restarts with parallel processing
2. Add simulated annealing to escape local optima
3. Optimize neighbor state generation
4. Implement better initial state selection

## Usage Examples

1. Running the hill climbing solver:
```python
from src.hill_climbing import NQueensSolver

solver = NQueensSolver(8)
solution = solver.solve(max_restarts=100)
if solution is not None:
    print(solver.visualize_board(solution))
```

2. Running performance analysis:
```bash
python3 analysis/performance_analysis.py
```

## Author

Sultan Kulbarakov  
Auburn University  
szk0222@auburn.edu