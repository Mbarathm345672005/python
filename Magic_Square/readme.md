# Magic Square Generator in Python 🎩✨
This Python program generates a Magic Square for an odd-order (n × n) matrix using the Siamese Method (also known as the De La Loubere algorithm). A Magic Square is a special arrangement of numbers where the sum of each row, column, and diagonal is the same.

#### How the Magic Square Works
The magic square is a square grid (n × n) filled with distinct positive integers from 1 to n².

The sum of each row, column, and both diagonals is always the same, which is given by:

Magic Constant= n(n^2 +1)/2
 
#### Algorithm Used: Siamese Method
This program follows the Siamese method to generate the Magic Square:

##### Start Position:

The first number (1) is placed at the middle of the last row.

##### Placement Rule:

Move one row up and one column right to place the next number.
If moving up goes out of bounds, wrap around to the last row.
If moving right goes out of bounds, wrap around to the first column.
If the calculated cell is already occupied, move one row down and place the number.
Repeat Until All Numbers are Placed:

Continue until all numbers from 1 to n² are placed correctly.

# Sample output:


![image](https://github.com/user-attachments/assets/d831968e-7ca7-4604-84d7-131bf601c591)
