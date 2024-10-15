"""
FIT1056 2024 Semester 2
Programming Concepts Task 4
"""

# Third party imports
import tkinter as tk

# Local application imports
from interface.homepage import HomePage

class MSMS(tk.Tk):

    def __init__(self, title, width, height):
        """
        Constructor for the MSMS class.

        Parameter(s):
        - title: str
        - width: int, width of window in pixels
        - height: int, height of window in pixels
        """
        super().__init__()
        super().title(title)
        super().geometry(f"{width}x{height}")

        self.homepage = HomePage(master=self, image_path="./images/logo.png")
        self.show_homepage()

    def show_homepage(self):
        """
        Displays the home page to make it visible in the main window.
        """
        self.homepage.place(relx=.5, rely=.5, anchor=tk.CENTER)

    def hide_homepage(self):
        """
        Hides the home page to make it invisible in the main window.
        """
        self.homepage.place_forget()



if __name__ == "__main__":
    # DO NOT MODIFY
    pass