# Speech Recognition Using Python

### Description

This project demonstrates how to use Python's speech_recognition library to convert speech from an audio file into text using Google Speech Recognition.

### Requirements

Make sure you have the following dependencies installed before running the script:

pip install SpeechRecognition

### Usage

Place your audio file in the same directory as the script and rename it to audiofile.wav or update the script with the correct filename.

### Run the script using:

python script.py

### Code Explanation

The script imports speech_recognition as sr.

It loads an audio file (audiofile.wav) and processes it using sr.Recognizer().

The recognize_google() function is used to convert speech to text.

The script includes exception handling for:

sr.UnknownValueError: When speech is not recognized.

sr.RequestError: When there is an issue connecting to Google Speech Recognition API.

### Example Output

![Screenshot 2025-02-15 172710](https://github.com/user-attachments/assets/6e427693-872f-4ef5-b934-4ecce79ac6d9)
