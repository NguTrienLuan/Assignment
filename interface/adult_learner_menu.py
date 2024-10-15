"""
FIT1056 2024 Semester 2
Programming Concepts Task 4

This file contains the class definition for the ReceptionistMenu class.
"""

# Third party imports
import tkinter as tk

# Local application imports
from interface.show_courses import ShowCourses
from interface.adult_learner_course_enrolll import AdultLearnerCourseEnroll
from interface.feedback_page import FeedbackPage


class AdultLearnerMenu(tk.Frame):

    def __init__(self, master, adult_learner_user):
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
        self.adult_learner_user = adult_learner_user

        self.welcome_label = tk.Label(self, text=f"Welcome in, {adult_learner_user.first_name}!")
        self.welcome_label.pack(padx=10, pady=10)

        self.label1 = tk.Label(self, text="Choose one of the following:")
        self.label1.pack(padx=10, pady=10)

        self.study_btn = tk.Button(self, text="Study", command=self.show_enrolled_course)
        self.study_btn.pack(padx=10, pady=10)

        self.search_btn = tk.Button(self, text="Enroll a course", command = self.enroll_courses)
        self.search_btn.pack(padx=10, pady=10)

        self.feedback_btn = tk.Button(self,text="FeedBack", command=self.go_to_feedback_page)
        self.feedback_btn.pack(padx=10, pady=10)

        self.logout_btn = tk.Button(self, text="Log out", command=self.logout)
        self.logout_btn.pack(padx=10, pady=10)

    def show_enrolled_course(self):
        """
        Method to handle the course studying functionality upon button click.
        """
        enrolled_courses = ShowCourses(self.master, self, self.adult_learner_user)
        enrolled_courses.place(relx=.5, rely=.5, anchor=tk.CENTER)
        self.hide_menu()

    def enroll_courses(self):
        courses_enroll = AdultLearnerCourseEnroll(self.master,self, self.adult_learner_user)
        courses_enroll.place(relx=.5, rely=.5, anchor=tk.CENTER)
        self.hide_menu()

    def go_to_feedback_page(self):
        feedback_page = FeedbackPage(self.master, self, self.adult_learner_user)
        feedback_page.place(relx=.5, rely=.5, anchor=tk.CENTER)
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
