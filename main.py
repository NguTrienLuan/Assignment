"""
FIT1056 2024 Semester 2
Programming Concepts Task 4

This file contains the function definition to run the GUI application.
"""

# Third party imports
import tkinter as tk

# Local application imports
from interface.main_window import MSMS

def main():
    """
    The main function definition.

    Parameters:
    (None)

    Returns:
    (None)
    """
    root = MSMS(title="Music School Management System", width=720, height=480)
    root.mainloop()
    print("MSMS proper shutdown completed.")


if __name__ == "__main__":
    # DO NOT MODIFY
    main()
