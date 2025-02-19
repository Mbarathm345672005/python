# Snakes and Ladders Game

This is a simple implementation of the classic Snakes and Ladders game using Python.

## Description

The Snakes and Ladders game is a popular board game played by two players. The objective of the game is to reach the 100th position on the board by rolling a dice. Along the way, players encounter ladders that help them move up and snakes that bring them down.

## Features

- Two-player game
- Dice rolling
- Ladders that move players up
- Snakes that bring players down
- Display of current points and positions

## How to Play

1. Enter the names of Player 1 and Player 2 when prompted.
2. Players take turns to roll the dice.
3. If a player lands on a ladder, they move up to the ladder's endpoint.
4. If a player lands on a snake, they move down to the snake's endpoint.
5. The first player to reach the 100th position wins the game.
6. Players can choose to continue or exit the game during their turn.

## Functions

### `show_image()`
Displays an image of the Snakes and Ladders board.

### `check_ladder(points)`
Checks if the current position of a player is at the base of a ladder. If so, moves the player up to the ladder's endpoint.

### `check_snake(points)`
Checks if the current position of a player is at the head of a snake. If so, moves the player down to the snake's endpoint.

### `is_reached(points)`
Checks if a player has reached the 100th position.

### `play()`
The main function that handles the game logic, including player turns, dice rolls, checking for ladders and snakes, and determining the winner.

## Dependencies

- `random` module: Used to generate random dice rolls.
- `PIL` (Python Imaging Library): Used to open and display the Snakes and Ladders board image.

## How to Run

1. Ensure you have Python installed on your system.
2. Install the PIL module using `pip install Pillow`.
3. Save the `sl.png` image in the same directory as the script.
4. Run the script using `python script_name.py`.

## Sample Output:
![Screenshot 2025-02-18 171537](https://github.com/user-attachments/assets/3b9408d3-6998-4275-a6b2-9d5884ffb404)
![Screenshot 2025-02-18 171250](https://github.com/user-attachments/assets/3e9a6f5a-fcc3-4027-a1e5-a30b523a07ca)
![Screenshot 2025-02-18 171339](https://github.com/user-attachments/assets/0c4819fc-1bb5-4e47-8174-db187bc38f3f)
![Screenshot 2025-02-18 171404](https://github.com/user-attachments/assets/95c7aa71-5d06-415d-a9e6-3b89aef0791d)
![Screenshot 2025-02-18 171424](https://github.com/user-attachments/assets/56105228-c4e4-47bc-b15a-a0f28dcd5fce)




## License

This project is licensed under the MIT License.
