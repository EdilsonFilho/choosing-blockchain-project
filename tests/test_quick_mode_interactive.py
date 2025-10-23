# tests/test_quick_mode_interactive.py
from unittest.mock import patch
from app.questions_quick import run_quick_mode

def generate_all_combinations(n):
    """Generate all 2^n combinations of True/False as strings 'yes'/'no'."""
    from itertools import product
    for combo in product(["no", "yes"], repeat=n):
        yield combo

def test_quick_mode_interactive_all_combinations():
    """
    Test the interactive quick mode by simulating user input.
    Covers all 32 possible combinations of 5 yes/no questions.
    """
    for combo in generate_all_combinations(5):
        with patch("rich.prompt.Prompt.ask", side_effect=list(combo)):
            # Just run the function, we only care it does not raise an exception
            run_quick_mode()
