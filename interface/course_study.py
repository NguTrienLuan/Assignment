import tkinter as tk

class CourseStudy(tk.Frame):

    def __init__(self, master, show_course, adult_learner_user, course):
        super().__init__(master)
        self.master = master
        self.show_course = show_course
        self.adult_learner_user = adult_learner_user
        self.course = course

        self.page_title= tk.Label(master=self, \
                                    text=f"Hi, {adult_learner_user.first_name}, Welcome to {self.course.name} study!", \
                                    font=("Arial Bold", 20))
        self.page_title.grid(row=1, columnspan=2, padx=10, pady=10)

        self.choose_label = tk.Label(master=self, text="Please select what you want to do")
        self.choose_label.grid(row=2, column=0, padx=10, pady=10, sticky=tk.E)

        self.lecture_label = tk.Button(self, text="Lecture")
        self.choose_label.grid(row=3, column=0, padx=10, pady=10)

        self.quiz_label = tk.Button(self,text="Quiz")
        self.quiz_label.grid(row=4, column=0, padx=10, pady=10)
        
        self.return_label = tk.Button(self,text="return to course selection", command=self.return_to_course_selection)
        self.return_label.grid(row=5, column=0, padx=10, pady=10)

    def return_to_course_selection(self):
        self.place_forget()
        self.show_course.place(relx=.5, rely=.5, anchor=tk.CENTER)
