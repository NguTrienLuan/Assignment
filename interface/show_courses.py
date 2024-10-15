import tkinter as tk
from interface.inside_course import InsideCourse

class ShowCourses(tk.Frame):
    def __init__(self, master, adult_learner_menu, adult_learner_user):
        super().__init__(master)
        self.master = master
        self.adult_learner_menu = adult_learner_menu
        self.adult_learner_user = adult_learner_user

        self.page_title = tk.Label(master=self, \
                                    text="All the courses you have enrolled", \
                                    font=("Arial Bold", 20))
        self.page_title.grid(row=1, columnspan=2, padx=10, pady=10)

        self.username_label = tk.Label(master=self, text="Please choose one to study:")
        self.username_label.grid(row=2, column=0, padx=10, pady=10, sticky=tk.E)

        self.python_button = tk.Button(self, text = "Python",command=self.go_to_python )
        self.information_security_button = tk.Button(self, text = "Information Security",command=self.go_to_information_security)
        self.artificial_intelligence_button = tk.Button(self, text = "Artificial Intelligence",command=self.go_to_artificial_intelligence)

        if "python" in self.adult_learner_user.enrolled_courses:
            self.python_button.grid(row = 3, columnspan = 2, padx=10, pady=10)
        if "information security" in self.adult_learner_user.enrolled_courses:
            self.information_security_button.grid(row = 4, columnspan=2, padx=10, pady=10)
        if "artificial intelligence" in self.adult_learner_user.enrolled_courses:
            self.artificial_intelligence_button.grid(row = 5, columnspan=2, padx=10, pady=10)

        self.return_button = tk.Button(self, text="Return to menu", command=self.return_to_menu)
        self.return_button.grid(row=6, columnspan=2, padx=10, pady=10)

    def return_to_menu(self):
        """
        This method handles the GUI logic to return to the receptionist's menu.

        Parameters:
        (None)

        Returns:
        (None)
        """
        self.place_forget()
        self.adult_learner_menu.place(relx=.5, rely=.5, anchor=tk.CENTER)

    def go_to_python(self):
        self.place_forget()
        python_page = InsideCourse(self.master,self,self.adult_learner_user,"python")
        python_page.place(relx=.5, rely=.5, anchor=tk.CENTER)

    def go_to_information_security(self):
        self.place_forget()
        information_security_page = InsideCourse(self.master,self,self.adult_learner_user,"information security")
        information_security_page.place(relx=.5, rely=.5, anchor=tk.CENTER)

    def go_to_artificial_intelligence(self):
        self.place_forget()
        artificial_intelligence_page = InsideCourse(self.master,self, self.adult_learner_user,"artificial intelligence")
        artificial_intelligence_page.place(relx=.5, rely=.5, anchor=tk.CENTER)