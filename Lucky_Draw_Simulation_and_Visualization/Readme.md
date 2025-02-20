# Betting Simulation Using Random Numbers and Matplotlib

This Python program simulates a daily betting scenario over the course of a year. It uses the `random` library to generate bets and lucky draw numbers, and the `matplotlib` library to plot the changes in the account balance over time.

## How It Works

1. The program initializes an account balance to 0.
2. It generates a random bet and a lucky draw number for each day of the year (365 days).
3. If the bet matches the lucky draw number, the account balance is increased by 900 and decreased by 100 (net gain of 800).
4. If the bet does not match, the account balance is decreased by 100.
5. The daily account balance is stored and plotted using `matplotlib`.

## Usage

1. Ensure you have the `matplotlib` library installed. You can install it using pip:
   pip install matplotlib
2. Run the program. The resulting plot will display the changes in the account balance over the course of the year.

## Example Output:

### Sample Output 1:
![Screenshot 2025-02-19 170858](https://github.com/user-attachments/assets/04f9b0cb-9211-494b-b7c6-7e9a732beb17)

### Sample Output 2:
![Screenshot 2025-02-19 170926](https://github.com/user-attachments/assets/41e20b18-db72-49c4-b017-4c81f0bee27c)


