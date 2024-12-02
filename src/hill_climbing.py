# src/hill_climbing.py

import numpy as np
from typing import List, Tuple, Optional
import random

class NQueensSolver:
    # Class for solving the N-Queens problem using Hill Climbing algorithm with random restarts
    def __init__(self, n: int):
        self.n = n
        self.board = None
        self.conflicts_history = []
        
    def _initialize_random_board(self) -> np.ndarray:
        # Creating random initial board configuration with one queen per column
        # And placing each queen in a random row in its column
        return np.array([random.randint(0, self.n-1) for _ in range(self.n)])
    
    def _calculate_conflicts(self, board: np.ndarray) -> int:
        # Calculating the number of conflicts between queens on the board
        conflicts = 0
        for i in range(self.n):
            for j in range(i + 1, self.n):
                # Checking for same row conflicts
                if board[i] == board[j]:
                    conflicts += 1
                # Checking for diagonal conflicts
                elif abs(board[i] - board[j]) == abs(i - j):
                    conflicts += 1
        return conflicts
    
    def _get_best_neighbor(self, board: np.ndarray) -> Tuple[np.ndarray, int]:
        # Finding the neighboring state with the lowest number of conflicts
        best_board = board.copy()
        min_conflicts = self._calculate_conflicts(board)
        # Trying moving each queen to each possible position in its column
        for col in range(self.n):
            current_row = board[col]
            for row in range(self.n):
                if row != current_row:
                    board[col] = row
                    conflicts = self._calculate_conflicts(board)
                    if conflicts < min_conflicts:
                        min_conflicts = conflicts
                        best_board = board.copy()
            board[col] = current_row
            
        return best_board, min_conflicts
    
    def solve(self, max_restarts: int = 100, max_iterations: int = 1000) -> Optional[np.ndarray]:
        # Attempting to solve the N-Queens problem using hill climbing with random restarts
        for _ in range(max_restarts):
            self.board = self._initialize_random_board()
            self.conflicts_history = []
            for iteration in range(max_iterations):
                current_conflicts = self._calculate_conflicts(self.board)
                self.conflicts_history.append(current_conflicts)
                if current_conflicts == 0:
                    return self.board
                next_board, next_conflicts = self._get_best_neighbor(self.board)
                if next_conflicts >= current_conflicts:
                    break  
                self.board = next_board
        return None  
    
    def visualize_board(self, board: Optional[np.ndarray] = None) -> str:
        # Creating string representation of the board
        if board is None:
            board = self.board 
        if board is None:
            return "No board configuration available."
        board_str = ""
        for row in range(self.n):
            for col in range(self.n):
                if board[col] == row:
                    board_str += "Q "
                else:
                    board_str += ". "
            board_str += "\n"
        return board_str

def main():
    # Testing with 8-queens
    solver = NQueensSolver(8)
    solution = solver.solve(max_restarts=100)
    if solution is not None:
        print("Solution found:")
        print(solver.visualize_board(solution))
        print("Conflicts history:", solver.conflicts_history)
    else:
        print("No solution found")

if __name__ == "__main__":
    main()