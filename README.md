# Password Generator
This is a simple terminal-based application that randomly generates passwords.

## Features
- Generates any number of passwords of any length.
- Customisation option for password complexity (can choose to in-/exclude lowercase, uppercase, numberical and special characters).
- Robust: application checks and validates user input instead of throwin an error.
- Easy-to-use.

### Table of contents:
- [Installation requirements](#installation-requirements)
- [How to run the application](#how-to-run-the-application)
- [How to use](#how-to-use)
- [File structure](#file-structure)
- [License information](#license-information)

## Installation requirements

The only requirement is a verson of Python (preferably Python 3) being installed on your computer.

## How to run the application

To run the application, enter the following line in the terminal while in the same directory as the file:

> python password-generator.py

Alternatively, use a python compiler/interpreter to run password-generator.py for you.

## How to use

The application asks you a variety of questions regarding your prefered number, length, and complexity of passwords.

For numerical inputs (length and number), the application validates the input and asks you to input a new value if the input is invalid.

For boolean inputs (complexity), you can enter your preference with `y`/`Y` for 'yes' or `n`/`N` for 'no'. If an invalid or no option is entered, the application defaults to value indicated by an uppercase after the question (e.g. if the question ends in `[Y/n]`, the question defaults to 'yes' if an invalid or no input is entered.)

After you answered all the questions, the application generates and prints the passwords with the desired preferences. After that, the application prompts the user if they want to keep using it, in which case the application loops back to the beginning. If not, the application terminates.

## File structure

```bash
.
├── password-generator.py
└── README.md

```

## License Information

None