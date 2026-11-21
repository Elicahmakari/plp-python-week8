import random


# Tool 1: Play a guessing game and keep asking until the user finds the secret number.
def number_guessing_game():
    secret_number = random.randint(1, 10)
    attempts = 0

    print("\n--- Number Guessing Game ---")
    print("I am thinking of a number from 1 to 10.")

    while True:
        guess_text = input("Enter your guess (or type q to return to the menu): ").strip()

        if guess_text.lower() == "q":
            print("You left the game. Thanks for playing!")
            break

        try:
            guess = int(guess_text)
        except ValueError:
            print("Please enter a whole number, or q to return to the menu.")
            continue

        attempts += 1

        if guess < 1 or guess > 10:
            print("Choose a number between 1 and 10.")
        elif guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Correct! You guessed {secret_number} in {attempts} attempt(s).")
            break


# Tool 2: Store tasks in a list and let the user add, view, and remove tasks.
def todo_list():
    tasks = []

    print("\n--- To-Do List ---")

    while True:
        print("\n1. Add a task")
        print("2. View tasks")
        print("3. Remove a task")
        print("4. Return to main menu")

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            task = input("Enter the task: ").strip()
            if task:
                tasks.append(task)
                print(f"Added: {task}")
            else:
                print("A task cannot be empty.")

        elif choice == "2":
            if not tasks:
                print("Your to-do list is empty.")
            else:
                print("\nYour tasks:")
                for number, task in enumerate(tasks, start=1):
                    print(f"{number}. {task}")

        elif choice == "3":
            if not tasks:
                print("There are no tasks to remove.")
                continue

            for number, task in enumerate(tasks, start=1):
                print(f"{number}. {task}")

            try:
                task_number = int(input("Enter the task number to remove: "))
                if 1 <= task_number <= len(tasks):
                    removed_task = tasks.pop(task_number - 1)
                    print(f"Removed: {removed_task}")
                else:
                    print("That task number is not on the list.")
            except ValueError:
                print("Please enter a valid whole number.")

        elif choice == "4":
            print("Returning to the main menu.")
            break

        else:
            print("Please choose 1, 2, 3, or 4.")


# Tool 3: Perform addition, subtraction, multiplication, or division on two numbers.
def simple_calculator():
    print("\n--- Simple Calculator ---")

    try:
        first_number = float(input("Enter the first number: "))
        second_number = float(input("Enter the second number: "))
    except ValueError:
        print("Please enter valid numbers. Returning to the main menu.")
        return

    print("Choose an operation: +, -, *, /")
    operation = input("Operation: ").strip()

    if operation == "+":
        answer = first_number + second_number
    elif operation == "-":
        answer = first_number - second_number
    elif operation == "*":
        answer = first_number * second_number
    elif operation == "/":
        if second_number == 0:
            print("You cannot divide by zero.")
            return
        answer = first_number / second_number
    else:
        print("That operation is not supported.")
        return

    print(f"Result: {first_number:g} {operation} {second_number:g} = {answer:g}")


# Main menu: keep showing the menu until the user chooses to quit.
def main():
    print("Welcome to Your Personal Mini-Toolkit!")

    while True:
        print("\nChoose a tool:")
        print("1. Number Guessing Game")
        print("2. To-Do List")
        print("3. Simple Calculator")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            number_guessing_game()
        elif choice == "2":
            todo_list()
        elif choice == "3":
            simple_calculator()
        elif choice == "4":
            print("Thank you for using your Personal Mini-Toolkit. Goodbye!")
            break
        else:
            print("Sorry, that is not a valid choice. Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
