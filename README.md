# Personal Mini-Toolkit

## Project description
The Personal Mini-Toolkit is a menu-driven Python program with three useful tools:
- **Number Guessing Game:** guess a randomly selected number from 1 to 10.
- **To-Do List:** add, view, and remove tasks while the program is running.
- **Simple Calculator:** add, subtract, multiply, and divide two numbers.

The main menu keeps running until the user chooses Quit. Invalid menu choices are handled with a friendly message.

## Files
- `toolkit_plan.txt` — the plan and exact menu text.
- `toolkit.py` — the complete Python program.
- `screenshots/` — add screenshots showing the menu, invalid-choice handling, and each tool in action.

## How to run
1. Install Python 3 if it is not already installed.
2. Open a terminal in the project folder.
3. Run:

   ```bash
   python toolkit.py
   ```

   On some computers, use `python3 toolkit.py`.

## Concepts used
Variables, input and output, type conversion, `if` / `elif` / `else`, `while` and `for` loops, lists, list methods, functions, imports, exception handling, and f-strings.

## Reflection
The most challenging part of this project was making the menu return after each tool while still allowing the user to quit cleanly. The part that needed the most careful testing was handling unexpected input, such as letters where a number was expected. I used input validation and `try` / `except` blocks to prevent the program from crashing when users enter invalid numbers. Building the to-do list helped me understand how a list can change while a program is running. I also learned how functions make a program easier to organize and read. If I had one more week, I would add the option to save tasks to a file so they are still available after the program closes.

## Screenshots
Run the program and save screenshots in this folder:
1. `menu.png` — main menu.
2. `invalid-choice.png` — enter an invalid choice such as `9` and show the friendly error message.
3. `guessing-game.png` — guessing game in action.
4. `todo-list.png` — add and view at least one task.
5. `calculator.png` — calculator showing a result.
