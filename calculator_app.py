"""
Course: Diploma in Information Technology
Assignment Title: Development of a Basic Calculator Using Python
Student Name: A.S.A. Ariyasinghe
Submission Type: Printed Book / Report
"""

import sys
import time
import os

# Global list to store calculation history
calculation_history = []

def clear_screen():
    """Clears the terminal screen based on the operating system."""
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def display_message(msg_type, dynamic_text=""):
    """
    Centralized function to handle all application messages and styling.
    Optimizes code footprint by reducing repetitive print blocks.
    """
    if msg_type == "exit":
        print(f"\nExiting the system. Thank you for using the program, {dynamic_text}!")
        print("=" * 50)
        # Holds the CLI screen for 3 seconds exactly as requested before exiting
        time.sleep(3)
    elif msg_type == "input_error":
        print("[ERROR] Invalid input! Please enter a valid numerical value.")
    elif msg_type == "choice_error":
        print("\n[ERROR] Invalid choice! Please select a valid operator from the menu.")
        print("\n" + "=" * 50)
    elif msg_type == "processing":
        print("\nProcessing calculation...")
        time.sleep(0.4)

def print_header():
    """Displays a professional and creative CLI header for the application."""
    print("=" * 50)
    print(" " * 7 + "DIPLOMA IN INFORMATION TECHNOLOGY")
    print(" " * 6 + "FINAL PRACTICAL ASSIGNMENT - TASK 1")
    print("=" * 50)
    print(" " * 5 + "PROJECT: BASIC CALCULATOR APPLICATION")
    print(" " * 5 + "DEVELOPED BY: A.S.A. Ariyasinghe")
    print("=" * 50 + "\n")

def print_menu():
    """Displays a user-friendly menu showing available operations and history."""
    print("Available Operations:")
    print("  [ + ] Addition")
    print("  [ - ] Subtraction")
    print("  [ * ] Multiplication")
    print("  [ / ] Division")
    print("\n")
    print("  [ H ] View Calculation History")
    print("  [ E ] Exit Application")
    print("-" * 50)

def get_number_input(prompt_text):
    """Safely gets a numeric input from the user, handling formatting errors."""
    while True:
        try:
            user_input = input(prompt_text).strip()
            if user_input.lower() == 'e':
                display_message("exit", "TwinNy")
                sys.exit()
            return float(user_input)
        except ValueError:
            display_message("input_error")

def calculate(no1, no2, operation):
    """Performs the arithmetic operation and returns the result or an error message."""
    if operation == '+':
        return no1 + no2
    elif operation == '-':
        return no1 - no2
    elif operation == '*':
        return no1 * no2
    elif operation == '/':
        if no2 == 0:
            return "[ERROR] Division by Zero is undefined!"
        return no1 / no2
    return None

def show_history():
    """Displays the formatted history of calculations."""
    clear_screen()
    print("-" * 50)
    print(" " * 15 + "CALCULATOR HISTORY")
    print("-" * 50)
    
    if not calculation_history:
        print("\n No history found. Perform some calculations first!\n")
    else:
        for record in calculation_history:
            print(record)
            print("--")
            
    print("____")
    choice = input("Go to main menu [ENTER] | Exit Application [e]: ").strip().lower()
    if choice == 'e':
        display_message("exit", "TwinNy")
        sys.exit()

def format_number(num):
    """Removes trailing zeros if the number is a whole number integer."""
    return int(num) if num.is_integer() else num

def main():
    while True:
        clear_screen()
        print_header()
        print_menu()
        
        # Step 1: Ask for the operation first
        operation = input("Select an operation symbol for the option: ").strip()
        
        # If user presses ENTER without typing anything, refresh and load menu again
        if not operation:
            continue
        
        # Check for Exit
        if operation.lower() == 'e':
            display_message("exit", "TwinNy")
            break
            
        # Check for History
        if operation.lower() == 'h':
            show_history()
            continue
            
        # Validate standard operators
        if operation not in ['+', '-', '*', '/']:
            display_message("choice_error")
            # Exact format requested for wrong choices
            choice = input("Go to main menu [ENTER] | Exit Application [e] : ").strip().lower()
            if choice == 'e':
                display_message("exit", "TwinNy")
                break
            else:
                continue
                
        # Step 2: Ask for numbers after selecting the operator
        print() # Line space
        no1 = get_number_input("Enter first number: ")
        no2 = get_number_input("Enter second number: ")
        
        display_message("processing")

        result = calculate(no1, no2, operation)
        
        # Step 3: Display and save result
        if isinstance(result, str) and result.startswith("[ERROR]"):
            print(f"\n{result}")
        else:
            formatted_no1 = format_number(no1)
            formatted_no2 = format_number(no2)
            formatted_res = format_number(result)
            
            # Exact display format with spacing
            print(f"\n\nResult = {formatted_res}")
            
            # Save string format to history list
            history_entry = f"{formatted_no1} {operation} {formatted_no2} = {formatted_res}"
            calculation_history.append(history_entry)
            
        print("\n" + "=" * 50)
        
        # Step 4: Navigation prompt
        choice = input("[ENTER] Another Calculation | [E] Exit Application : ").strip().lower()
        if choice == 'e':
            display_message("exit", "TwinNy")
            break

if __name__ == "__main__":
    main()