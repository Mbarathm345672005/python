# Tic-Tac-Toe Game
This project implements a simple command-line Tic-Tac-Toe game using Python and NumPy. The game allows two players to take turns placing their symbols ('X' and 'O') on a 3x3 board. The game ends when one player wins by aligning three of their symbols in a row, column, or diagonal, or when the board is full and the game is a draw.

### Files
tic_tac_toe.py: Contains the main game logic.

### How to Play
Run the tic_tac_toe.py script.

The game will display the initial empty board.

Players take turns entering the row and column numbers (1, 2, or 3) to place their symbol on the board.

The game will check for a win or a draw after each move.

The game ends when one player wins or the board is full.

### Game Functions
place(sym): Prompts the player to enter the row and column numbers to place their symbol on the board. The function ensures that the chosen cell is valid and empty.

won(sym): Checks if the given symbol has won the game by forming a line in a row, column, or diagonal.

check_row(sym): Checks if the given symbol has formed a line in any row.

check_col(sym): Checks if the given symbol has formed a line in any column.

check_dia(sym): Checks if the given symbol has formed a line in either diagonal.

play(): Manages the game flow, alternating turns between the two players and checking for a win or draw after each turn.

### Dependencies
NumPy: Used for creating and managing the game board.
pip install numpy

# Output for this code:

![image](https://github.com/user-attachments/assets/519fe7ce-b0fc-49fa-8645-c01648e87e6a)
![image](https://github.com/user-attachments/assets/1f8c357b-ca3f-47cb-98a1-3fb39ea6f24f)

# Author:
 Barath M


You can install NumPy using the following command:
