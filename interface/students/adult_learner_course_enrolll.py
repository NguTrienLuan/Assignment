# Third party imports
import tkinter as tk

class AdultLearnerCourseEnroll(tk.Frame):

    def __init__(self, master, adult_learner_menu, adult_learner_user):
        super().__init__(master)
        self.master = master
        self.adult_learner_menu = adult_learner_menu
        self.adult_learner_user = adult_learner_user

        self.page_title = tk.Label(master=self, \
                                    text=f"Hi, {adult_learner_user.first_name}, here is all the class that you can enroll", \
                                    font=("Arial Bold", 20))
        self.page_title.grid(row=1, columnspan=2, padx=10, pady=10)

        self.choose_label = tk.Label(master=self, text="Please choose one to study:")
        self.choose_label.grid(row=2, column=0, padx=10, pady=10, sticky=tk.E)

        self.python_button = tk.Button(self, text = "Python")
        self.information_security_button = tk.Button(self, text = "Information Security")
        self.artificial_intelligence_button = tk.Button(self, text = "Artificial Intelligence")
        self.enrolled_all = tk.Label(master=self, text="There is not anymore class for you to enroll")

        if "python" not in self.adult_learner_user.enrolled_courses:
            self.python_button.grid(row = 3, columnspan = 2, padx=10, pady=10)
        if "information security" not in self.adult_learner_user.enrolled_courses:
            self.information_security_button.grid(row = 4, columnspan=2, padx=10, pady=10)
        if "artificial intelligence" not in self.adult_learner_user.enrolled_courses:
            self.artificial_intelligence_button.grid(row = 5, columnspan=2, padx=10, pady=10)

        if len(self.adult_learner_user.enrolled_courses) == 3:
            self.enrolled_all.grid(row = 3, columnspan = 2, padx=10, pady=10)

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


if __name__ == "__main__":
    # DO NOT MODIFY
    pass
