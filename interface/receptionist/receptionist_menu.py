"""
FIT1056 2024 Semester 2
Programming Concepts Task 4

This file contains the class definition for the ReceptionistMenu class.
"""

# Third party imports
import tkinter as tk

# Local application imports
from interface.teacher_registion import TeacherRegistion
from interface.adult_learner_registion import AdultLearnerRegistion
from interface.search_teacher import SearchTeachers


class ReceptionistMenu(tk.Frame):

    def __init__(self, master, receptionist_user):
        """
        Constructor for the ReceptionistMenu

        Parameter(s):
        - master: master widget of this widget instance
        - receptionist_user: an instance of the ReceptionistUser class
                             representing the receptionist that has 
                             successfully logged in
        """
        super().__init__(master=master)
        self.master = master
        self.receptionist_user = receptionist_user

        self.welcome_label = tk.Label(self, text=f"Welcome in, {receptionist_user.first_name}!")
        self.welcome_label.pack(padx=10, pady=10)

        self.label1 = tk.Label(self, text="Choose one of the following:")
        self.label1.pack(padx=10, pady=10)

        self.register_btn = tk.Button(self, text="Register a student", command=self.show_register_student)
        self.register_btn.pack(padx=10, pady=10)

        self.register_btn = tk.Button(self, text="Register a teacher", command=self.show_register_teacher)
        self.register_btn.pack(padx=10, pady=10)

        self.search_btn = tk.Button(self, text="Search teachers by instrument", command=self.show_search_teachers_frame)
        self.search_btn.pack(padx=10, pady=10)

        self.logout_btn = tk.Button(self, text="Log out", command=self.logout)
        self.logout_btn.pack(padx=10, pady=10)

    def show_search_teachers_frame(self):
        """
        Method to handle the search teachers functionality upon button click.
        """
        search_teachers = SearchTeachers(self.master, self, self.receptionist_user)
        search_teachers.place(relx=.5, rely=.5, anchor=tk.CENTER)
        self.hide_menu()

    def show_register_student(self):
        register_student = AdultLearnerRegistion(self.master, self, self.receptionist_user)
        register_student.place(relx=.5, rely=.5, anchor=tk.CENTER)
        self.hide_menu()

    def show_register_teacher(self):
        register_teacher = TeacherRegistion(self.master,self, self.receptionist_user)
        register_teacher.place(relx=.5, rely=.5, anchor=tk.CENTER)
        self.hide_menu()

    def logout(self):
        """
        Method to handle the logout upon button click.

        Parameter(s):
        (None)

        Return(s):
        (None)
        """
        self.hide_menu()
        self.master.show_homepage()

    def show_menu(self):
        """
        Method to show the receptionist menu in the main window.
        """
        self.place(relx=.5, rely=.5, anchor=tk.CENTER)

    def hide_menu(self):
        """
        Method to hide the receptionist menu frame.
        """
        self.place_forget()


if __name__ == "__main__":
    # DO NOT MODIFY
    pass
