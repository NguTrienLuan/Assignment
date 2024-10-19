"""
FIT1056 2024 Semester 2
Programming Concepts Task 4

This file contains the class definition for the HomePage class.
"""

# Third party imports
import tkinter as tk

# Local application imports
from interface.homepage import HomePage
# from interface.main_window import MSMS


class HomePage2(tk.Frame):

    def __init__(self, master, image_path):
        super().__init__(master=master)
        self.master = master # Hint: a very useful instance variable
        self.image_path = image_path
        self.homepage = HomePage(master=self.master, image_path="./images/logo.png")

        # Image obtained from: 
        # https://pngtree.com/freepng/red-blue-separation-line-musical-music-logo_6244544.html

        # Logo image
        self.logo_photoimage = tk.PhotoImage(master=self, file=self.image_path)
        self.logo_label = tk.Label(master=self, image=self.logo_photoimage, width=128, height=128)
        self.logo_label.grid(row=0, columnspan=2, sticky=tk.S, padx=10, pady=10)

        # Welcome heading
        self.login_title = tk.Label(master=self, \
            text="Welcome to EmpowerU platform", \
            font=("Arial Bold", 20))
        self.login_title.grid(row=1, columnspan=2, padx=10, pady=10)
        
        self.student_button = tk.Button(self, text="Student", command=self.show_homepage)
        self.student_button.grid(row=2, columnspan=2, padx=10, pady=10)

        self.teacher_button = tk.Button(self, text="Teacher", command=self.show_homepage)
        self.teacher_button.grid(row=3, columnspan=2, padx=10, pady=10)

        self.receptionist_button = tk.Button(self, text="Receptionist", command=self.show_homepage)
        self.receptionist_button.grid(row=4, columnspan=2, padx=10, pady=10)

        # Button to shut down
        self.shutdown_button = tk.Button(self, text="Shut down", command=master.destroy)
        self.shutdown_button.grid(row=5, columnspan=2, padx=10, pady=10)


    def show_homepage(self):
        """
        Displays the home page to make it visible in the main window.
        """
        self.place_forget()
        self.homepage.place(relx=.5, rely=.5, anchor=tk.CENTER)

    def hide_homepage(self):
        self.homepage.place_forget()
		

if __name__ == "__main__":
    # DO NOT MODIFY
    pass