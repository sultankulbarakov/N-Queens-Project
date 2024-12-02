# src/board.py

import numpy as np
from typing import List, Tuple

class Board:
    # Class representing the N-Queens chessboard
    def __init__(self, n: int):
        self.n = n
        self.queens = np.zeros(n, dtype=int) 
        
    def place_queen(self, col: int, row: int) -> None:
        # Placing queen at the specified position
        self.queens[col] = row
        
    def remove_queen(self, col: int) -> None:
        # Removing queen from the specified column
        self.queens[col] = -1
        
    def is_under_attack(self, row: int, col: int) -> bool:
        # Checking if a position is under attack by any queen
        # Checking row conflicts
        for i in range(col):
            if self.queens[i] == row:
                return True     
        # Checking diagonal conflicts
        for i in range(col):
            if abs(self.queens[i] - row) == abs(i - col):
                return True       
        return False
        
    def get_conflicts(self) -> int:
        # Calculating total number of conflicts on the board
        conflicts = 0
        for i in range(self.n):
            for j in range(i + 1, self.n):
                # Checking row conflicts
                if self.queens[i] == self.queens[j]:
                    conflicts += 1
                # Checking diagonal conflicts
                elif abs(self.queens[i] - self.queens[j]) == abs(i - j):
                    conflicts += 1
        return conflicts
        
    def random_state(self) -> None:
        # Generating random board state with one queen per column
        self.queens = np.random.randint(0, self.n, size=self.n)
        
    def get_state(self) -> np.ndarray:
        # Getting current board state
        return self.queens.copy()
        
    def set_state(self, state: np.ndarray) -> None:
        # Setting board to a specific state
        self.queens = state.copy()
        
    def display(self) -> str:
        # Creating string representation of the board
        board_str = ""
        for row in range(self.n):
            for col in range(self.n):
                if self.queens[col] == row:
                    board_str += "Q "
                else:
                    board_str += ". "
            board_str += "\n"
        return board_str
    
    def get_neighbor_states(self) -> List[np.ndarray]:
        # Generating all possible neighbor states from current state
        neighbors = []
        for col in range(self.n):
            current_row = self.queens[col]
            for row in range(self.n):
                if row != current_row:
                    new_state = self.queens.copy()
                    new_state[col] = row
                    neighbors.append(new_state)
        return neighbors