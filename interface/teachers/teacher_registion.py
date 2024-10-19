import tkinter as tk
from utils import is_valid_date_format, is_valid_time_format, is_valid_course

class TeacherRegistion(tk.Frame):
    def __init__(self, master, receptionist_menu, receptionist_user):
        super().__init__(master)
        self.master = master
        self.receptionist_menu = receptionist_menu
        self.receptionist_user = receptionist_user

        self.page_title = tk.Label(master=self, \
                                    text="Register Teacher", \
                                    font=("Arial Bold", 20))
        self.page_title.grid(row=1, columnspan=2, padx=10, pady=10)

        self.first_name_label = tk.Label(master = self, text="Please enter you're first name")
        self.first_name_label.grid(row=2, column=0, padx=10, pady=10, sticky=tk.E)

        self.first_name_var = tk.StringVar(master=self)
        self.first_name_entry = tk.Entry(master=self, textvariable = self.first_name_var)
        self.first_name_entry.grid(row=2, column=1, padx=10, pady=10, sticky=tk.W)

        self.last_name_label = tk.Label(master = self, text="Please enter you're last name")
        self.last_name_label.grid(row=3, column=0, padx=10, pady=10, sticky=tk.E)

        self.last_name_var = tk.StringVar(master=self)
        self.last_name_entry = tk.Entry(master=self, textvariable = self.last_name_var)
        self.last_name_entry.grid(row=3, column=1, padx=10, pady=10, sticky=tk.W)

        self.phone_no_label = tk.Label(master = self, text="Please enter you're phone number")
        self.phone_no_label.grid(row=6, column=0, padx=10, pady=10, sticky=tk.E)

        self.phone_no_var = tk.StringVar(master=self)
        self.phone_no_label = tk.Entry(master=self, textvariable = self.phone_no_var)
        self.phone_no_label.grid(row=6, column=1, padx=10, pady=10, sticky=tk.W)

        self.courses_label = tk.Label(master = self, text="Please enter courses that the teacher teaches")
        self.courses_label.grid(row=7, column=0, padx=10, pady=10, sticky=tk.E)

        self.courses_var = tk.StringVar(master=self)
        self.courses_label = tk.Entry(master=self, textvariable = self.courses_var)
        self.courses_label.grid(row=7, column=1, padx=10, pady=10, sticky=tk.W)

        self.username_label = tk.Label(master = self, text="Please enter you're username")
        self.username_label.grid(row=8, column=0, padx=10, pady=10, sticky=tk.E)

        self.username_var = tk.StringVar(master=self)
        self.username_label = tk.Entry(master=self, textvariable = self.username_var)
        self.username_label.grid(row=8, column=1, padx=10, pady=10, sticky=tk.W)

        self.password_label = tk.Label(master = self, text="Please enter you're password")
        self.password_label.grid(row=9, column=0, padx=10, pady=10, sticky=tk.E)

        self.password_var = tk.StringVar(master=self)
        self.password_label = tk.Entry(master=self, textvariable = self.password_var)
        self.password_label.grid(row=9, column=1, padx=10, pady=10, sticky=tk.W)

        self.teacher_var = tk.StringVar(master=self)
        self.teacher_label = tk.Label(master=self, textvariable = self.teacher_var)
        self.teacher_label.grid(row=10, column=1, padx=10, pady=10, sticky=tk.W)

        self.search_button = tk.Button(master=self, text="Submit", command=self.check_teacher)
        self.search_button.grid(row=11, columnspan=2, padx=10, pady=10)

        self.return_button = tk.Button(self, text="Return to menu", command=self.return_to_menu)
        self.return_button.grid(row=12, columnspan=2, padx=10, pady=10)


    def check_teacher(self):
        valid_fn = False
        no = 0
        if not len(self.first_name_var.get().strip()) > 0:
            no+=1
        else:
            valid_fn = True
                
        if not len(self.last_name_var.get().strip()) > 0:
            no+=1
        else:
            valid_fn = True

        all_valid_digits = True
        for char in self.phone_no_var.get():
            if char not in "0123456789":
                all_valid_digits = False
                break
        if not (len(self.phone_no_var.get()) == 10 and all_valid_digits):
            no+=1
        else:
            valid_contact_number = True

        formatted_course = self.courses_var.get().replace(",","&")
        if not is_valid_course(self.courses_var.get()):
            no += 1
        else:
            valid_fn = True
            if valid_fn:
                formatted_course = "&".join([course.title() for course in formatted_course.split("&")])

        if no == 0:
            self.receptionist_user.store_teacher_data(self.first_name_var.get(), self.last_name_var.get(), self.phone_no_var.get(), formatted_course, self.username_var.get(), self.password_var.get())
            self.teacher_var.set("Successfully registered teacher")
        else:
            self.teacher_var.set("Failed to register teacher")


    def return_to_menu(self):
        """
        This method handles the GUI logic to return to the receptionist's menu.

        Parameters:
        (None)

        Returns:
        (None)
        """
        self.place_forget()
        self.receptionist_menu.place(relx=.5, rely=.5, anchor=tk.CENTER)