# File Encryption Script
This project implements a simple file encryption script using Python. The script reads the content of a file (demo.txt), encrypts it by shifting each letter to the previous letter in the alphabet, and writes the encrypted content to a new file (demo1.txt).

### Files
file_encryption.py: Contains the main encryption logic.

demo.txt: Input file containing the original text to be encrypted.

demo1.txt: Output file containing the encrypted text.

### How It Works
The script creates a dictionary that maps each letter in the alphabet to the previous letter.

The script reads the content of demo.txt.

It iterates through each character in the file, replacing it with the corresponding character from the dictionary.

The encrypted content is written to demo1.txt.

## Example output:

![Screenshot 2025-02-16 121155](https://github.com/user-attachments/assets/38d8ddf4-b6e8-4b75-b06d-20d743bf828c)

### Script Functions
Dictionary Creation: Maps each letter to the previous letter in the alphabet using string.ascii_letters.

File Reading: Reads the content of demo.txt.

Encryption Process: Iterates through each character, encrypting it based on the dictionary.

File Writing: Writes the encrypted content to demo1.txt.

### Usage
Place your original text in demo.txt.

Run the file_encryption.py script.

The encrypted text will be saved in demo1.txt.

### Dependencies
No external dependencies required.

### Author:
 Barath M
