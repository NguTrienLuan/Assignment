import tkinter as tk
from modules.course.Course import Course

class InsideCourse(tk.Frame):
    def __init__(self, master, show_course_menu, adult_learner_user, course_name):
        super().__init__(master)
        self.master = master
        self.show_course_menu = show_course_menu
        self.adult_learner_user = adult_learner_user
        self.course = Course(course_name)

        self.welcome_label = tk.Label(self, text=f"Welcome to {course_name}, {adult_learner_user.first_name}!")
        self.welcome_label.pack(padx=10, pady=10)

        self.track_label = tk.Label(self, text=f"You finished {self.course.calculate_course_track()} of this course, You almost there!")
        self.track_label.pack(padx=10, pady=10)

        self.label1 = tk.Label(self, text="Choose what you want to do:")
        self.label1.pack(padx=10, pady=10)

        self.quiz_btn = tk.Button(self, text="Quiz")
        self.quiz_btn.pack(padx=10, pady=10)

        self.lecture_btn = tk.Button(self, text="Lecture")
        self.lecture_btn.pack(padx=10, pady=10)

        self.back_btn = tk.Button(self, text="Go back to last page", command=self.return_to_show_course)
        self.back_btn.pack(padx=10, pady=10)
    
    def return_to_show_course(self):
        self.place_forget()
        self.show_course_menu.place(relx=.5, rely=.5, anchor=tk.CENTER)
