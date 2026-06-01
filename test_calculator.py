"""
Automated Unit Testing Script for the Basic Calculator Application
Student Name: A.S.A. Ariyasinghe
Covers: Integers, Floats, Validations, History, and Exception Handling
"""

import unittest
from unittest.mock import patch, MagicMock
import io
import sys

# Importing components from your core application code
# Ensure your calculator script is named 'calculator_app.py' in the same directory
import calculator_app

class TestCalculatorApplication(unittest.TestCase):

    def setUp(self):
        """Resets the shared history before running each test case."""
        calculator_app.calculation_history = []

    # ---------------------------------------------------------
    # PART 1: TESTING CORE CALCULATIONS (Integers & Floats)
    # ---------------------------------------------------------

    def test_addition_integer_and_float(self):
        """Test addition with integers and decimal float values."""
        self.assertEqual(calculator_app.calculate(10, 5, '+'), 15)
        self.assertEqual(calculator_app.calculate(10.5, 4.2, '+'), 14.7)
        self.assertEqual(calculator_app.calculate(-5, 5, '+'), 0)

    def test_subtraction_integer_and_float(self):
        """Test subtraction with integers and decimal float values."""
        self.assertEqual(calculator_app.calculate(20, 8, '-'), 12)
        self.assertEqual(calculator_app.calculate(15.5, 5.5, '-'), 10.0)
        self.assertEqual(calculator_app.calculate(5, 10, '-'), -5)

    def test_multiplication_integer_and_float(self):
        """Test multiplication with integers and decimal float values."""
        self.assertEqual(calculator_app.calculate(6, 7, '*'), 42)
        self.assertEqual(calculator_app.calculate(2.5, 4, '*'), 10.0)
        self.assertEqual(calculator_app.calculate(0, 100, '*'), 0)

    def test_division_integer_and_float(self):
        """Test standard division resulting in floating point answers."""
        self.assertEqual(calculator_app.calculate(10, 2, '/'), 5)
        self.assertEqual(calculator_app.calculate(7, 2, '/'), 3.5)
        self.assertEqual(calculator_app.calculate(100.5, 2, '/'), 50.25)

    def test_division_by_zero_handling(self):
        """Test if division by zero returns the expected safety error message."""
        result = calculator_app.calculate(10, 0, '/')
        self.assertEqual(result, "[ERROR] Division by Zero is undefined!")

    # ---------------------------------------------------------
    # PART 2: TESTING FORMATTING LOGIC
    # ---------------------------------------------------------

    def test_number_formatting(self):
        """Verify trailing decimals are cleaned up only for whole number floats."""
        self.assertEqual(calculator_app.format_number(12.0), 12)  # Should convert to int
        self.assertEqual(type(calculator_app.format_number(12.0)), int)
        
        self.assertEqual(calculator_app.format_number(12.34), 12.34) # Should stay float
        self.assertEqual(type(calculator_app.format_number(12.34)), float)


    # ---------------------------------------------------------
    # PART 3: TESTING CLI INPUT HANDLING & ERROR MESSAGES
    # ---------------------------------------------------------

    @patch('builtins.input', side_counts=None)
    def test_get_number_input_valid_and_invalid(self, mock_input):
        """Simulate continuous user prompts ensuring data safety and sanitization."""
        # Test Case A: Safe float parsing
        mock_input.return_value = "45.67"
        self.assertEqual(calculator_app.get_number_input("Enter: "), 45.67)

        # Test Case B: Recovery from an invalid text entry to a valid integer
        mock_input.side_effect = ["abc_text", "25"]
        # Capturing internal print output to verify the custom error triggers safely
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            result = calculator_app.get_number_input("Enter: ")
            self.assertEqual(result, 25.0)
            self.assertIn("[ERROR] Invalid input!", fake_out.getvalue())


    # ---------------------------------------------------------
    # PART 4: TESTING SYSTEM FLOW & NAVIGATION
    # ---------------------------------------------------------

    @patch('calculator_app.clear_screen')
    @patch('builtins.input')
    def test_main_menu_workflow_and_history(self, mock_input, mock_clear):
        """Simulates a complete interactive calculator user lifecycle workflow."""
        # Action Flow Sequence:
        # 1. Choose Addition '+'
        # 2. Enter Number 1: '12'
        # 3. Enter Number 2: '8'
        # 4. Trigger navigation prompt: Press [ENTER] to continue ('')
        # 5. Choose History Module 'h'
        # 6. From History window: Press [ENTER] to return to main menu ('')
        # 7. Choose Exit Application option 'e'
        mock_input.side_effect = ['+', '12', '8', '', 'h', '', 'e']
        
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            calculator_app.main()
            output = fake_out.getvalue()
            
            # Validating Output Expectations
            self.assertIn("Result = 20", output)
            self.assertIn("CALCULATOR HISTORY", output)
            self.assertIn("12 + 8 = 20", output)
            self.assertIn("Exiting the system.", output)

if __name__ == '__main__':
    print("\n--- STARTING AUTOMATED CALCULATOR UNIT TESTS ---")
    unittest.main()